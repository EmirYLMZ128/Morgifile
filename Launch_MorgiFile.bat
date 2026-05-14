@echo off
color 0a
title MorgiFile Fully Launcher

echo ========================================
echo Starting MorgiFile Fully System...
echo ========================================

echo.
echo [1/3] Starting Python Backend (System Tray)...
cd /d "%~dp0App"
REM Check if common package is missing (using pystray as marker)
python -c "import pystray" 2>nul
if errorlevel 1 (
    echo Python dependencies missing. Installing...
    pip install -r requirements.txt
)
start "MorgiFile Backend" /b pythonw app.py

echo [2/3] Starting Vue Frontend Server...
cd /d "%~dp0App\Dashboard"
if not exist node_modules (
    echo node_modules not found. Installing dependencies...
    call npm install
)
start "MorgiFile Frontend" cmd /k "npm run dev"

echo.
echo [3/3] Waiting for servers to initialize...
timeout /t 4 /nobreak > nul

echo.
echo Launching Dashboard in default browser...
start http://localhost:5173

echo.
echo Done! You can close this launcher window now.
timeout /t 3 > nul
