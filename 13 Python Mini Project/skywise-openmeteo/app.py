import json
import os
import threading
import time
from collections import Counter
from datetime import datetime, timezone
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from openai import AuthenticationError, OpenAI, PermissionDeniedError, RateLimitError

load_dotenv()

app = Flask(__name__)
AI_PROVIDER = os.getenv("AI_PROVIDER", "ollama").strip().lower()
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434").strip().rstrip("/")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2").strip()
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "").strip()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite").strip()
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini").strip()
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
METNO_FORECAST_URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
METNO_USER_AGENT = "SkyWiseWeather/1.0 (https://github.com/AdityaMane231105/skywise-openmeteo)"
REQUEST_TIMEOUT = 15
PORT = int(os.getenv("PORT", "5001"))
WEATHER_CACHE_TTL = 600
WEATHER_CACHE_MAX_ENTRIES = 128
_weather_cache = {}
_weather_cache_lock = threading.Lock()


class WeatherAPIError(Exception):
    """A safe, user-displayable weather API error."""

    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code


def request_json(url, params, headers=None):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.Timeout as exc:
        raise WeatherAPIError("The weather service took too long to respond. Please try again.") from exc
    except requests.HTTPError as exc:
        status_code = exc.response.status_code if exc.response is not None else None
        app.logger.warning(
            "Weather provider %s returned HTTP %s",
            urlsplit(url).hostname,
            status_code,
        )
        if status_code == 429:
            message = "The weather service is receiving too many requests. Wait a moment and try again."
        else:
            message = "The weather service request failed. Please try again shortly."
        raise WeatherAPIError(message, status_code=status_code) from exc
    except (requests.RequestException, ValueError) as exc:
        raise WeatherAPIError("Could not retrieve weather data. Check your internet connection and try again.") from exc


def find_city(city):
    data = request_json(GEOCODING_URL, {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json",
    })
    results = data.get("results") or []
    if not results:
        raise WeatherAPIError("City not found. Check the spelling or include the country name.")
    return results[0]


def metno_weather_code(symbol_code):
    symbol = symbol_code.split("_", 1)[0]
    return {
        "clearsky": 0,
        "fair": 1,
        "partlycloudy": 2,
        "cloudy": 3,
        "fog": 45,
        "lightrain": 61,
        "rain": 63,
        "heavyrain": 65,
        "lightsleet": 66,
        "sleet": 66,
        "heavysleet": 67,
        "lightsnow": 71,
        "snow": 73,
        "heavysnow": 75,
        "lightrainshowers": 80,
        "rainshowers": 81,
        "heavyrainshowers": 82,
        "lightsnowshowers": 85,
        "snowshowers": 85,
        "heavysnowshowers": 86,
        "lightrainandthunder": 95,
        "rainandthunder": 95,
        "heavyrainandthunder": 96,
        "snowandthunder": 96,
        "sleetandthunder": 96,
        "thunderstorm": 95,
    }.get(symbol, 3)


def normalise_metno(place, data):
    entries = data.get("properties", {}).get("timeseries", [])
    if not entries:
        raise WeatherAPIError("The alternate weather service returned no forecast data.")

    try:
        location_timezone = ZoneInfo(place.get("timezone") or "UTC")
    except KeyError:
        location_timezone = timezone.utc

    now = datetime.now(timezone.utc)
    parsed_entries = [
        (
            datetime.fromisoformat(entry["time"].replace("Z", "+00:00")),
            entry.get("data", {}),
        )
        for entry in entries
    ]
    past_entries = [entry for entry in parsed_entries if entry[0] <= now]
    current_time, current_data = past_entries[-1] if past_entries else parsed_entries[0]
    current_details = current_data.get("instant", {}).get("details", {})
    current_symbol = (
        current_data.get("next_1_hours", {}).get("summary", {}).get("symbol_code")
        or current_data.get("next_6_hours", {}).get("summary", {}).get("symbol_code")
        or "cloudy_day"
    )
    current_code = metno_weather_code(current_symbol)
    current_temperature = float(current_details.get("air_temperature", 0))
    current = {
        "temperature_2m": current_temperature,
        "relative_humidity_2m": int(round(float(current_details.get("relative_humidity", 0)))),
        "apparent_temperature": current_temperature,
        "is_day": int(current_symbol.endswith("_day")),
        "weather_code": current_code,
        "wind_speed_10m": round(float(current_details.get("wind_speed", 0)) * 3.6, 1),
        "pressure_msl": float(current_details.get("air_pressure_at_sea_level", 0)),
    }

    daily_entries = {}
    for entry_time, entry_data in parsed_entries:
        local_date = entry_time.astimezone(location_timezone).date()
        if local_date < now.astimezone(location_timezone).date():
            continue
        details = entry_data.get("instant", {}).get("details", {})
        temperature = details.get("air_temperature")
        if temperature is None:
            continue
        day = daily_entries.setdefault(local_date, {"temperatures": [], "codes": []})
        day["temperatures"].append(float(temperature))
        symbol = (
            entry_data.get("next_6_hours", {}).get("summary", {}).get("symbol_code")
            or entry_data.get("next_1_hours", {}).get("summary", {}).get("symbol_code")
            or "cloudy_day"
        )
        day["codes"].append(metno_weather_code(symbol))

    forecast_dates = sorted(daily_entries)[:5]
    daily = {
        "time": [day.isoformat() for day in forecast_dates],
        "weather_code": [
            Counter(daily_entries[day]["codes"]).most_common(1)[0][0]
            for day in forecast_dates
        ],
        "temperature_2m_max": [
            max(daily_entries[day]["temperatures"]) for day in forecast_dates
        ],
        "temperature_2m_min": [
            min(daily_entries[day]["temperatures"]) for day in forecast_dates
        ],
        "precipitation_probability_max": [None] * len(forecast_dates),
    }
    return {"current": current, "daily": daily}


def weather_description(code, is_day=True):
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Depositing rime fog",
        51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
        56: "Light freezing drizzle", 57: "Dense freezing drizzle",
        61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        66: "Light freezing rain", 67: "Heavy freezing rain",
        71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow", 77: "Snow grains",
        80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
        85: "Slight snow showers", 86: "Heavy snow showers",
        95: "Thunderstorm", 96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail",
    }
    # WMO weather interpretation codes used by Open-Meteo.
    return descriptions.get(code, "Unknown conditions")


def weather_icon(code, is_day=True):
    if code == 0:
        return "sun" if is_day else "moon"
    if code in (1, 2):
        return "partly-cloudy"
    if code in (3, 45, 48):
        return "cloud"
    if code in (51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82):
        return "rain"
    if code in (71, 73, 75, 77, 85, 86):
        return "snow"
    if code in (95, 96, 99):
        return "thunderstorm"
    return "cloud"


def fetch_for_city(city):
    cache_key = city.casefold()
    now = time.monotonic()
    with _weather_cache_lock:
        cached = _weather_cache.get(cache_key)
        if cached and cached[0] > now:
            return cached[1], cached[2]

        place = find_city(city)
        try:
            data = request_json(FORECAST_URL, {
                "latitude": place["latitude"],
                "longitude": place["longitude"],
                "current": (
                    "temperature_2m,relative_humidity_2m,apparent_temperature,is_day,"
                    "precipitation,weather_code,pressure_msl,visibility,wind_speed_10m"
                ),
                "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max",
                "timezone": "auto",
                "forecast_days": 7,
                "wind_speed_unit": "ms",
            })
        except WeatherAPIError as exc:
            if exc.status_code != 429:
                raise
            app.logger.warning("Open-Meteo forecast was rate-limited; using MET Norway fallback")
            fallback_data = request_json(
                METNO_FORECAST_URL,
                {"lat": place["latitude"], "lon": place["longitude"]},
                headers={"User-Agent": METNO_USER_AGENT},
            )
            data = normalise_metno(place, fallback_data)

        expired = [
            key for key, entry in _weather_cache.items()
            if entry[0] <= now
        ]
        for key in expired:
            del _weather_cache[key]
        if len(_weather_cache) >= WEATHER_CACHE_MAX_ENTRIES:
            oldest_key = min(_weather_cache, key=lambda key: _weather_cache[key][0])
            del _weather_cache[oldest_key]
        _weather_cache[cache_key] = (time.monotonic() + WEATHER_CACHE_TTL, place, data)
        return place, data


def normalise_current(place, data):
    current = data.get("current") or {}
    code = int(current.get("weather_code", -1))
    visibility = current.get("visibility")
    return {
        "city": place.get("name", "Unknown location"),
        "country": place.get("country_code", ""),
        "temperature": round(float(current.get("temperature_2m", 0)), 1),
        "feels_like": round(float(current.get("apparent_temperature", current.get("temperature_2m", 0))), 1),
        "condition": weather_description(code, bool(current.get("is_day", 1))),
        "icon": weather_icon(code, bool(current.get("is_day", 1))),
        "humidity": int(current.get("relative_humidity_2m", 0)),
        "wind_speed": round(float(current.get("wind_speed_10m", 0)), 1),
        "pressure": int(round(float(current.get("pressure_msl", 0)))),
        "visibility": round(float(visibility) / 1000, 1) if visibility is not None else None,
        "updated_at": datetime.now().isoformat(timespec="minutes"),
    }


def normalise_forecast(data):
    daily = data.get("daily") or {}
    dates = daily.get("time", [])
    days = []
    for index, date_key in enumerate(dates[:5]):
        code = int(daily.get("weather_code", [])[index])
        date = datetime.strptime(date_key, "%Y-%m-%d")
        rain_values = daily.get("precipitation_probability_max", [])
        rain_probability = rain_values[index] if index < len(rain_values) else None
        days.append({
            "date": date_key,
            "day": date.strftime("%a"),
            "label": date.strftime("%b %d"),
            "min": round(float(daily.get("temperature_2m_min", [0])[index])),
            "max": round(float(daily.get("temperature_2m_max", [0])[index])),
            "condition": weather_description(code),
            "icon": weather_icon(code),
            "pop": int(rain_probability) if rain_probability is not None else None,
        })
    return days


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/api/weather")
def current_weather():
    city = request.args.get("city", "").strip()
    if not city:
        return jsonify(error="Enter a city name to search."), 400
    if len(city) > 100:
        return jsonify(error="City name is too long."), 400
    try:
        place, data = fetch_for_city(city)
        current = normalise_current(place, data)
        current["days"] = normalise_forecast(data)
        return jsonify(current)
    except WeatherAPIError as exc:
        return jsonify(error=str(exc)), 502


@app.get("/api/forecast")
def forecast():
    city = request.args.get("city", "").strip()
    if not city:
        return jsonify(error="Enter a city name to search."), 400
    if len(city) > 100:
        return jsonify(error="City name is too long."), 400
    try:
        place, data = fetch_for_city(city)
        return jsonify({"city": place.get("name", city), "days": normalise_forecast(data)})
    except WeatherAPIError as exc:
        return jsonify(error=str(exc)), 502


@app.post("/api/ai-advice")
def ai_advice():
    body = request.get_json(silent=True) or {}
    weather = body.get("weather")
    question = str(body.get("question", "")).strip()
    if not isinstance(weather, dict):
        return jsonify(error="Search for a city first so the assistant has weather data."), 400
    if len(question) > 500:
        return jsonify(error="Please keep your question under 500 characters."), 400
    if not question:
        question = "Summarise this weather and give practical suggestions for today."

    safe_weather = {key: weather.get(key) for key in (
        "city", "country", "temperature", "feels_like", "condition", "humidity",
        "wind_speed", "pressure", "visibility"
    )}
    system_message = (
        "You are SkyWise, a friendly weather assistant. Use the supplied weather data as "
        "the source of truth. Do not invent forecast details. Give concise, practical advice. "
        "Mention that weather can change and that official alerts should be checked for safety."
    )
    weather_context = (
        f"Current weather data (metric units): {json.dumps(safe_weather)}\n\n"
        f"User question: {question}"
    )

    try:
        if AI_PROVIDER == "ollama":
            ollama_host = urlsplit(OLLAMA_BASE_URL).hostname
            ollama_is_local = ollama_host in {"127.0.0.1", "localhost", "::1"}
            if not ollama_is_local and not OLLAMA_API_KEY:
                return jsonify(error="Ollama Cloud is not configured. Add OLLAMA_API_KEY in the hosting environment settings."), 503
            headers = (
                {"Authorization": f"Bearer {OLLAMA_API_KEY}"}
                if OLLAMA_API_KEY
                else {}
            )
            try:
                response = requests.post(
                    f"{OLLAMA_BASE_URL}/api/chat",
                    headers=headers,
                    json={
                        "model": OLLAMA_MODEL,
                        "messages": [
                            {"role": "system", "content": system_message},
                            {"role": "user", "content": weather_context},
                        ],
                        "stream": False,
                        "options": {"temperature": 0.3, "num_predict": 256},
                    },
                    timeout=(5, 180),
                )
                response.raise_for_status()
                result = response.json()
            except requests.ConnectionError as exc:
                app.logger.warning("Could not connect to the Ollama server: %s", exc)
                if ollama_is_local:
                    message = "Could not connect to Ollama. Make sure the Ollama app is running on this computer."
                else:
                    message = "Could not connect to Ollama Cloud. Please try again shortly."
                return jsonify(error=message), 503
            except requests.Timeout as exc:
                app.logger.warning("Ollama timed out while generating AI advice: %s", exc)
                return jsonify(error="Ollama is taking too long to respond. Please try again."), 504
            except requests.HTTPError as exc:
                status_code = exc.response.status_code if exc.response is not None else None
                if status_code in (401, 403):
                    message = "Ollama rejected the API key. Check OLLAMA_API_KEY in your hosting settings."
                    app.logger.warning("Ollama rejected the configured API key (HTTP %s)", status_code)
                elif status_code == 404 and ollama_is_local:
                    message = (
                        f"The Ollama model '{OLLAMA_MODEL}' was not found. "
                        f"Download it with: ollama pull {OLLAMA_MODEL}"
                    )
                elif status_code == 404:
                    message = f"The Ollama Cloud model '{OLLAMA_MODEL}' was not found or is unavailable to this account."
                    app.logger.warning("Ollama Cloud model was not found or available: %s", OLLAMA_MODEL)
                elif status_code == 429:
                    message = "Ollama Cloud rate limit reached. Please wait and try again."
                    app.logger.warning("Ollama Cloud rate limit reached")
                else:
                    app.logger.exception("Ollama returned an HTTP error (HTTP %s)", status_code)
                    if ollama_is_local:
                        message = "Ollama could not generate an answer. Check that its local service is working."
                    else:
                        message = "Ollama Cloud could not generate an answer. Please try again shortly."
                return jsonify(error=message), 502
            except (requests.RequestException, ValueError):
                app.logger.exception("Could not read a valid response from Ollama")
                return jsonify(error="Ollama returned an invalid response. Check that its local service is working."), 502

            answer = (result.get("message") or {}).get("content", "").strip()
        elif AI_PROVIDER == "openai":
            if not OPENAI_API_KEY or OPENAI_API_KEY == "replace_with_your_openai_api_key":
                return jsonify(error="AI advice is not configured. Add your OpenAI API key to the .env file; weather search works without it."), 503
            client = OpenAI(api_key=OPENAI_API_KEY, timeout=25.0, max_retries=1)
            response = client.responses.create(
                model=OPENAI_MODEL,
                instructions=system_message,
                input=weather_context,
            )
            answer = response.output_text.strip()
        elif AI_PROVIDER == "gemini":
            if not GEMINI_API_KEY:
                return jsonify(error="AI advice is not configured. Add GEMINI_API_KEY in the hosting environment settings."), 503
            try:
                response = requests.post(
                    f"{GEMINI_API_URL}/{GEMINI_MODEL}:generateContent",
                    headers={"x-goog-api-key": GEMINI_API_KEY},
                    json={
                        "systemInstruction": {"parts": [{"text": system_message}]},
                        "contents": [{"role": "user", "parts": [{"text": weather_context}]}],
                        "generationConfig": {"temperature": 0.3, "maxOutputTokens": 384},
                    },
                    timeout=(5, 60),
                )
                response.raise_for_status()
                result = response.json()
            except requests.ConnectionError as exc:
                app.logger.warning("Could not connect to the Gemini API: %s", exc)
                return jsonify(error="Could not connect to the AI service. Please try again shortly."), 502
            except requests.Timeout as exc:
                app.logger.warning("Gemini timed out while generating AI advice: %s", exc)
                return jsonify(error="The AI service is taking too long to respond. Please try again."), 504
            except requests.HTTPError as exc:
                status_code = exc.response.status_code if exc.response is not None else None
                if status_code in (401, 403):
                    message = "The Gemini API key is invalid or does not have access. Check GEMINI_API_KEY in your hosting settings."
                    app.logger.warning("Gemini rejected the configured API key (HTTP %s)", status_code)
                elif status_code == 429:
                    message = "The Gemini API quota or rate limit was reached. Check your Google AI API usage and try again later."
                    app.logger.warning("Gemini API quota or rate limit reached")
                elif status_code == 404:
                    message = f"The Gemini model '{GEMINI_MODEL}' was not found. Check the GEMINI_MODEL setting."
                    app.logger.warning("Gemini model was not found: %s", GEMINI_MODEL)
                else:
                    app.logger.exception("Gemini returned an HTTP error (HTTP %s)", status_code)
                    message = "The AI service could not generate an answer. Please try again shortly."
                return jsonify(error=message), 502
            except (requests.RequestException, ValueError):
                app.logger.exception("Could not read a valid response from Gemini")
                return jsonify(error="The AI service returned an invalid response. Please try again shortly."), 502

            candidates = result.get("candidates") or []
            parts = (candidates[0].get("content") or {}).get("parts", []) if candidates else []
            answer = "\n".join(
                part["text"].strip()
                for part in parts
                if isinstance(part.get("text"), str) and part["text"].strip()
            )
        else:
            app.logger.error("Unsupported AI_PROVIDER configuration: %s", AI_PROVIDER)
            return jsonify(error="The AI provider is not configured correctly. Set AI_PROVIDER to 'ollama', 'openai', or 'gemini' and restart SkyWise."), 503

        if not answer:
            raise RuntimeError("The AI returned an empty response.")
        return jsonify(answer=answer)
    except AuthenticationError:
        app.logger.exception("OpenAI rejected the configured API key")
        return jsonify(error="OpenAI rejected the API key. Check OPENAI_API_KEY in .env and restart SkyWise."), 502
    except PermissionDeniedError:
        app.logger.exception("OpenAI denied access to the configured model")
        return jsonify(error="The OpenAI account does not have access to this model. Check OPENAI_MODEL and your API project permissions."), 502
    except RateLimitError as exc:
        if exc.code in {"insufficient_quota", "credit_balance_exhausted"}:
            message = (
                "Your OpenAI API account has no credits remaining. Add API billing credits at "
                "https://platform.openai.com/settings/organization/billing/ to use SkyWise AI."
            )
        else:
            message = "The OpenAI API rate limit was reached. Please wait a moment and try again."
        app.logger.warning("OpenAI rate limit while generating AI advice (code=%s)", exc.code)
        return jsonify(error=message), 502
    except Exception:
        app.logger.exception("AI advice request failed")
        return jsonify(error="The AI assistant is temporarily unavailable. Check your API key, model access, and connection."), 502


@app.errorhandler(404)
def not_found(_error):
    if request.path.startswith("/api/"):
        return jsonify(error="API endpoint not found."), 404
    return render_template("index.html"), 404


@app.errorhandler(500)
def internal_error(_error):
    app.logger.exception("Unhandled server error")
    if request.path.startswith("/api/"):
        return jsonify(error="An unexpected server error occurred."), 500
    return "An unexpected server error occurred. Check the terminal for details.", 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=PORT,
        debug=os.getenv("FLASK_DEBUG", "false").lower() == "true",
    )
