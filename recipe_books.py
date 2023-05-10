import randomiser as r
import recipe_generators as rg

def get_recipe_book(book=None, food_type=None):
    
    HVSF_food_types = ['India & Sri Lanka',
                       'Thailand, Laos and Vietnam',
                       'Malaysia & Indonesia']
    
    TVB_food_types = ['Aubergine',
                      'Beetroot',
                      'Broccoli',
                      'Cabbage',
                      'Carrots',
                      'Cauliflower',
                      'Courgettes',
                      'Leeks',
                      'Mushrooms',
                      'Potatoes']
    
    BoshHV_food_types = ['Lighter',
                         'Greener',
                         'Heartier',
                         'Treats',
                         'Breakfast']
    
    recipe_books = {
        'Healthy Vegan Street Food': rg.Healthy_Vegan_Steet_Food(),
        'The Veg Box': rg.The_Veg_Box(),
        'Bosh! Healthy Vegan': rg.Bosh_Healthy_Vegan()
    }
    
    ### GENORATING THE RANDOM RECIPE ###
    if food_type in HVSF_food_types:
        book_choice = rg.Healthy_Vegan_Steet_Food(food_type)
        
    elif food_type in TVB_food_types:
        book_choice = rg.The_Veg_Box(food_type)
        
    elif food_type in BoshHV_food_types:
        book_choice = rg.Bosh_Healthy_Vegan(food_type)
    
    else:
        _, book_choice = r.get_random_book(recipe_books, book)
        
    return book_choice