## Note that the pipeline is our worflow pipeline; actual pipeline you should follow starts at step 3; this is because manual collection of grocery price is done before thsi stage.

### 1. Setup Environment
#### 1.1 download and install conda
https://conda.io/projects/conda/en/latest/user-guide/install/index.html
after installation is completed, run in command line `conda init --all`
#### 1.2 create conda environment
`conda create -n 'msml604final' python=3.12`
`conda activate msml604final`
#### 1.3 install python libraries
`pip install -r requirements.txt`


### 2. Data Collection
#### 2.1 download random recipe
run `python download_recipe.py`

This makes rest api call to `spoonacular` to receive 50 random recipes. Number of recipes downloaded can be changed by modifying `num_recipes`

#### 2.2 get nutritional value
run `python recipe_nutrition_value.py`

This makes rest api call to `edamam` to get nutritional value of each serving of the recipes just downloaded

#### 2.3 get recipe price

##### 2.3.1 get unique ingredients
run `python unique_ingredients.py`

This derives a list of unique ingredients through NLP analysis, so that workload for collecting ingredient price is less cumbersome.

##### 2.3.2 collect unique ingredients per-gram prices
collect and form the data in `ingredient_prices.py` as a dictionary

##### 2.3.3 setup interpretation of "unit"
examine the units of the ingredients, and setup `weights` dicitonary and `get_ingredient_cost` function to suit the units of the ingredients

##### 2.3.4 get recipe cost
run `python recipe_cost.py` to get the recipe cost in recipe_time_cost.csv 

AWAITING MODIFICATION