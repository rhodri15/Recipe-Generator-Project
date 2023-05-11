"""
This module contains random recipe generators from a library of books.
Currnetly some recipes have more chance of being selected due to picture pages.

"""

import randomiser as r
import numpy as np

### CREATE RANDOM GENERATORS FOR EACH BOOK ###

def Healthy_Vegan_Steet_Food(chapter=None):
    
    Title = 'Healthy Vegan Street Food'
    Author = 'Jackie Kearney'

    regions = {
        'India & Sri Lanka': np.linspace(19, 77, 59),
        'Thailand, Laos & Vietnam': np.linspace(82, 151, 70),
        'Malaysia & Indonesia': np.linspace(156, 205, 50)
    }
    
    region, page = r.get_random_recipe(regions, chapter)
    
    message = f"""
        Your recipe is from the book '{Title}' by {Author}.
        The chapter is {region}.
        Go to page {int(page)}.
        Enjoy!
        """
    return message
    
    
def The_Veg_Box(chapter=None):
    
    Title = 'The Veg Box'
    Author = 'Stephen & David Flynn (The Happy Pear)'
    
    veg = {
        'Aubergine': np.linspace(52, 69, 18),
        'Beetroot': np.linspace(74, 91, 18),
        'Broccoli': np.linspace(96, 113, 18),
        'Cabbage': np.linspace(118, 135, 18),
        'Carrots': np.linspace(140, 157, 18),
        'Cauliflower': np.linspace(162, 179, 18),
        'Courgettes': np.linspace(184, 201, 18),
        'Leeks': np.linspace(206, 223, 18),
        'Mushrooms': np.linspace(228, 245, 18),
        'Potatoes': np.linspace(250, 267, 18)
    }
    
    veg, page = r.get_random_recipe(veg, chapter)
    
    message = f"""
        Your recipe is from the book '{Title}' by {Author}.
        The recipe uses {veg.lower()}.
        Go to page {int(page)}.
        See pages 270-276 for sauces and dips.
        Enjoy!
        """
    return message
    

def Bosh_Healthy_Vegan(chapter=None):
    
    Title = 'Bosh! Healthy Vegan'
    Author = 'Henry Firth & Ian Theasby (Bosh!)'
    
    contents = {
        'Lighter': np.linspace(67, 93, 27),
        'Greener': np.linspace(97, 120, 24),
        'Heartier': np.linspace(125, 186, 62),
        'Treats': np.linspace(191, 207, 17),
        'Breakfast': ['210 (top recipe)', '210 (bottom recipe)'] \
            + list(np.linspace(211, 232, 22))
    }
    
    meal, page = r.get_random_recipe(contents, chapter)
        
    message1 = f"""
        Your recipe is from the book '{Title}' by {Author}.
        The chapter is '{meal.lower()}'.
        Go to page {int(page)}.
        Enjoy!
        """
    message2 = f"""
        Your recipe is from the book '{Title}' by {Author}.
        The recipe's meal type is '{meal.lower()}'.
        Go to page {page}.
        Enjoy!
        """
    
    if type(page) != str:
        return message1
        
    else:
        return message2
