# Advanced Programming Concepts

A collection of Python coursework, experiments, and projects developed while learning programming concepts and building practical applications.

## Main Python Mini Project

### [SkyWise OpenMeteo](13%20Python%20Mini%20Project/skywise-openmeteo/README.md)

SkyWise is my main Python mini project in this repository: a responsive weather dashboard built with **Python and Flask**. It retrieves current conditions and five-day forecasts from **Open-Meteo**, and includes an AI weather-advice panel.

**Highlights**
- Search for a city and view current weather conditions
- Check a five-day forecast
- Ask weather-related questions through the configurable AI panel
- Run locally or deploy using the included Render configuration

**Technologies:** Python, Flask, Open-Meteo, HTML, CSS, JavaScript, Ollama

For requirements, setup instructions, and deployment steps, see the [SkyWise project README](13%20Python%20Mini%20Project/skywise-openmeteo/README.md).

## Repository Contents

The folders in this repository contain Python experiments, coursework programs, and mini projects organized by topic. SkyWise is the featured main mini project.

## Run SkyWise

Open the project folder `13 Python Mini Project/skywise-openmeteo` in VS Code, then follow the detailed setup in its README. The basic commands on Windows are:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe app.py
```

The app starts at http://127.0.0.1:5001. Weather search and forecasts do not require an API key. The AI advice setup and deployment options are documented in the project README.
