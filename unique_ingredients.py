# perform similarity analysis on ingredients to find unique ingredients
# this list of unique ingredients is later used to search for price of ingredients.

import pandas as pd
import spacy
import json

# Load the spaCy model for NER
nlp = spacy.load("en_core_web_sm")

# Load ingredients_df from recipe_ingredients.csv
ingredients_df = pd.read_csv('data/recipe_ingredients.csv')

import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Normalize ingredient names: convert to lowercase
ingredients_df['name'] = ingredients_df['name'].str.lower()

# Tokenization and Lemmatization
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = re.sub(r'\d+', '', text)  # Remove digits
    tokens = word_tokenize(text)  # Tokenize
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words and token.isalnum()]  # Lemmatize and remove stopwords and non-alphanumeric tokens
    return ' '.join(tokens)

ingredients_df['processed_name'] = ingredients_df['name'].apply(preprocess_text)

# Vectorization using TF-IDF
vectorizer = TfidfVectorizer().fit_transform(ingredients_df['processed_name'])
vectors = vectorizer.toarray()

# Calculate similarity matrix
similarity_matrix = cosine_similarity(vectors)

# Threshold for pruning redundant ingredients
threshold = 0.8

# Initialize the mapping column with the ingredient names themselves
ingredients_df['mapped_name'] = ingredients_df['name']

# Find non-redundant ingredients based on similarity
non_redundant_indices = []
for idx, row in enumerate(similarity_matrix):
    if not any(row[:idx] > threshold):
        non_redundant_indices.append(idx)
    else:
        # Find the index of the most similar ingredient
        most_similar_idx = row[:idx].argmax()
        most_similar_ingredient = ingredients_df.iloc[most_similar_idx]['name']
        if not most_similar_ingredient == ingredients_df.iloc[idx]['name']:
            print(f"Ingredient '{ingredients_df.iloc[idx]['name']}' is similar to '{most_similar_ingredient}'")
        ingredients_df.at[idx, 'mapped_name'] = most_similar_ingredient

# Create a pruned dataframe
pruned_ingredients_df = ingredients_df.iloc[non_redundant_indices]

# Drop the processed_name column for the final output
pruned_ingredients_df = pruned_ingredients_df.drop(columns=['processed_name'])
# save non-redundant ingredients to csv
pruned_ingredients_df.to_csv('data/non_redundant_ingredients.csv', index=False)

pruned_ingredients_df.reset_index(drop=True, inplace=True)
print(pruned_ingredients_df)
ingredients = pruned_ingredients_df['name'].to_list()
# print out 50 ingredients at a time
for i in range(0, len(ingredients), 50):
    print(ingredients[i:i+50])
ingredients_df.drop(columns=['processed_name'], inplace=True)
print(ingredients_df)

# save ingredient mapping to a json file
ingredient_mapping = ingredients_df.set_index('name')['mapped_name'].to_dict()

with open('data/ingredient_mapping.json', 'w') as f:
    json.dump(ingredient_mapping, f, indent=4)
