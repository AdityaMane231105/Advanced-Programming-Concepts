const form = document.getElementById("search-form");
const cityInput = document.getElementById("city-input");
const searchButton = document.getElementById("search-button");
const statusMessage = document.getElementById("status-message");
const weatherSection = document.getElementById("weather-section");
const forecastGrid = document.getElementById("forecast-grid");
const aiForm = document.getElementById("ai-form");
const aiQuestion = document.getElementById("ai-question");
const aiSubmit = document.getElementById("ai-submit");
const aiAnswer = document.getElementById("ai-answer");

let currentWeather = null;
document.getElementById("year").textContent = new Date().getFullYear();

function setStatus(message, loading = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("loading", loading);
}

async function getJSON(url, options = {}) {
  let response;
  try {
    response = await fetch(url, options);
  } catch (_error) {
    throw new Error("Could not reach the app server. Check your connection and make sure Flask is running.");
  }
  let data;
  try {
    data = await response.json();
  } catch (_error) {
    throw new Error("The server returned an unexpected response.");
  }
  if (!response.ok) throw new Error(data.error || "Something went wrong.");
  return data;
}

function iconURL(code) {
  const icons = {
    sun: "☀️", moon: "🌙", "partly-cloudy": "🌤️", cloud: "☁️",
    rain: "🌧️", snow: "❄️", thunderstorm: "⛈️"
  };
  const emoji = icons[code] || "🌡️";
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96"><text x="48" y="67" text-anchor="middle" font-size="64">${emoji}</text></svg>`;
  return `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}`;
}

function renderCurrent(data) {
  currentWeather = data;
  document.getElementById("location-name").textContent =
    `${data.city}${data.country ? ", " + data.country : ""}`;
  document.getElementById("condition-text").textContent = data.condition;
  document.getElementById("temperature").textContent = Math.round(data.temperature);
  document.getElementById("feels-like").textContent = `Feels like ${Math.round(data.feels_like)}°C`;
  document.getElementById("humidity").textContent = `${data.humidity}%`;
  document.getElementById("wind").textContent = `${data.wind_speed} m/s`;
  document.getElementById("pressure").textContent = `${data.pressure} hPa`;
  document.getElementById("visibility").textContent =
    data.visibility == null ? "—" : `${data.visibility} km`;
  const icon = document.getElementById("current-icon");
  icon.src = iconURL(data.icon);
  icon.alt = data.condition;
  document.getElementById("updated-at").textContent =
    `Updated ${new Date(data.updated_at).toLocaleTimeString([], {hour:"2-digit", minute:"2-digit"})}`;
}

function renderForecast(days) {
  forecastGrid.replaceChildren();
  if (!days || !days.length) {
    forecastGrid.textContent = "Forecast data is not available for this location.";
    return;
  }
  days.forEach((day) => {
    const card = document.createElement("article");
    card.className = "forecast-card";
    const title = document.createElement("div");
    title.className = "forecast-day";
    title.textContent = day.day;
    const date = document.createElement("div");
    date.className = "forecast-date";
    date.textContent = day.label;
    const icon = document.createElement("img");
    icon.className = "forecast-icon";
    icon.src = iconURL(day.icon);
    icon.alt = day.condition;
    const condition = document.createElement("div");
    condition.className = "forecast-condition";
    condition.textContent = day.condition;
    const temps = document.createElement("div");
    temps.className = "forecast-temps";
    const high = document.createElement("span");
    high.textContent = `${day.max}°`;
    const low = document.createElement("span");
    low.textContent = `${day.min}°`;
    temps.append(high, low);
    const rain = document.createElement("div");
    rain.className = "rain-chance";
    rain.textContent = day.pop == null ? "☂ Precipitation chance unavailable" : `☂ ${day.pop}% chance`;
    card.append(title, date, icon, condition, temps, rain);
    forecastGrid.append(card);
  });
}

async function searchCity(city) {
  if (!city.trim()) {
    setStatus("Please enter a city name.");
    return;
  }
  searchButton.disabled = true;
  setStatus(`Getting the latest weather for ${city.trim()}…`, true);
  aiAnswer.classList.add("hidden");
  aiAnswer.textContent = "";
  try {
    const encoded = encodeURIComponent(city.trim());
    const weather = await getJSON(`/api/weather?city=${encoded}`);
    renderCurrent(weather);
    renderForecast(weather.days);
    weatherSection.classList.remove("hidden");
    setStatus("");
    weatherSection.scrollIntoView({behavior:"smooth", block:"start"});
  } catch (error) {
    setStatus(error.message);
  } finally {
    searchButton.disabled = false;
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  searchCity(cityInput.value);
});

document.querySelectorAll(".city-chip").forEach((button) => {
  button.addEventListener("click", () => {
    cityInput.value = button.dataset.city;
    searchCity(button.dataset.city);
  });
});

async function askAI(question) {
  if (!currentWeather) {
    setStatus("Search for a city before asking the AI assistant.");
    return;
  }
  aiSubmit.disabled = true;
  aiAnswer.classList.remove("hidden");
  aiAnswer.textContent = "SkyWise is thinking…";
  try {
    const data = await getJSON("/api/ai-advice", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({weather: currentWeather, question})
    });
    aiAnswer.textContent = data.answer;
  } catch (error) {
    aiAnswer.textContent = error.message;
  } finally {
    aiSubmit.disabled = false;
  }
}

aiForm.addEventListener("submit", (event) => {
  event.preventDefault();
  askAI(aiQuestion.value.trim());
});

document.querySelectorAll("[data-question]").forEach((button) => {
  button.addEventListener("click", () => {
    aiQuestion.value = button.dataset.question;
    askAI(button.dataset.question);
  });
});
