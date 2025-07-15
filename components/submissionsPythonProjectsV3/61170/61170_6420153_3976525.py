import os
import csv # two files needed to be open to have my project spit out specific outputs 

# here files are being identified and opened inorder for code to execute
file_path = '61170_6420154_904213.csv'

if not os.path.isfile(file_path):
  with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)# writer row as in writing the recipes to the file same thing goes for reading a file
    writer.writerow(['food_name', 'ingredients'])
    
# introducing the project and whats expected 
print('Welcome to my Recipe Cookbook By Eeyonah McWhinnie\n')
print('In this project, the the recipe ingredients (for example, chicken, veggies, sauces, etc.). A constructed recipe is shown and the data is written to a file.')
print('I hope you enjoy the ineractive cookbook as well as the delisious recipes you get to add or delete, HAPPY EATING :) ')

#use def function to call load recipe to file 
def load_additional_recipe(): 

    recipe = {
      "tacos": ['oil', 'pepper', 'salt', 'meat(your choice)', 'lettuce'],
      "burger": ['burger buns', 'patty', 'salt', 'pepper', 'lettuce', 'tomato'],
      "fries": ['oil', 'potatoes', 'fries'],
      "pizza": ['dough', 'pizza sauce', 'cheese' , 'small pepperonis'],
      "strawberry icecream":['1 pound strawberried halved', '3/4 cup sugar',  '3/4 cup sugar', '3/4 teaspoon fresh lemon juice' ,'1/8 teaspoon salt', '2 cups horizon Heavy whipping cream'],
      "steak": ['steak', 'salt', 'pepper', 'butter', 'tyme', 'cooking oil'],
      "spagetti":['angle hair pasta noodles', 'spagetti sauce', 'meat or none meant', 'spices', 'bell peppers'],
      "avocado toast":['1 piece of rye bread', '1 half avocado', '2 tomato slices', '1 teaspoon seasalt', '1 teaspoon pepper'],
      "cheese cake": ['Crust' , '2 cups graham crumbs', '2 tablespoon sugar','cup butter melted', '24 ounces cream cheese softened', '1 cup sugar', '1 teaspoon vanilla', '3 eggs']
      
    } # here is the dict and function where recipe can be loaded
    
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                food_name, ingredients = row
                recipe[food_name] = ingredients.split(',')
            except ValueError:
                print(f"Skipping row: {row} - Invalid format") ## This line prints a message to the console, indicating that a particular row is being skipped due to an invalid format. 
                                                               # The {row} placeholder is replaced with the value of the 'row' variable.

    return recipe

#recipes will be saved to the CSV AND OS  here when put in from above ( in your load recipes) or through the output
def save_recipe(recipe):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['food_name', 'ingredients'])
        for food_name, ingredients in recipe.items():
            writer.writerow([food_name, ','.join(ingredients)])
            
recipe = load_additional_recipe()
print("\nOffered Recipes:\n", list(recipe.keys())) #recipe.keys makes the recipes into a organized list

while True:
    print("\nWELCOME TO MY COOKBOOK RECIPE MENU (1/2/3/4/5), Where your food dreams will come true just by following\nthe instructions below :)") # this half of the code is giving the user choices to pick from. 
    print("\n1. View available ingredients for a specific recipe")
    print("\n2. Add an additional recipe")
    print("\n3. Change a recipe you may have messed up on or do not like")
    print("\n4. Remove a specific recipe out of the list")
    print("\n5. Goodbye!!!")

    x = input("\nEnter your desired choice by picking numbers(1/2/3/4/5): ") # defining the varible and add input function to recive input from user 

    if x == '1':
        recipe_x = input("\nChoose your desired recipe from the list above: ")
        if recipe_x in recipe:
            print(f"These are the Ingredients for {recipe_x}:")
            for ingredient in recipe[recipe_x]:
                print(ingredient)
        else:
            print("Don't have that recipe")

    elif x == '2':
        diff_recipe = input("Please enter the name of a different recipe: ")
        diff_ingredients = input("Please enter ingredients (separate them with commas): ")
        recipe[diff_recipe] = diff_ingredients.split(',')
        print(f"{diff_recipe} recipe you chose was added successfully.")
        save_recipe(recipe)

    elif x == '3':
        recipe_x = input("Enter the name of a recipe you want to change or modify: ") 
        if recipe_x in recipe:                                                       
            diff_ingredients = input("Enter new ingredients here (separate them with commas): ")
            recipe[recipe_x] = diff_ingredients.split(',')
            print(f"Ingredients for {recipe_x} changed successfully.")
            save_recipe(recipe)
        else:
            print("Recipe that you entered  was not found. Try again please")

    elif x == '4':
        recipe_x = input("Enter the recipe that you'd like to delete from the menu: ")# delete recipe 
        if recipe_x in recipe:
            del recipe[recipe_x]
            print(f"{recipe_x} recipe entered deleted successfully.")
            save_recipe(recipe)
        else:
            print("Recipe chosen not found.")

    elif x == '5':
        print("Leaving Recipe Cookbook. Have a good one!")
        break # code breaks after User is done once they press '5'

    else:
        print("No available choice. Please choose a different option.")

