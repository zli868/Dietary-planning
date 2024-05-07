import json

def main():
    # load the recipe data
    with open('data/recipe/random_recipe_10_2024-05-07-17-29-31.json') as f:
        data = json.load(f)

    # Create dataframe with columns "title", "readyInMinutes", "servings"

    all_ingredient_names = []
    # print "title" of each recipe in "recipes" list.
    for recipe in data['recipes']:
        ingredients = recipe['extendedIngredients']
        ingredient_names = [ingredient['name'] for ingredient in ingredients]

        all_ingredient_names.append(ingredient_names)
    
    all_ingredient_names = set(all_ingredient_names)

    print(all_ingredient_names)

if __name__ == '__main__':
    main()