@echo off
REM Quick setup script for Slot Machine Game
REM This script sets up everything you need to run the game

echo.
echo ========================================
echo   SLOT MACHINE GAME - Quick Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

echo [1/4] Installing Python dependencies...
cd backend
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
cd ..

echo.
echo [2/4] Generating symbol images...
python generate_images.py
if errorlevel 1 (
    echo WARNING: Could not generate images (PIL not installed)
    echo Trying to install Pillow...
    pip install Pillow
    python generate_images.py
)

echo.
echo [3/4] Generating audio files...
python generate_sounds.py
if errorlevel 1 (
    echo WARNING: Could not generate audio files
)

echo.
echo [4/4] Setup complete!
echo.
echo ========================================
echo   READY TO PLAY!
echo ========================================
echo.
echo To start the game:
echo   cd backend
echo   python app.py
echo.
echo Then open: http://localhost:5000
echo.
pause
