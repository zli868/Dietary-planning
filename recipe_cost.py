import json
import pandas as pd

from ingredient_prices import ingredient_prices

# Define ingredient costs

weights = {
    'avocado': 200,  # grams per avocado
    'bananas': 120,  # grams per medium banana
    'banana': 120,  # grams per medium banana
    'apple': 182,  # grams per medium apple
    'pearl onions': 10,  # grams per onion
    'bay leaf': 0.2,  # grams per leaf
    'beijing cabbage': 900,  # grams per head
    'bell pepper': 150,  # grams per medium bell pepper
    'cayenne pepper': 0.5,  # grams per teaspoon
    'carrot': 61,  # grams per carrot
    'cherry tomatoes': 15,  # grams per cherry tomato
    'chicken': 500,  # grams per serving (average)
    'chicken breasts': 150,  # grams per breast
    'chili': 2,  # grams per chili
    'chilies': 2,  # grams per chili
    'chocolate-hazelnut pirouette cookies': 10,  # grams per cookie
    'cucumbers': 300,  # grams per cucumber
    'dates': 7,  # grams per date
    'daikon radish': 462,  # grams per radish
    'drop natural food coloring': 0.05,  # grams per drop
    'ear of corn': 100,  # grams per ear
    'egg': 50,  # grams per large egg
    'egg yolks': 17,  # grams per yolk
    'eggs': 50,  # grams per large egg
    'garlic clove': 5,  # grams per clove
    'garlic cloves': 5,  # grams per clove
    'gloves garlic': 5,  # grams per clove
    'green onions': 15,  # grams per green onion
    'jalapeno chile peppers': 14,  # grams per pepper
    'jalapeño peppers': 14,  # grams per pepper
    'juice of lemon': 30,  # grams per lemon
    'juice of lime': 30,  # grams per lime
    'leek': 89,  # grams per leek
    'lemon verbena leaves': 0.1,  # grams per leaf
    'lemon zest': 6,  # grams per lemon
    'lentils': 192,  # grams per cup (cooked)
    'lime': 67,  # grams per lime
    'onion': 150,  # grams per medium onion
    'peppers': 150,  # grams per medium pepper
    'popsicle moulds': 0,  # no weight as it's a container
    'swiss chard leaves': 0,
    'zucchini': 124,
    'overripe bananas': 120,  # grams per medium banana
    'overripe banana': 120,  # grams per medium banana
    'granny smith apples': 182,  # grams per medium apple
    'bouquet garnic': 0.2,  # grams per leaf
    'corn on the cob': 100,  # grams per ear
    'tomato': 182,  # grams per medium tomato
    'green onion': 15,  # grams per green onion
    'pepper': 0.5,  # grams per teaspoon
}

# Function to convert ingredient quantity to cost
def get_ingredient_cost(ingredient, quantity, unit):
    cost_per_unit = ingredient_prices.get(ingredient, 0)
    if ingredient not in ingredient_prices:
        padding = 15 - len(ingredient)
        print(f"Warning: No COST found for ingredient '{ingredient}', {' ' * padding} unit '{unit}'")
        return 0 
    
    if unit in ['g', 'ml', 'milliliters', 'grams', 'pinch']:
        pass
    elif unit == 'can':
        quantity *= 400  # ml per can
    elif unit in ['tsp', 'tsps', 'teaspoon', 'teaspoons']:
        quantity *= 4.92892  # tsp to ml
    elif unit in ['tbsp', 'tb', 'tbs', 'tbsps']:
        quantity *= 14.7868  # tbsp to ml
    elif unit == 'cup':
        quantity *= 240  # cup to ml
    elif unit in ['oz', 'ounces', 'serving', 'servings', 'fl. oz.s']:
        quantity *= 29.5735  # oz to ml
    elif unit in ['lb', 'pints']:
        quantity *= 453.592  # lb to grams
    
    elif unit in [None, '', 'large', 'larges', 'medium', 'mediums', 'small', 'smalls']:
        if ingredient in weights:
            quantity *= weights.get(ingredient, 0)
        else:
            padding = 15 - len(ingredient)
            print(f"Warning: No UNIT found for ingredient '{ingredient}', {' ' * padding} unit '{unit}'")

    
    return cost_per_unit * quantity

# Function to estimate recipe cost
def estimate_recipe_cost(recipe_ingredients):
    total_cost = 0

    for item in recipe_ingredients:
        name, quantity, unit = item
        total_cost += get_ingredient_cost(name, quantity, unit)
    return round(total_cost, 2)

# Estimate cost for each recipe
recipe_costs = {}

# load recipe_basic_infor.csv
recipe_basic_info_df = pd.read_csv('data/recipe_basic_info.csv')

# load ingredient_mapping.json
ingredient_mapping = json.load(open('data/ingredient_mapping.json'))

recipes = json.load(open('data/recipe/random_recipe_50_2024-05-15-01-16-18.json'))

# create dataframe for recipe ingredients
recipe_ingredients_df = pd.DataFrame(columns=['name', 'quantity', 'unit'])

all_ingredient_names = set()
for recipe in recipes['recipes']:
    recipe_name = recipe['title']
    if not recipe_name in recipe_basic_info_df['name'].values:
        continue
    ingredients = recipe['extendedIngredients']
    recipe_ingredients = []
    for ingredient in ingredients:
        quantity = ingredient['measures']['metric']['amount']
        unit = ingredient['measures']['metric']['unitLong'].lower()
        name = ingredient['name'].lower()
        mapped_name = ingredient_mapping.get(name, None)
        if not mapped_name:
            print(f"Warning: No MAPPING found for ingredient '{name}'")
            continue
        recipe_ingredients.append((mapped_name, quantity, unit))
        recipe_ingredients_df.loc[len(recipe_ingredients_df)] = [ingredient_mapping[mapped_name], quantity, unit]
        all_ingredient_names.add(mapped_name)
    
    cost = estimate_recipe_cost(recipe_ingredients)
    recipe_costs[recipe_name] = cost

# sort recipe_ingredients_df by name
recipe_ingredients_df = recipe_ingredients_df.sort_values(by='name')
# save recipe_ingredients_df to csv
recipe_ingredients_df.to_csv('data/recipe_ingredients.csv', index=False)

print(recipe_ingredients_df)

all_units = set(recipe_ingredients_df['unit'].values)

print(f'len(all_ingredient_names): {len(all_ingredient_names)}, len(all_units): {len(all_units)}')

# for unit in all_units:
#     # print unit and an example of corresponding ingredient
#     ingredient = recipe_ingredients_df[recipe_ingredients_df['unit'] == unit]['name'].to_list()
#     print(f'unit: {unit}, ingredient: {ingredient}')

print(recipe_costs)
print(f'Total number of recipes: {len(recipe_costs)}')


# load Recipe_Cost_Formalized.csv
recipe_cost_df = pd.read_csv('data/Recipe_Cost_Formalized.csv')
# add the new cost column
recipe_cost_df['Cost'] = recipe_cost_df['Name'].apply(lambda x: recipe_costs.get(x, None))
# check if there is na in the cost column
print(recipe_cost_df[recipe_cost_df['Cost'].isna()])
# save the dataframe to csv
recipe_cost_df.to_csv('data/recipe_time_cost.csv', index=False)