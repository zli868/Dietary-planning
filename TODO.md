TODO:
1. Pull data from spoonaculator for random recipe
2. collect desired information from raw recipe data, store in dataframe with columns "name, ingredient_1_amount (str that include the unit), .... ingredient_n_amount"
   1. note that similar ingredient name should be annexed using named entity recognition techinques.
   2. get time data from 'analyzedInstructions'
3. Use 'edamam' api to get nutritional information of each recipe, and also the weight of each ingredient given ingredient_amount strings for each recipe.
4. use some cost api to get cost of unit amount of each ingredient (a vector from ingredient to per-gram cost)


Note that the matrix that maps ingredients to its nutritional values is no longer needed; in original proposal, it is only used to calcualte the recipe nutritional value, now that edamam api is used to do that, no where else is the ingredient nutrition matrix needed.

# note that it seems that from https://developer.edamam.com/edamam-nutrition-api-demo the resulting nutritional return is very limited interms of type of nutrients; if necessary, align the nutritional requirement vector to match what is provided by edamam.