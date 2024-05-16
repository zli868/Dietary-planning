import json

import requests
import pandas as pd

def get_ingredient_str_lst(recipe):
    servings = recipe['servings']
    ingredient_str_lst = []
    ingredient_lst = []
    
    for ingredient in recipe['extendedIngredients']:
        measures = ingredient['measures']['metric']
        amount   = measures['amount']/servings
        unit     = measures['unitLong'].lower()
        name     = ingredient['name'].lower()
        
        ingredient_str = f"{amount:.3f} {unit} {name},"
        ingredient_str_lst.append(ingredient_str)
        ingredient_lst.append(name)
    
    return ingredient_str_lst, ingredient_lst

# call edamam API to get nutritional value of the recipe
def get_nutritional_value(ingredient_str_lst):
    # API endpoint
    url = "https://api.edamam.com/api/nutrition-details"

    # Request body
    request = {
        "title": "Your Recipe Title",
        "ingr": ingredient_str_lst,
        "url": '',
        "summary": "Recipe summary",
        "yield": "Recipe yield",
        "time": "Recipe time",
        "img": "Recipe image URL",
        "prep": "Recipe preparation"
    }

    # Make the API call
    response = requests.post(url, json=request, auth=('c5e34fbe', '7380c1dd9b76545e97016694badf3d73'))

    # Check if the request was successful (status code 200)
    # if response.status_code == 200:
    #     # Print the response JSON data
    #     print(response.json()['totalNutrients'])
    if response.status_code != 200:
        # Print an error message if the request failed
        print(f"Error: {response.status_code}, {response.text}")
        return None
    
    return response.json()

def main():
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
        if not response:
            # delete recipe from the dataframe
            recipe_basic_info_df = recipe_basic_info_df[recipe_basic_info_df['name'] != name]
            continue

        
        recipe_ingredient_str_lst[name] = ingredient_str_lst
        ingredients.update(ingredient_lst)


        # the response also contain other information like diet/health labels and emissions...
        nutritions = response['totalNutrients']
        
        recipe_nutritional_value[recipe['title']] = nutritions
        # for key in nutritions:
        #     print(key, nutritions[key]['label'], nutritions[key]['quantity'], nutritions[key]['unit'])
        
        # break
    
    # save set of ingredients to a txt file
    with open('data/ingredients.txt', 'w') as f:
        for item in ingredients:
            f.write("%s\n" % item)
    # save recipe_ingredient_str_lst to a json file
    with open('data/recipe_ingredient_str_lst.json', 'w') as f:
        json.dump(recipe_ingredient_str_lst, f)
    
    # 2. create a list of all unique nutritional values
    nutrition_units = {}
    for recipe, nutritions in recipe_nutritional_value.items():
        for key, value in nutritions.items():
            nutrition_name = value['label']
            if not nutrition_name in nutrition_units:
                nutrition_units[nutrition_name] = value['unit']
            else:
                assert nutrition_units[nutrition_name] == value['unit']
    
    print(nutrition_units)
    # save nutrition_units to a json file
    
    # 3. create a dataframe whose rows are recipes and columns are nutritional values
    recipe_nutritional_value_df = pd.DataFrame(columns= list(nutrition_units.keys()))
    
    for recipe, nutritions in recipe_nutritional_value.items():
        for key, value in nutritions.items():
            recipe_nutritional_value_df.loc[recipe, value['label']] = value['quantity']
    
    print(recipe_nutritional_value_df)
    
    # 4. save the dataframes to csv
    recipe_basic_info_df.to_csv('data/recipe_basic_info.csv', index=False)
    recipe_nutritional_value_df.to_csv('data/recipe_nutritional_value.csv')
    # save nutrition_units to a json file
    with open('data/nutrition_units.json', 'w') as f:
        json.dump(nutrition_units, f)
    

if __name__ == '__main__':
    main()