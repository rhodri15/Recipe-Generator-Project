import recipe_books as rb
import tools

user_book_choice = tools.user_input("Do you want to choose a book?")
user_food_choice = tools.user_input("Do you want to choose a food type?")


recipe = rb.get_recipe_book(user_book_choice, user_food_choice)

print(recipe)