# 🍳 Smart Recipe Analyzer

A modern web application that uses AI to suggest delicious recipes based on your available ingredients. Built with React frontend, Flask backend, and powered by Google's Gemini AI.

## ✨ Features

- **AI-Powered Recipe Suggestions**: Get 2-3 personalized recipe recommendations based on your ingredients
- **Modern UI/UX**: Beautiful, responsive design with smooth animations
- **Real-time Analysis**: Instant recipe suggestions using Gemini Flash 2.5
- **Detailed Recipe Information**: Complete ingredients list, step-by-step instructions, cooking time, and difficulty level
- **Mobile Responsive**: Works perfectly on all devices

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- Google Gemini API key

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd smart-recipe-analyzer
   ```

2. **Set up the Backend (Flask)**
   ```bash
   # Install Python dependencies
   pip install -r requirements.txt
   
   # Create environment file
   cp env_example.txt .env
   ```

3. **Configure API Keys**
   - Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Edit `.env` file and add your API key:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```

4. **Set up the Frontend (React)**
   ```bash
   # Install Node.js dependencies
   npm install
   ```

5. **Run the Application**

   **Terminal 1 - Start the Flask backend:**
   ```bash
   python app.py
   ```
   The backend will run on `http://localhost:5000`

   **Terminal 2 - Start the React frontend:**
   ```bash
   npm start
   ```
   The frontend will run on `http://localhost:3000`

6. **Open your browser**
   Navigate to `http://localhost:3000` to use the application!

## 🎯 How to Use

1. **Enter Ingredients**: Type your available ingredients separated by commas
   - Example: `chicken, rice, tomatoes, onions, garlic`

2. **Get Suggestions**: Click "Get Recipe Suggestions" to analyze your ingredients

3. **View Recipes**: Browse through the AI-generated recipe suggestions with:
   - Recipe name and description
   - Complete ingredients list
   - Step-by-step cooking instructions
   - Cooking time and difficulty level

## 🛠️ Technology Stack

### Backend
- **Flask**: Python web framework
- **Flask-CORS**: Cross-origin resource sharing
- **Google Generative AI**: Gemini Flash 2.5 model
- **python-dotenv**: Environment variable management

### Frontend
- **React**: JavaScript library for building user interfaces
- **Axios**: HTTP client for API calls
- **CSS3**: Modern styling with gradients and animations

## 📁 Project Structure

```
smart-recipe-analyzer/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── package.json          # Node.js dependencies
├── env_example.txt       # Environment variables template
├── README.md            # Project documentation
├── public/
│   └── index.html       # Main HTML file
└── src/
    ├── index.js         # React entry point
    ├── index.css        # Global styles
    ├── App.js          # Main React component
    └── App.css         # Component styles
```

## 🔧 API Endpoints

- `POST /api/analyze-recipe`: Analyze ingredients and return recipe suggestions
- `GET /api/health`: Health check endpoint

### Request Format
```json
{
  "ingredients": ["chicken", "rice", "tomatoes"]
}
```

### Response Format
```json
{
  "recipes": [
    {
      "name": "Recipe Name",
      "description": "Brief description",
      "ingredients": ["ingredient1", "ingredient2"],
      "instructions": ["step1", "step2"],
      "cooking_time": "30 minutes",
      "difficulty": "Easy"
    }
  ]
}
```

## 🎨 Features in Detail

### Smart Ingredient Processing
- Automatically cleans and formats ingredient input
- Handles various input formats (commas, spaces, etc.)
- Filters out empty entries

### AI-Powered Analysis
- Uses Gemini Flash 2.5 for intelligent recipe generation
- Considers ingredient compatibility and cooking methods
- Provides practical and delicious recipe suggestions

### Beautiful UI/UX
- Modern gradient background
- Smooth hover animations
- Responsive design for all screen sizes
- Loading states and error handling
- Color-coded difficulty badges

## 🔒 Security

- API keys are stored in environment variables
- CORS enabled for secure cross-origin requests
- Input validation and sanitization

## 🚀 Deployment

### Backend Deployment
1. Set up a Python environment on your server
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables
4. Run with: `python app.py`

### Frontend Deployment
1. Build the React app: `npm run build`
2. Serve the `build` folder with a web server
3. Configure proxy settings for API calls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.
