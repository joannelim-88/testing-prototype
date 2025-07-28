import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [ingredients, setIngredients] = useState('');
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [parsedIngredients, setParsedIngredients] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!ingredients.trim()) {
      setError('Please enter at least one ingredient');
      return;
    }

    setLoading(true);
    setError('');
    setRecipes([]);

    try {
      // Improved ingredient parsing - handle multiple separators and formats
      const ingredientsList = ingredients
        .split(/[,;]/) // Split by comma or semicolon
        .map(ingredient => ingredient.trim())
        .filter(ingredient => ingredient.length > 0)
        .map(ingredient => {
          // Remove common prefixes and clean up
          return ingredient
            .replace(/^(and|or|with|plus)\s+/i, '') // Remove common prefixes
            .replace(/\s+/g, ' ') // Normalize whitespace
            .trim();
        })
        .filter(ingredient => ingredient.length > 0); // Filter again after cleaning

      console.log('Parsed ingredients:', ingredientsList); // Debug log

      if (ingredientsList.length === 0) {
        setError('Please enter valid ingredients separated by commas or semicolons');
        setLoading(false);
        return;
      }

      // Show user what ingredients were parsed
      console.log(`Processing ${ingredientsList.length} ingredients: ${ingredientsList.join(', ')}`);
      setParsedIngredients(ingredientsList);

      const response = await axios.post('/api/analyze-recipe', {
        ingredients: ingredientsList
      });

      setRecipes(response.data.recipes || []);
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to analyze ingredients. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const getDifficultyColor = (difficulty) => {
    switch (difficulty?.toLowerCase()) {
      case 'easy':
        return '#28a745';
      case 'medium':
        return '#ffc107';
      case 'hard':
        return '#dc3545';
      default:
        return '#6c757d';
    }
  };

  return (
    <div className="App">
      <div className="container">
        <header className="header">
          <h1>🍳 Smart Recipe Analyzer</h1>
          <p>Enter your ingredients and get delicious recipe suggestions powered by AI</p>
        </header>

        <div className="card">
          <form onSubmit={handleSubmit}>
            <div className="input-group">
              <label htmlFor="ingredients">What ingredients do you have?</label>
              <input
                type="text"
                id="ingredients"
                value={ingredients}
                onChange={(e) => setIngredients(e.target.value)}
                placeholder="e.g., chicken, rice, tomatoes, onions"
                disabled={loading}
              />
              <small>Separate ingredients with commas or semicolons (e.g., chicken, rice; tomatoes, onions)</small>
            </div>
            
            <button 
              type="submit" 
              className="btn btn-primary"
              disabled={loading}
            >
              {loading ? 'Analyzing...' : 'Get Recipe Suggestions'}
            </button>
          </form>
        </div>

        {error && (
          <div className="error">
            {error}
          </div>
        )}

        {parsedIngredients.length > 0 && !loading && (
          <div className="card parsed-ingredients">
            <h4>📋 Parsed Ingredients:</h4>
            <div className="ingredients-tags">
              {parsedIngredients.map((ingredient, idx) => (
                <span key={idx} className="ingredient-tag">
                  {ingredient}
                </span>
              ))}
            </div>
          </div>
        )}

        {loading && (
          <div className="loading">
            <div className="spinner"></div>
            <p>AI is analyzing your ingredients and finding the perfect recipes...</p>
          </div>
        )}

        {recipes.length > 0 && (
          <div className="recipes-section">
            <h2>🍽️ Recipe Suggestions</h2>
            {recipes.map((recipe, index) => (
              <div key={index} className="card recipe-card">
                <div className="recipe-header">
                  <h3>{recipe.name}</h3>
                  <span 
                    className="difficulty-badge"
                    style={{ backgroundColor: getDifficultyColor(recipe.difficulty) }}
                  >
                    {recipe.difficulty}
                  </span>
                </div>
                
                <p className="recipe-description">{recipe.description}</p>
                
                <div className="recipe-meta">
                  <span className="cooking-time">⏱️ {recipe.cooking_time}</span>
                </div>

                <div className="recipe-section">
                  <h4>📝 Ingredients:</h4>
                  <ul className="ingredients-list">
                    {recipe.ingredients.map((ingredient, idx) => (
                      <li key={idx}>{ingredient}</li>
                    ))}
                  </ul>
                </div>

                <div className="recipe-section">
                  <h4>👨‍🍳 Instructions:</h4>
                  <ol className="instructions-list">
                    {recipe.instructions.map((instruction, idx) => (
                      <li key={idx}>{instruction}</li>
                    ))}
                  </ol>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App; 