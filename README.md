# Advanced Programming Concepts

A collection of Python coursework, programming experiments, and mini projects. The repository is organized around practice in core Python, text processing, file handling, and small application projects.

## Main Python Mini Project

### [SkyWise OpenMeteo](13%20Python%20Mini%20Project/skywise-openmeteo/README.md)

**SkyWise OpenMeteo is my main Python mini project.** It is a Flask weather dashboard that uses Open-Meteo for current conditions and forecasts, with an optional AI weather-advice feature.

| Project detail | Description |
| --- | --- |
| Category | Python mini project |
| Main technologies | Python, Flask, HTML, CSS, JavaScript |
| Weather and forecast data | Open-Meteo |
| AI advice | Ollama or another configured provider |
| Source folder | [13 Python Mini Project/skywise-openmeteo](13%20Python%20Mini%20Project/skywise-openmeteo) |

### Features

- Search for a city and view current weather conditions
- View a five-day forecast
- Ask weather-related questions using the configured AI provider
- Run locally or deploy with the included Render configuration

### Run SkyWise on Windows

Open `13 Python Mini Project/skywise-openmeteo` in VS Code. In the terminal, run:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe app.py
```

Open [http://127.0.0.1:5001](http://127.0.0.1:5001) in your browser. Weather search and forecasts do not require an API key. See the [SkyWise README](13%20Python%20Mini%20Project/skywise-openmeteo/README.md) for full setup, AI configuration, and deployment instructions.

## Repository Guide

The repository contains individual Python programs at the top level and folders that group related exercises or projects.

### Core Python and programming exercises

These folders contain practice programs for common programming concepts and problem solving:

- [Calculator](Calculator/)
- [Character Types](Character%20Types/)
- [Number Utils](Number%20Utils/)
- [Recursive Utils](Recursive%20Utils/)
- [String Utils](String%20Utils/)
- [Vowels_Consonants](Vowels_Consonants/)

Examples of individual exercises include factorial, Fibonacci, prime checking, even and odd numbers, powers, patterns, data types, and 2D plane points.

### Strings and text processing

These exercises cover character and word operations, validation, and text transformations:

- [Longest Word](Longest%20Word/)
- [Remove Comments](Remove%20Comments/)
- [Search Word](Search%20Word/)
- [Word Frequency](Word%20Frequency/)
- [text_project](text_project/)
- [texttools project1](texttools%20project1/)

Top-level examples include anagram checks, character counts and frequencies, palindrome checks, Caesar cipher, email and password validation, hashtag and phone number extraction, stopword removal, and duplicate-character removal.

### File handling

These folders contain exercises for reading, comparing, searching, merging, and editing files:

- [Comparing Files](Comparing%20Files/)
- [Convert File Uppercase](Convert%20File%20Uppercase/)
- [Count File](Count%20File/)
- [File Characters](File%20Characters/)
- [File Contents](File%20Contents/)
- [File Words](File%20Words/)
- [Find & Replace in File](Find%20%26%20Replace%20in%20File/)
- [Merging Files](Merging%20Files/)
- [Read File](Read%20File/)
- [Replace Word](Replace%20Word/)
- [Reverse Lines](Reverse%20Lines/)

Related top-level programs include extracting file extensions and counting them, extracting dates into a uniform format, and counting occurrences of a word.

### Student, employee, and record exercises

These folders group record-based and student or employee practice programs:

- [Employee Info](Employee%20Info/)
- [Salary](Salary/)
- [Student](Student/)
- [Student File](Student%20File/)
- [Student Info](Student%20Info/)
- [Student Project1](Student%20Project1/)
- [Exception Handling-Student Info](Exception%20Handling-Student%20Info/)

Other related programs include employee records, attendance, and inventory management with dictionaries.

### Application and mini project folders

These folders contain larger practice projects and application work:

- [Banking Project1](Banking%20Project1/)
- [banking_project](banking_project/)
- [college_project](college_project/)
- [college_project1](college_project1/)
- [ecommerce](ecommerce/)
- [ecommerce1](ecommerce1/)
- [library](library/)
- [library_app](library_app/)
- [math_project](math_project/)
- [mathutils1](mathutils1/)
- [medical](medical/)
- [medical_project](medical_project/)
- [recursion_project](recursion_project/)
- [student_project](student_project/)
- [Main Python mini project: SkyWise OpenMeteo](13%20Python%20Mini%20Project/skywise-openmeteo/README.md)

## Individual Python Experiments

Standalone `.py` files in the repository root provide additional practice in:

- **Numbers and logic:** factorial, Fibonacci, prime numbers, digit sums, even and odd numbers, and powers of two
- **Strings:** anagrams, palindromes, character frequency, duplicate characters, and text cleanup
- **Collections:** sets, dictionaries, and inventory tracking
- **Files and data extraction:** file extension counts, dates, hashtags, phone numbers, and word occurrences
- **Validation:** email addresses and password strength
- **Patterns:** character sequences and pattern printing

Browse the [repository files](.) to see the complete set of programs.

## Folder Structure

```text
Advanced Programming Concepts/
├── 13 Python Mini Project/
│   └── skywise-openmeteo/
│       ├── app.py
│       ├── requirements.txt
│       ├── templates/
│       ├── static/
│       └── README.md
├── topic and exercise folders/
└── individual Python experiment files
```
