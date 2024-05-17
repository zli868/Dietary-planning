ingredient_prices = {
    '6 liter milk': 0.002,  # $0.12 per liter, 6 liters is 6000 grams, 0.12 / 6000
    'active yeast': 0.02,   # $2 per 100 grams
    'agave nectar': 0.03,   # $3 per 100 grams
    'ajwain seeds': 0.05,   # $5 per 100 grams
    'all purpose flour': 0.002,  # $2 per 1000 grams
    'almond extract': 0.20,  # $20 per 100 grams
    'almond meal': 0.01,    # $10 per 1000 grams
    'almond milk': 0.002,   # $2 per liter, approximately $2 per 1000 grams
    'almonds': 0.01,        # $10 per 1000 grams
    'apple cider vinegar': 0.003,  # $3 per liter, approximately $3 per 1000 grams
    'apple sauce': 0.004,   # $4 per 1000 grams
    'applesauce': 0.004,    # Same as apple sauce
    'asafetida': 0.10,      # $10 per 100 grams
    'asian sesame oil': 0.03,  # $30 per liter, approximately $30 per 1000 grams
    'avocado': 0.01,        # $10 per 1000 grams
    'bacon': 0.01,          # $10 per 1000 grams
    'baking powder': 0.005,  # $5 per 1000 grams
    'baking soda': 0.003,   # $3 per 1000 grams
    'banana': 0.002,        # $2 per 1000 grams
    'basil': 0.02,          # $20 per 1000 grams (fresh)
    'basil leaves': 0.10,   # $10 per 100 grams (dried)
    'bay leaf': 0.20,       # $20 per 100 grams
    'beef broth': 0.004,    # $4 per liter, approximately $4 per 1000 grams
    'beef chuck': 0.01,     # $10 per 1000 grams
    'beef chuck roast': 0.01,  # Same as beef chuck
    'beef gravy': 0.01,     # $10 per 1000 grams
    'beer': 0.001,          # $1 per liter, approximately $1 per 1000 grams
    'beets': 0.002,         # $2 per 1000 grams
    'beijing cabbage': 0.001,  # $1 per 1000 grams
    'bell pepper': 0.003,   # $3 per 1000 grams
    'biscuits': 0.01,       # $10 per 1000 grams
    'bittersweet chocolate chips': 0.02,  # $20 per 1000 grams
    'black beans': 0.001,   # $1 per 1000 grams
    'blanched almonds and': 0.01,  # Same as almonds
    'blueberries': 0.01,    # $10 per 1000 grams
    'bouquet garnic': 0.05,  # $50 per 1000 grams (approximation)
    'bread crumbs': 0.002,  # $2 per 1000 grams
    'bread flour': 0.002,   # Same as all purpose flour
    'breadcrumbs': 0.002,   # Same as bread crumbs
    'broccoli florets': 0.003,  # $3 per 1000 grams
    'broccolini': 0.004,    # $4 per 1000 grams
    'brown rice flour': 0.004,  # $4 per 1000 grams
    'brown sugar': 0.002,   # $2 per 1000 grams
    'butter': 0.01,         # $10 per 1000 grams
    'buttermilk': 0.002,    # $2 per liter, approximately $2 per 1000 grams
    'canola oil': 0.002,    # $2 per liter, approximately $2 per 1000 grams
    'carrot': 0.002,        # $2 per 1000 grams
    'cauliflower': 0.002,   # $2 per 1000 grams
    'cayenne': 0.10,        # $10 per 100 grams
    'celery': 0.002,         # $2 per 1000 grams
    'cheddar cheese': 0.01,  # $10 per 1000 grams
    'cherry tomatoes': 0.005,  # $5 per 1000 grams
    'chicken': 0.008,  # $8 per 1000 grams
    'chicken breasts': 0.01,  # $10 per 1000 grams
    'chicken broth': 0.004,  # $4 per liter, approximately $4 per 1000 grams
    'chicken fat': 0.01,  # $10 per 1000 grams
    'chicken stock': 0.004,  # $4 per liter, approximately $4 per 1000 grams
    'chickpea flour': 0.006,  # $6 per 1000 grams
    'chili': 0.02,  # $20 per 1000 grams
    'chili slit': 0.02,  # $20 per 1000 grams
    'chilies': 0.02,  # $20 per 1000 grams
    'chilli flakes': 0.05,  # $50 per 1000 grams
    'chocolate': 0.02,  # $20 per 1000 grams
    'chocolate and hazelnuts': 0.03,  # $30 per 1000 grams
    'chocolate chips': 0.02,  # $20 per 1000 grams
    'chocolate chunks': 0.02,  # $20 per 1000 grams
    'chocolate-hazelnut pirouette cookies': 0.03,  # $30 per 1000 grams
    'choux pastry': 0.01,  # $10 per 1000 grams
    'cilantro': 0.02,  # $20 per 1000 grams (fresh)
    'cinnamon': 0.05,  # $50 per 1000 grams
    'cocoa powder': 0.02,  # $20 per 1000 grams
    'coconut beverage': 0.004,  # $4 per liter, approximately $4 per 1000 grams
    'coconut butter': 0.02,  # $20 per 1000 grams
    'coconut milk': 0.004,  # $4 per liter, approximately $4 per 1000 grams
    'coconut sugar': 0.02,  # $20 per 1000 grams
    'coffee granules': 0.04,  # $40 per 1000 grams
    'condensed cream of chicken soup': 0.005,  # $5 per 1000 grams
    "confectioner's sugar - optional": 0.002,  # $2 per 1000 grams
    "confectioners' sugar": 0.002,  # $2 per 1000 grams
    'corn on the cob': 0.003,  # $3 per 1000 grams
    'cornbread': 0.01,  # $10 per 1000 grams
    'cornstarch': 0.004,  # $4 per 1000 grams
    'corriander': 0.02,  # $20 per 1000 grams
    'cranberries': 0.01,  # $10 per 1000 grams
    'cream': 0.01,  # $10 per 1000 grams
    'cream cheese': 0.01,  # $10 per 1000 grams
    'cremini mushrooms': 0.01,  # $10 per 1000 grams
    'cremini; but your choice)': 0.01,  # Same as cremini mushrooms
    'cucumbers': 0.002,  # $2 per 1000 grams
    'cumin': 0.02,  # $20 per 1000 grams
    'cumin seeds': 0.02,  # $20 per 1000 grams
    'curry powder': 0.02,  # $20 per 1000 grams
    'daikon radish': 0.002,  # $2 per 1000 grams
    'dates': 0.01,  # $10 per 1000 grams
    'defrosted blackberries': 0.01,  # $10 per 1000 grams
    'dill': 0.03,  # $30 per 1000 grams
    'drop natural food coloring': 0.50,  # $500 per 1000 grams (approximation)
    'ear of corn': 0.003,  # $3 per 1000 grams
    'earth balance buttery spread': 0.01,  # $10 per 1000 grams
    'egg': 0.005,  # $5 per 1000 grams (approximately $0.5 per egg, average weight 50 grams)
    'egg yolks': 0.01,  # $10 per 1000 grams (approximation)
    'eight packages ounces cream cheese': 0.01,  # $10 per 1000 grams
    'enoki mushrooms': 0.01,  # $10 per 1000 grams
    'espresso': 0.05,  # $50 per 1000 grams
    'extra virgin olive oil': 0.01,  # $10 per 1000 grams
    'fat-trimmed beef flank steak': 0.02,  # $20 per 1000 grams
    'fenugreek leaves': 0.04,  # $40 per 1000 grams
    'five spice powder': 0.03,  # $30 per 1000 grams
    'flaxseeds': 0.02,  # $20 per 1000 grams
    'flour': 0.002,  # $2 per 1000 grams
    'full cream milk': 0.002,  # $2 per liter, approximately $2 per 1000 grams
    'full-bodied wine': 0.01,  # $10 per liter, approximately $10 per 1000 grams
    'g heavy whipping cream': 0.01,  # $10 per 1000 grams
    'g puff pastry': 0.02,  # $20 per 1000 grams
    'g sugar': 0.002,  # $2 per 1000 grams
    'ganache': 0.02,  # $20 per 1000 grams (approximation)
    'garlic': 0.01,  # $10 per 1000 grams
    'garlic bu': 0.01,  # $10 per 1000 grams (approximation)
    'garlic clove': 0.01,  # $10 per 1000 grams
    'garlic powder': 0.02,  # $20 per 1000 grams
    'garnish: cilantro': 0.02,  # $20 per 1000 grams (fresh)
    'ghee': 0.02,  # $20 per 1000 grams
    'ginger': 0.01,  # $10 per 1000 grams
    'gloves garlic': 0.01,  # $10 per 1000 grams (approximation)
    'golden syrup': 0.02,  # $20 per 1000 grams
    'graham wafer crumbs': 0.02,  # $20 per 1000 grams
    'granny smith apples': 0.002,  # $2 per 1000 grams
    'grape seed oil': 0.01,  # $10 per 1000 grams
    'grapeseed oil': 0.01,  # $10 per 1000 grams (same as grape seed oil)
    'green beans': 0.003,  # $3 per 1000 grams
    'green onion': 0.005,  # $5 per 1000 grams
    'ground beef': 0.01,  # $10 per 1000 grams
    'ground cardamom': 0.10,  # $100 per 1000 grams
    'ground coriander': 0.02,  # $20 per 1000 grams
    'ground cumin': 0.02,  # $20 per 1000 grams
    'ground flax': 0.02,  # $20 per 1000 grams (same as flaxseeds)
    'ground flaxseed': 0.02,  # $20 per 1000 grams (same as flaxseeds)
    'ground nutmeg': 0.10,  # $100 per 1000 grams
    'ground pepper': 0.02,  # $20 per 1000 grams
    'gruyère cheese': 0.02,  # $20 per 1000 grams
    'half-and-half': 0.01,  # $10 per 1000 grams
    'herbs': 0.02,  # $20 per 1000 grams (general approximation)
    'honey': 0.01,  # $10 per 1000 grams
    'icing sugar': 0.002,  # $2 per 1000 grams
    'jalapeno chile peppers': 0.01,  # $10 per 1000 grams
    'jalapeño peppers': 0.01,  # $10 per 1000 grams
    'jar pear': 0.01,  # $10 per 1000 grams (approximation)
    'juice of lemon': 0.01,  # $10 per liter, approximately $10 per 1000 grams
    'juice of lime': 0.01,  # $10 per liter, approximately $10 per 1000 grams
    'kahlua': 0.05,  # $50 per liter, approximately $50 per 1000 grams
    'ketchup': 0.003,  # $3 per 1000 grams
    'kidney beans': 0.001,  # $1 per 1000 grams
    'korean marinade': 0.01,  # $10 per 1000 grams
    'kosher salt': 0.001,  # $1 per 1000 grams
    'leek': 0.003,  # $3 per 1000 grams
    'lemon verbena leaves': 0.05,  # $50 per 1000 grams
    'lemon zest': 0.02,  # $20 per 1000 grams
    'lentils': 0.002,  # $2 per 1000 grams
    'lime': 0.01,  # $10 per 1000 grams
    'mango': 0.01,  # $10 per 1000 grams
    'mango pieces': 0.01,  # $10 per 1000 grams
    'maple syrup': 0.01,  # $10 per 1000 grams
    'milk': 0.002,  # $2 per 1000 grams
    'mint leaves': 0.02,  # $20 per 1000 grams
    'molasses': 0.005,  # $5 per 1000 grams
    'mung bean sprouts': 0.01,  # $10 per 1000 grams
    'mushrooms': 0.01,  # $10 per 1000 grams
    'natural butter extract': 0.50,  # $500 per 1000 grams (approximation)
    'nutella': 0.02,  # $20 per 1000 grams
    'nutella spread': 0.02,  # $20 per 1000 grams (same as nutella)
    'nutmeg': 0.10,  # $100 per 1000 grams
    'oats': 0.002,  # $2 per 1000 grams
    'oil': 0.002,  # $2 per 1000 grams (generic oil)
    'olive oil': 0.01,  # $10 per 1000 grams
    'olive oil to brush vegetables': 0.01,  # $10 per 1000 grams (same as olive oil)
    'onion': 0.002,  # $2 per 1000 grams
    'onion powder': 0.02,  # $20 per 1000 grams
    'orange cauliflower': 0.002,  # $2 per 1000 grams (same as regular cauliflower)
    'overripe banana': 0.002,  # $2 per 1000 grams
    'panko crumbs': 0.01,  # $10 per 1000 grams
    'paprika': 0.02,  # $20 per 1000 grams
    'parmesan cheese': 0.02,  # $20 per 1000 grams
    'parsley': 0.01,  # $10 per 1000 grams
    'pasteurized egg whites': 0.01,  # $10 per 1000 grams
    'pastry': 0.02,  # $20 per 1000 grams
    'pastry cream': 0.02,  # $20 per 1000 grams
    'peanut butter': 0.01,  # $10 per 1000 grams
    'peanut oil': 0.01,  # $10 per 1000 grams
    'pearl onions': 0.01,  # $10 per 1000 grams
    'pecans': 0.02,  # $20 per 1000 grams
    'penne pasta': 0.002,  # $2 per 1000 grams
    'pepper': 0.02,  # $20 per 1000 grams
    'peppermint extract': 0.50,  # $500 per 1000 grams (approximation)
    'pickled jalapenos': 0.01,  # $10 per 1000 grams
    'pineapple': 0.01,  # $10 per 1000 grams
    'pink salt': 0.01,  # $10 per 1000 grams
    'pistachios': 0.02,  # $20 per 1000 grams
    'popsicle moulds': 0.05,  # $50 per 1000 grams (approximation)
    'pork loin': 0.01,  # $10 per 1000 grams
    'potatoes': 0.001,  # $1 per 1000 grams
    'poultry seasoning': 0.05,  # $50 per 1000 grams
    'powder sugar': 0.002,  # $2 per 1000 grams
    'powdered sugar': 0.002,  # $2 per 1000 grams (same as powder sugar)
    'powdered xylitol': 0.04,  # $40 per 1000 grams
    'quinoa': 0.01,  # $10 per 1000 grams
    'raspberries': 0.01,  # $10 per 1000 grams
    'raspberry jam': 0.01,  # $10 per 1000 grams
    'red wine': 0.01,  # $10 per liter, approximately $10 per 1000 grams
    'reserve a bit of sugar and cream': 0.01,  # $10 per 1000 grams (approximation)
    'rice': 0.002,  # $2 per 1000 grams
    'rice flour': 0.004,  # $4 per 1000 grams
    'rice vinegar': 0.005,  # $5 per liter, approximately $5 per 1000 grams
    'rosemary': 0.03,  # $30 per 1000 grams
    'rum': 0.02,  # $20 per liter, approximately $20 per 1000 grams
    'salad oil': 0.002,  # $2 per 1000 grams
    'salmon fillet': 0.02,  # $20 per 1000 grams
    'salt': 0.001,  # $1 per 1000 grams
    'salt & pepper': 0.015,  # $15 per 1000 grams (approximation)
    'sea salt': 0.002,  # $2 per 1000 grams
    'sesame oil': 0.03,  # $30 per 1000 grams
    'sesame seed': 0.01,  # $10 per 1000 grams
    'shallot': 0.01,  # $10 per 1000 grams
    'sharp cheddar': 0.01,  # $10 per 1000 grams
    'short macaroni': 0.002,  # $2 per 1000 grams
    'snow peas': 0.01,  # $10 per 1000 grams
    'soba noodles': 0.01,  # $10 per 1000 grams
    'sorghum flour': 0.01,  # $10 per 1000 grams
    'soy milk': 0.003,  # $3 per liter, approximately $3 per 1000 grams
    'spelt flour': 0.01,  # $10 per 1000 grams
    'strawberries': 0.01,  # $10 per 1000 grams
    'superfine sugar': 0.002,  # $2 per 1000 grams
    'swiss chard leaves': 0.01,  # $10 per 1000 grams
    'tamari sauce': 0.01,  # $10 per liter, approximately $10 per 1000 grams
    'thyme': 0.03,  # $30 per 1000 grams
    'tomato': 0.002,  # $2 per 1000 grams
    'tomato paste': 0.01,  # $10 per 1000 grams
    "trader joe's spicy peanut vinaigrette": 0.02,  # $20 per 1000 grams (approximation)
    'turmeric': 0.02,  # $20 per 1000 grams
    'turmeric little': 0.02,  # $20 per 1000 grams (same as turmeric)
    'unbleached all purpose flour': 0.002,  # $2 per 1000 grams
    'vanilla': 0.50,  # $500 per 1000 grams
    'vanilla extract': 0.50,  # $500 per 1000 grams (same as vanilla)
    'vanilla sugar': 0.02,  # $20 per 1000 grams
    'vegetable broth': 0.003,  # $3 per liter, approximately $3 per 1000 grams
    'vegetable oil': 0.002,  # $2 per 1000 grams
    'vegetables': 0.005,  # $5 per 1000 grams (general approximation)
    'vinegar': 0.005,  # $5 per liter, approximately $5 per 1000 grams
    'walnuts': 0.02,  # $20 per 1000 grams
    'wasabi or)': 0.10,  # $100 per 1000 grams (approximation)
    'water': 0.0001,  # $0.10 per 1000 grams
    'whipping cream': 0.01,  # $10 per 1000 grams
    'white wine': 0.01,  # $10 per liter, approximately $10 per 1000 grams
    'worcestershire sauce': 0.01,  # $10 per liter, approximately $10 per 1000 grams
    'yogurt': 0.01,  # $10 per 1000 grams
    'zucchini': 0.003,  # $3 per 1000 grams
    'cayenne pepper': 0.02,  # $20 per 1000 grams
    'heavy cream': 0.01,  # $10 per 1000 grams
    'chili powder': 0.02  # $20 per 1000 grams
}

