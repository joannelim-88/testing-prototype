@echo off
echo 🍳 Smart Recipe Analyzer - Windows Startup
echo ==========================================

echo.
echo 📋 Setup Instructions:
echo 1. Install Python dependencies: pip install -r requirements.txt
echo 2. Create .env file with your Gemini API key
echo 3. Install Node.js dependencies: npm install
echo 4. Start the application
echo.

echo 🚀 Starting Flask backend...
echo Backend will run on: http://localhost:5000
echo.
echo 📝 To start the React frontend in a new terminal:
echo    npm start
echo.
echo 🌐 Then open: http://localhost:3000
echo.

python app.py

pause 