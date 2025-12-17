@echo off
echo ========================================
echo  Crop Yield Prediction System
echo  Starting Application...
echo ========================================
echo.

echo Checking if packages are installed...
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo ERROR: Streamlit is not installed!
    echo Please run install.bat first.
    echo.
    pause
    exit /b 1
)

echo Starting Streamlit server...
echo.
echo The app will open in your browser automatically.
echo If not, open: http://localhost:8501
echo.
echo Press Ctrl+C to stop the server.
echo ========================================
echo.

streamlit run src/app.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to start the application!
    echo Please check the error messages above.
    pause
)
