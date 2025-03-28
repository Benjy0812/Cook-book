import json
import time
import sys
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
            print(
                "\nOne or more fields are empty. Recipe was not added, please try again.\n"
            )
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
    clear_console()
    search_term = input("Enter the recipe name to search: ").lower()
    found_recipes = [recipe for recipe in recipes if search_term in recipe[0].lower()]

    if not found_recipes:
        print("\nNo recipes found with that name.\n")
    else:
        for i, recipe in enumerate(found_recipes, start=1):
            print(f"\n----- Recipe {i} -----")
            view_recipe(recipe)

    input("Press enter to continue.")
    clear_console()


def save_and_exit():
    clear_console()
    print("saving...")
    with open("recipes.json", "w") as f:
        json.dump(recipes, f)
    time.sleep(2)
    print("exiting...")
    time.sleep(2)
    sys.exit


def exit():
    print("Exiting...")
    time.sleep(2)
    sys.exit


def menu():
    while True:
        try:
            print("CookBook Menu:")
            print("1. Add Recipe.")
            print("2. View All Recipes.")
            print("3. Search Recipes.")
            print("4. Save and Exit.")
            print("5. Exit.\n")

            choice = int(input("Enter your choice: "))

            if choice not in range(1, 6):
                print("Invalid choice. Please try again.")
                print("choice must be between 1 and 5\n")
                continue
            elif choice == 1:
                clear_console()
                add_recipe()
            elif choice == 2:
                clear_console()
                view_all_recipes()
            elif choice == 3:
                clear_console()
                search_recipes()
            elif choice == 4:
                clear_console()
                save_and_exit()
            elif choice == 5:
                clear_console()
                print("Exiting CookBook. Goodbye!")
                break
        except ValueError:
            clear_console()
            print("Invalid input. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    load_recipes()
    menu()
