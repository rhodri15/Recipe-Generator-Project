from random import choice as randomise

def get_random_book(dictionary, user_input):
    
    if user_input != None:
        recipe = dictionary[user_input]
        
        return user_input, recipe
        
    else:
        dictionary_keys = [k for k in dictionary]
        random_key = randomise(dictionary_keys)
        
        recipe = dictionary[random_key]
        
        return random_key, recipe


def get_random_recipe(dictionary: dict, user_input: str):
    
    if user_input != None:
        recipes = dictionary[user_input]
        recipe = randomise(recipes)
        
        return user_input, recipe
        
    else:
        dictionary_keys = [k for k in dictionary]
        random_key = randomise(dictionary_keys)
        
        recipes = dictionary[random_key]
        recipe = randomise(recipes)
        
        return random_key, recipe