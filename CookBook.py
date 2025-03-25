import json
import time
import os

def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

recipes = []


def load_recipes():
    global recipes
    try:
        with open("recipes.json", "r") as f:
            recipes = json.load(f)
    except FileNotFoundError:
        recipes = []



def add_recipe():
    while True:
        print("Add Recipe:")
        name = input("Enter the recipe name: ")
        ingredients = input("Enter the ingredients: ")
        instructions = input("Enter the instructions: ")
        servings = input("Enter how many servings: ")

        if not all([name, ingredients, instructions, servings]):
            print("\nOne or more fields are empty. Recipe was not added, please try again.\n")
            continue
        else:
            clear_console()
            recipe = (name, ingredients, instructions, servings)
            recipes.append(recipe)
            print("\nRecipe added successfully!\n")
            return recipe


def view_recipe(recipe):

    name, ingredients, instructions, servings = recipe

    print("--- Recipe Details ---")
    print(f"Recipe Name: {name}")
    print(f"Ingredients: {ingredients}")
    print(f"Instructions: {instructions}")
    print(f"Servings: {servings}")
    print("----------------------")


def view_all_recipes():
    if not recipes:
        clear_console()
        print("\nNo recipes available.\n")
        return

    for i, recipe in enumerate(recipes, start=1):
        print(f"\n----- Recipe {i} -----")
        view_recipe(recipe)
    
    input("Press enter to continue.")
    clear_console()


def search_recipes():
    print("Search Recipes:")
    print("Not added yet wont work.")


def save_and_exit():
    clear_console()
    print("saving...")
    with open("recipes.json", "w") as f:
        json.dump(recipes, f)
    time.sleep(2)
    print("exiting...")
    time.sleep(2)
    os._exit(0)


def menu():
    while True:
        print("CookBook Menu:")
        print("1. Add Recipe.")
        print("2. View All Recipes.")
        print("3. Search Recipes not implemented yet.")
        print("4. Save and Exit.\n")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                clear_console()
                add_recipe()
            elif choice == "2":
                clear_console()
                view_all_recipes()
            elif choice == "3":
                search_recipes()
            elif choice == "4":
                clear_console()
                save_and_exit()
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    load_recipes()
    menu()
