# What to Cook?

Cook with what you have, not with what you wish you had.

A smart culinary discovery platform based on the user's available ingredients, designed to reduce food waste, simplify meal decisions, and promote a more sustainable and ethical way of cooking.

## About the Project

What to Cook? helps users discover vegan recipes based on the ingredients they already have at home.

By entering available ingredients, the application suggests the best matching recipes from a curated vegan database, prioritizing those that require the fewest missing items.

Unlike traditional recipe platforms, this application starts from what the user already has — not what they need to buy.

## Core Philosophy

This project is built around three core principles:

- Sustainability → Reducing food waste through smarter ingredient usage  
- Ethical Cooking → Promoting a fully vegan recipe ecosystem  
- Simplicity → Helping users decide what to cook in seconds  

The platform is exclusively focused on vegan recipes, aligned with environmental awareness and the reduction of animal exploitation and suffering.

## Problem Statement

A common everyday situation:

"I have ingredients in my kitchen, but I don't know what to cook."

This uncertainty often leads to food waste, unnecessary grocery purchases, time-consuming recipe searches, and poor ingredient utilization.

What to Cook? solves this by reversing the traditional recipe search model.

## How It Works

1. User inputs available ingredients  
2. Ingredients are normalized by the system  
3. Vegan recipe database is searched  
4. Each recipe is scored based on ingredient compatibility  
5. Results are ranked from best match to lowest match  
6. User receives suggested recipes and missing ingredients  

## Matching Formula

Match Score = (Number of Matching Ingredients) / (Total Number of Required Ingredients)

Higher scores indicate better recipe compatibility.

## Features

- Vegan recipe-only database  
- Ingredient-based recipe search  
- Recipe ranking by compatibility score  
- Missing ingredient identification  
- Fast and minimal user experience  
- REST API built with FastAPI  
- Modern frontend built with React  
- Expandable recipe dataset  

## Example

User Input:
tofu, tomato, rice

Output:
1. Tofu Fried Rice
   Match: 100%
   Missing Ingredients: None

2. Tomato Tofu Stir Fry
   Match: 80%
   Missing Ingredients:
   - Soy Sauce

## Tech Stack

Backend:
- Python
- FastAPI
- Uvicorn

Frontend:
- React
- JavaScript
- HTML
- CSS

Data Storage:
Initial version:
- JSON-based recipe database

Future evolution:
- PostgreSQL
- SQLite

## Project Structure

what-to-cook/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── models/
│   │   └── data/
│   │
│   └── main.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│
├── recipes.json
│
└── README.md

## Future Improvements

- User accounts and personalization  
- Favorite recipes system  
- Advanced filtering (nutritional, dietary needs, preferences)  
- AI-powered recipe recommendations  
- Ingredient substitution engine  
- Grocery list generation  
- Meal planning system  
- Nutrition analysis  
- Recipe difficulty and cooking time estimation  
- Machine learning-based recommendation ranking  

## Learning Goals

This project was built as a practical full-stack software engineering portfolio project, focusing on:

- Backend development with FastAPI  
- Frontend development with React  
- REST API design principles  
- Data processing and ranking algorithms  
- Clean architecture and modular design  
- Real-world problem solving with production mindset  

## License

This project is licensed under the MIT License.
