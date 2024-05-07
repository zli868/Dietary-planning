import json
from datetime import datetime

import requests

def download_random_recipe(num_recipes=1):
    url = 'https://api.spoonacular.com/recipes/random'
    params = {
        'number': 10,
        'apiKey': '41f198eb1fda42e19a807b5858929e7c'
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data

def main():
    num_recipes = 10
    data = download_random_recipe(num_recipes)
    date_time_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open(f'data/recipe/random_recipe_{num_recipes}_{date_time_str}.json', 'w') as f:
        json.dump(data, f, indent=4)
    
if __name__ == '__main__':
    main()

# 'analyzedInstructions', if have length, then use length, else ask llm to generate time requried, so as to get a total time for the recipe