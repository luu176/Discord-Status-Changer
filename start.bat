@echo off
setlocal

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed.
    echo Need to install python first. Make sure to add it to the PATH.
    echo Download Python from: https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe
    exit /b 1
)

REM Check if pip is available (pip comes bundled with Python, but just in case)
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed or not added to PATH.
    exit /b 1
)

REM Check if module is installed
python -c "import requests" 2>nul
if %errorlevel% neq 0 (
    echo 'requests' module not found, installing...
    pip install requests
)

python -c "import colorama" 2>nul
if %errorlevel% neq 0 (
    echo 'colorama' module not found, installing...
    pip install colorama
)

REM Run main.py
python main.py
endlocal
