import requests

def find_recipes_by_ingredients(ingredients, number=5):
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual Spoonacular API key
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={','.join(ingredients)}&number={number}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        recipes = response.json()
        return recipes
    else:
        print("Error fetching recipes:", response.status_code)
        return None

def print_recipe_info(recipe):
    print("Title:", recipe['title'])
    print("Ingredients:")
    for ingredient in recipe['usedIngredients']:
        print("-", ingredient['original'])
    for ingredient in recipe['missedIngredients']:
        print("-", ingredient['original'])
    print("Instructions:", recipe['instructions'] or "Not available")
    print("\n")

if __name__ == "__main__":
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    number_of_recipes = int(input("Enter the number of recipes you want: "))
    recipes = find_recipes_by_ingredients(ingredients, number_of_recipes)
    if recipes:
        print(f"Here are {len(recipes)} recipes:")
        for recipe in recipes:
            print_recipe_info(recipe)
    else:
        print("No recipes found.")
