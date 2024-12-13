import pytest
from recipe_manager import Recipe, Ingredient, search_recipes, filter_recipes_by_ingredient
#mock data for testing
test_ingredients = [
    Ingredient("Flour", 2.0, "cups"), #ingredient: flour with 2 cups
    Ingredient("Sugar", 1.0, "cup"),  # ingredient: sugar with 1 cup
    Ingredient("Salt", 1.0, "tsp")#ingredient: salt with 1 tsp
]
test_recipe = Recipe("Chocolate Cake", "A simple chocolate cake.", test_ingredients) #recipe: chocolate cake
test_recipe2 = Recipe("Vanilla Cake", "A classic vanilla cake.", test_ingredients)  #recipe: vanilla cake

testing_recipes = [test_recipe, test_recipe2]  #list containing both recipes

#test case for the search_recipes function
def test_search_recipes():
    #test searching for chocolate
    result = search_recipes(testing_recipes, "Chocolate")
    assert len(result) == 1  #should return one recipe
    assert result[0].title == "Chocolate Cake"  #check if the correct recipe is returned

    #test searching for vanilla
    result = search_recipes(testing_recipes, "Vanilla")
    assert len(result) == 1  # should return one recipe
    assert result[0].title == "Vanilla Cake"#check if the correct recipe is returned

    #test searching for cake
    result = search_recipes(testing_recipes, "Cake")
    assert len(result) == 2  #both recipes should be returned since cake is in both titles

# test case for the filter_recipes_by_ingredient function
def test_filter_recipes_by_ingredient():
    #test filtering recipes with sugar where quantity >= 1 cup
    result = filter_recipes_by_ingredient(testing_recipes, "Sugar", 1)
    assert len(result) == 2#both recipes should be returned since both contain sugar

    #test filtering recipes with sugar where quantity >= 2 cups
    result = filter_recipes_by_ingredient(testing_recipes, "Sugar", 2)
    assert len(result) == 0 #no recipe should be returned since none have 2 cups of sugar

#test case for wromg ingredient filtering
def test_filter_recipes_invalid_ingredient():
    #test filtering recipes with an ingredient that does not exist
    result = filter_recipes_by_ingredient(testing_recipes, "Chocolate", 1)
    assert len(result) == 0  #no recipe should be returned since chocolate is not an ingredient

# test case for minimum quantity filtering
def test_filter_recipes_minimum_quantity():
    #test filtering recipes with sugar where quantity >= 0.5 cup
    result = filter_recipes_by_ingredient(testing_recipes, "Sugar", 0.5)
    assert len(result) == 2  #both recipes should be returned since both meet the minimum quantity
