import requests
import json


API_KEY = 'ViwtyH9Eo6p6TZ7pk7rEhvsWGvgyvdXPGl65TDqQ'

# API endpoint for searching foods
api_url = "https://api.nal.usda.gov/fdc/v1/foods/search"

# Search query
query = "parsley"

# Construct the request URL with parameters
params = {
    'api_key': API_KEY,
    'query': query
}

# Make the GET request to the USDA FoodData Central API
response = requests.get(api_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Print the result if the API call was successful
    # print(response.json())
    # Save the result to a file 
    with open('data/recipe/food_search.json', 'w') as f:
        json.dump(response.json(), f)
else:
    # Print an error message if the API call failed
    print("Failed to fetch data:", response.status_code)
