import json
import time
import os

recipes = []

def load_recipes():
    global recipes
    try:
        with open('recipes.json', 'r') as f:
            recipes = json.load(f)
    except FileNotFoundError:
        recipes = []

def add_recipe():
    print("Add Recipe:")
    recipe_name = input("Enter the recipe name: ")
    recipe_ingredients = input("Enter the ingredients: ")
    recipe_instructions = input("Enter the instructions: ")
    recipe_servings = input("Enter how many servings: ")

    recipe = (recipe_name, recipe_ingredients, recipe_instructions, recipe_servings)
    recipes.append(recipe)
    return recipe

def view_recipe(recipe):
    if len(recipe) != 4:
        print("Invalid recipe format. Recipe must contain 4 items.")
        return None

    name, ingredients, instructions, servings = recipe

    print("--- Recipe Details ---")
    print(f"Recipe Name: {name}")
    print(f"Ingredients: {ingredients}")
    print(f"Instructions: {instructions}")
    print(f"Servings: {servings}")
    print("----------------------\n")

def view_all_recipes():
    if not recipes:
        print("No recipes available.")
        return

    for i, recipe in enumerate(recipes, start=1):
        print(f"\n----- Recipe {i} -----")
        view_recipe(recipe)

def search_recipes():
    print("Search Recipes:")

def save_and_exit():
    print("saving...")
    with open('recipes.json', 'w') as f:
        json.dump(recipes, f)
    time.sleep(2)
    print("exiting...")
    time.sleep(2)
    os._exit(0)

def menu():
    while True:
        print("CookBook Menu:")
        print("1. Add Recipe")
        print("2. View All Recipes")
        print("3. Search Recipes not implemented")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_recipe()
            elif choice == "2":
                view_all_recipes()
            elif choice == "3":
                search_recipes()
            elif choice == "4":
                save_and_exit()
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    load_recipes()
    menu()
