import json

import requests

url = 'https://api.spoonacular.com/recipes/random'
params = {
    'number': 1,
    'apiKey': '41f198eb1fda42e19a807b5858929e7c'
}

response = requests.get(url, params=params)
data = response.json()

print(data)

# save to data/recipe/random_recipe.json
with open('data/recipe/random_recipe.json', 'w') as f:
    json.dump(data, f)