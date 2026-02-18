# Quick start script for Slot Machine Game (PowerShell)
# Run this with: powershell -ExecutionPolicy Bypass -File start.ps1

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  SLOT MACHINE GAME - Starting...     " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
$pythonCheck = python --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Python found: $pythonCheck" -ForegroundColor Green
Write-Host ""

# Check if backend folder exists
if (-not (Test-Path "backend")) {
    Write-Host "ERROR: Backend folder not found!" -ForegroundColor Red
    exit 1
}

# Install dependencies if needed
Write-Host "Checking dependencies..." -ForegroundColor Yellow
$requirements = @("flask", "flask-cors")
foreach ($package in $requirements) {
    $installed = pip show $package 2>&1 | Select-String "Name"
    if (-not $installed) {
        Write-Host "Installing $package..." -ForegroundColor Yellow
        pip install $package | Out-Null
    }
}

Write-Host ""
Write-Host "✅ All dependencies ready!" -ForegroundColor Green
Write-Host ""

# Generate images if Pillow is available
$pillow = pip show pillow 2>&1 | Select-String "Name"
if (-not $pillow) {
    Write-Host "Installing Pillow for image generation..." -ForegroundColor Yellow
    pip install Pillow | Out-Null
}

# Try to generate images and sounds
if (Test-Path "generate_images.py") {
    Write-Host "Generating symbol images..." -ForegroundColor Yellow
    python generate_images.py 2>&1 | Out-Null
}

if (Test-Path "generate_sounds.py") {
    Write-Host "Generating audio files..." -ForegroundColor Yellow
    python generate_sounds.py 2>&1 | Out-Null
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  STARTING GAME SERVER...              " -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "🎰 Your slot machine game is starting!" -ForegroundColor Green
Write-Host ""
Write-Host "📍 Open your browser and go to:" -ForegroundColor Cyan
Write-Host "   http://localhost:5000" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press CTRL+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Run the Flask app
cd backend
python app.py
