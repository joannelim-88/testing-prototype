from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash')

@app.route('/api/analyze-recipe', methods=['POST'])
def analyze_recipe():
    try:
        data = request.get_json()
        ingredients = data.get('ingredients', [])
        
        # Validate and clean ingredients
        if not ingredients or not isinstance(ingredients, list):
            return jsonify({'error': 'No ingredients provided'}), 400
        
        # Clean and validate each ingredient
        cleaned_ingredients = []
        for ingredient in ingredients:
            if isinstance(ingredient, str) and ingredient.strip():
                # Clean the ingredient
                cleaned = ingredient.strip().lower()
                if cleaned and len(cleaned) > 0:
                    cleaned_ingredients.append(cleaned)
        
        if not cleaned_ingredients:
            return jsonify({'error': 'No valid ingredients provided'}), 400
        
        print(f"Processing ingredients: {cleaned_ingredients}")  # Debug log
        
        # Create prompt for Gemini
        ingredients_text = ', '.join(cleaned_ingredients)
        prompt = f"""
        Based on the following ingredients: {ingredients_text}
        
        Please suggest 2-3 recipe suggestions that can be made with these ingredients. 
        For each recipe, provide:
        1. Recipe name
        2. Brief description
        3. Ingredients needed (including the ones provided plus any additional ones)
        4. Step-by-step cooking instructions
        5. Estimated cooking time
        6. Difficulty level (Easy/Medium/Hard)
        
        Format the response as a JSON object with the following structure:
        {{
            "recipes": [
                {{
                    "name": "Recipe Name",
                    "description": "Brief description",
                    "ingredients": ["ingredient1", "ingredient2", ...],
                    "instructions": ["step1", "step2", ...],
                    "cooking_time": "X minutes",
                    "difficulty": "Easy/Medium/Hard"
                }}
            ]
        }}
        
        Make sure the recipes are practical and delicious. If the ingredients are limited, suggest simple recipes or mention what additional ingredients would make the recipe even better.
        """
        
        # Generate response using Gemini
        response = model.generate_content(prompt)
        
        # Parse the response to extract JSON
        response_text = response.text
        
        # Try to extract JSON from the response
        try:
            # Find JSON in the response
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1
            json_str = response_text[start_idx:end_idx]
            recipes_data = json.loads(json_str)
            
            return jsonify(recipes_data)
            
        except (json.JSONDecodeError, ValueError):
            # If JSON parsing fails, return a structured response
            return jsonify({
                'recipes': [{
                    'name': 'Recipe Suggestion',
                    'description': 'Based on your ingredients, here are some recipe suggestions:',
                    'ingredients': cleaned_ingredients,
                    'instructions': [response_text],
                    'cooking_time': 'Varies',
                    'difficulty': 'Medium'
                }]
            })
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'message': 'Recipe Analyzer API is running'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 