import json
import pandas as pd


def get_ingredient(recipe):
    servings = recipe['servings']
    ingredient_str_lst = []
    ingredient_lst = []
    
    for ingredient in recipe['extendedIngredients']:
        measures = ingredient['measures']['metric']
        amount   = measures['amount']/servings
        unit     = measures['unitLong'].lower()
        name     = ingredient['name'].lower()
        
        ingredient = (name, unit, round(amount, 3))
    
    return ingredient


# load recipe_basic_infor.csv
recipe_basic_info_df = pd.read_csv('data/recipe_basic_info.csv')

# load random_recipe_50_2024-05-15-01-16-18.json
# load the recipe data
with open('data/recipe/random_recipe_50_2024-05-15-01-16-18.json') as f:
    data = json.load(f)

# 1. get nutritional value of each recipe

recipe_basic_info_df = pd.DataFrame(columns=['name', 'cooking_time'])
recipe_nutritional_value = {}
ingredients = set()
recipe_ingredient_str_lst = {}
for recipe in data['recipes']:
    name = recipe['title']
    cooking_time = recipe['readyInMinutes']
    recipe_basic_info_df.loc[len(recipe_basic_info_df)] = [name, cooking_time]
    
    ingredient_str_lst, ingredient_lst = get_ingredient_str_lst(recipe)
    # print(ingredients_lst)
    response = get_nutritional_value(ingredient_str_lst)