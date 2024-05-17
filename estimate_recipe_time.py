import json
import os
import time

import pandas as pd

from openai import OpenAI

# Load OpenAI API key from file
with open('openai_api.key', 'r') as file:
    openai_api_key = file.read().strip()

# # Set the API key
# openai.api_key = openai_api_key

def get_recipe_instructions(recipe_data: dict) -> list[str]:
    recipe_instructions = []
    for recipe in recipe_data['recipes']:
        instructions = []
        if 'analyzedInstructions' in recipe and len(recipe['analyzedInstructions']) > 0:
            for instruction in recipe['analyzedInstructions'][0]['steps']:
                instructions.append(instruction['step'])
        else:
            print("Warning: No Instructions found for  '{recipe['title']}'. Not able to estimate time for this recipe.")        

        instructions = [instruction.strip() for instruction in instructions if instruction.strip() != '']
        instruction_str = '\n'.join(instructions)
        instruction_str = 'Recipe Name: ' + recipe['title'] + '\n' + instruction_str
        recipe_instructions.append(instruction_str)
        # print(instruction_str)
        # print()
    return recipe_instructions


def estimate_recipe_time(recipe_instructions: list[str]):
    client = OpenAI(
    api_key = openai_api_key
    )
    
    time_estimation_df = pd.DataFrame(columns=['name', 'instruction', 'response', 'completion_tokens', 'time_taken', 'estimated_time'])
    # Make API call for each string
    for i, recipe_instruction in enumerate(recipe_instructions):
        start_time = time.time()
        print(f"processing {i+1}/{len(recipe_instructions)}")

        print(f"Recipe Instruction: \n{recipe_instruction}")
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert chef tasked with estimating TOTAL Active Time to cook a meal (not counting the time waiting for food to stew, cook in oven, etc.). You will be provided instructions for a recipe, where each instruction step is in a new line. Your analysis should be concise and you shouldn't print out the steps provided. Your response should end with \"Total Time: \{total_time\}\", where the total_time should be in terms of minutes."},
                {"role": "user", "content": recipe_instruction}
            ],
            max_tokens=500  # Adjust based on expected response length
        )
        response_text = response.choices[0].message.content.strip()
        print(f"Response: \n{response_text}")
        response_dict = {
            'name': recipe_instruction.split('\n')[0].split(':')[-1].strip(),
            'instruction': recipe_instruction,
            'response': response_text,
            'completion_tokens': response.usage.completion_tokens,
            'time_taken': time.time() - start_time,
            'estimated_time': response_text.split('Total Time: ')[-1].strip()
        }
        time_estimation_df.loc[i] = response_dict
        print(f"Token count: {response.usage}, Time taken: {time.time() - start_time:.2f} seconds")
    # Ensure the data directory exists
    os.makedirs('data', exist_ok=True)

    # Save time estimation data to file
    time_estimation_df.to_csv('data/estimated_recipe_time.csv', index=False)

    print("Responses have been saved to data/estimated_recipe_time.json")

def main():
    # Load the recipe data
    with open('data/recipe/random_recipe_50_2024-05-15-01-16-18.json', 'r') as file:
        recipe_data = json.load(file)

    # Get the recipe instructions
    recipe_instructions = get_recipe_instructions(recipe_data)

    # Estimate the time for each recipe
    estimate_recipe_time(recipe_instructions)

if __name__ == '__main__':
    main()