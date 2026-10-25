# Advanced Programming Concepts

A collection of Python coursework, experiments, and projects organized by topic. This repository documents my learning and includes practical programs and applications.

## Contents

- [Featured Mini Project](#featured-mini-project)
- [Project Features](#project-features)
- [Folder Structure](#folder-structure)
- [Run the Project](#run-the-project)
- [Documentation](#documentation)

## Featured Mini Project

### [SkyWise OpenMeteo](13%20Python%20Mini%20Project/skywise-openmeteo/README.md)

**SkyWise is my main Python mini project.** It is a responsive weather dashboard built with Python and Flask. It uses Open-Meteo for current weather and forecast data, and provides an optional AI weather-advice feature.

| Details | Information |
| --- | --- |
| Project type | Python mini project |
| Main technologies | Python, Flask, HTML, CSS, JavaScript |
| Weather data | Open-Meteo |
| AI advice | Ollama or another configured provider |
| Project folder | `13 Python Mini Project/skywise-openmeteo` |

## Project Features

- Search for a city and view its current weather
- View a five-day forecast
- Ask weather-related questions using the configured AI provider
- Run locally or deploy using the included Render configuration

## Folder Structure

```text
13 Python Mini Project/
└── skywise-openmeteo/
    ├── app.py
    ├── requirements.txt
    ├── templates/
    ├── static/
    └── README.md
```

## Run the Project

Open `13 Python Mini Project/skywise-openmeteo` in VS Code. In the terminal, run:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe app.py
```

Then open [http://127.0.0.1:5001](http://127.0.0.1:5001) in your browser. Weather search and forecasts do not require an API key.

## Documentation

See the [SkyWise project README](13%20Python%20Mini%20Project/skywise-openmeteo/README.md) for complete requirements, configuration, AI setup, and deployment instructions.
