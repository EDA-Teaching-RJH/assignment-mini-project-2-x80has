import csv
import re
# ingredient class: this represents an ingredient with its name, quantity, and unit of measurement
class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name  #sets the name of the ingredient
        self.quantity = quantity  # sets the quantity of the ingredient
        self.unit = unit  # sets the unit of the ingredient
    #this will output a formatted niceeee looking string
    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.name}"  #output example: "2.0 cups of Flour"
    def __repr__(self):
        return self.__str__()

# recipe class: this will be the class for the recipes, this includes titlw, description and ingredients
class Recipe:
    def __init__(self, title, description, ingredients):
        self.title = title  #title of the recipe
        self.description = description  # a description of the recipes
        self.ingredients = ingredients  #ingredients used in the recipe
    #formatting for recipes
    def __str__(self):
        ingredient_list = "\n".join(str(ingredient) for ingredient in self.ingredients)  #lists all ingredients
        return f"Recipe: {self.title}\nDescription: {self.description}\nIngredients:\n{ingredient_list}"
    def __repr__(self):
        return self.__str__()

# function reads csv file and returns the recipes
def read_recipes_from_csv(filename):
    recipes = []  #creates an empty list to store recipes
    with open(filename, mode='r') as file:  #opens csv file
        reader = csv.reader(file)  #reads the CSV file
        for row in reader:  #go through each row which is a different recipe
            title, description, ingredients_str = row[0], row[1], row[2]  # gets the title etc
            ingredients = parse_ingredients(ingredients_str)  #to make ingredient string into object
            recipes.append(Recipe(title, description, ingredients))  #make a new recipe and add it
    return recipes  #returns recipe object

#funtion to parse ingredient string to ingredient object
def parse_ingredients(ingredients_str):
    ingredients = []  #creates an empty list to hold the ingredient objects
    ingredients_list = ingredients_str.split(";")  #separate the ingredients string by semicolons
    for ingredient_str in ingredients_list:  #go through each ingredient
        match = re.match(r"(\d+\.?\d*)\s*(\w+)\s+of\s+(.+)", ingredient_str.strip())  #match and extract quantity, unit, and name
        if match:
            quantity = float(match.group(1))  #converts the quantity to a float
            unit = match.group(2)  #extract the unit of measurement
            name = match.group(3)  #extract the name of the ingredient
            ingredients.append(Ingredient(name, quantity, unit))  #creates an Ingredient object and add it to the list
    return ingredients  #Returns the list of Ingredient objects

#funtion to search by keyword
def search_recipes(recipes, keyword):
    search_results = []  #make an empty list to store the search results
    for recipe in recipes:  #go through all the recipes
        if re.search(keyword, recipe.title, re.IGNORECASE):  #search for the keyword in the recipe title (won't matter if capital or not)
            search_results.append(recipe)  #Ads the recipe to the search results if it matches
    return search_results  #shows list of recipes that match

# funtion to filter recipe by ingredient and mininimm quantity 
def filter_recipes_by_ingredient(recipes, ingredient_name, min_quantity):
    filtered_recipes = []  #makes empty list to store the filtered recipes
    for recipe in recipes:  # go through all the recipes
        for ingredient in recipe.ingredients:  #go through the ingredients of each recipe
            if ingredient_name.lower() in ingredient.name.lower():  #check if the ingredient name matches the filter
                if isinstance(ingredient.quantity, float) and ingredient.quantity >= min_quantity: #compare the quantity
                    filtered_recipes.append(recipe)  #a dd the recipe to the filtered list if it meets the criteria
                    break  # stop checking other ingredients when a match is found
    print("Filtered Recipes List:", filtered_recipes)  # print the filtered recipes list
    return filtered_recipes  #returns filteredrecipes

#function to print a list of recipes
def print_recipes(recipes):
    for recipe in recipes:  #go through each recipe
        print(recipe)  # prints the recipe details
        print("\n" + "-"*30 + "\n")  #separator to make it easier to read

# ths the main function to run the program
def main():
    recipes = read_recipes_from_csv('recipes.csv')  #read recipes from csv
    
    #this is to search recipes
    search_term = input("Enter a search term for recipes: ")  #asks the user for a search term
    search_results = search_recipes(recipes, search_term)  #Gget the search results
    print(f"\nSearch Results for '{search_term}':")
    print_recipes(search_results)  #print search result

    #this is to filter recipes
    ingredient_name = input("\nEnter ingredient name for filtering: ")  #ask the user for an ingredient name
    min_quantity = float(input(f"Enter minimum quantity for {ingredient_name}: "))  #ask for the minimum quantity
    filtered_results = filter_recipes_by_ingredient(recipes, ingredient_name, min_quantity)  #gets the filtered results
    
    if filtered_results:
        print(f"\nFiltered Recipes with '{ingredient_name}' (>= {min_quantity}):")
        print_recipes(filtered_results)  #print the filtered recipes
    else:
        print(f"No recipes match the filter criteria.")  #message when no matches in filter

if __name__ == "__main__":
    main()
