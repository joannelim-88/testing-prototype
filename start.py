#!/usr/bin/env python3
"""
Smart Recipe Analyzer - Startup Script
This script helps you start the Flask backend and provides instructions for the React frontend.
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed."""
    print("🔍 Checking dependencies...")
    
    # Check Python dependencies
    try:
        import flask
        import flask_cors
        import google.generativeai
        print("✅ Python dependencies are installed")
    except ImportError as e:
        print(f"❌ Missing Python dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False
    
    return True

def check_env_file():
    """Check if .env file exists and has the API key."""
    env_file = Path('.env')
    
    if not env_file.exists():
        print("❌ .env file not found!")
        print("Please create a .env file with your Gemini API key:")
        print("GEMINI_API_KEY=your_api_key_here")
        return False
    
    # Check if API key is set
    with open(env_file, 'r') as f:
        content = f.read()
        if 'GEMINI_API_KEY=your_gemini_api_key_here' in content or 'GEMINI_API_KEY=' not in content:
            print("❌ Please set your Gemini API key in the .env file")
            return False
    
    print("✅ Environment file is configured")
    return True

def start_backend():
    """Start the Flask backend server."""
    print("\n🚀 Starting Flask backend server...")
    print("Backend will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "app.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Backend server stopped")
    except Exception as e:
        print(f"❌ Error starting backend: {e}")

def main():
    """Main function to start the application."""
    print("🍳 Smart Recipe Analyzer - Startup Script")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check environment file
    if not check_env_file():
        sys.exit(1)
    
    print("\n📋 Next Steps:")
    print("1. This script will start the Flask backend")
    print("2. Open a new terminal and run: npm install")
    print("3. Then run: npm start")
    print("4. Open http://localhost:3000 in your browser")
    print("\n" + "=" * 50)
    
    # Ask user if they want to start the backend
    response = input("Do you want to start the Flask backend now? (y/n): ").lower().strip()
    
    if response in ['y', 'yes']:
        start_backend()
    else:
        print("To start the backend manually, run: python app.py")

if __name__ == "__main__":
    main() 