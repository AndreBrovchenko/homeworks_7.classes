from pprint import pprint


class CookBook:
    """
    Class representing a cook book.
    ...
    Attributes
    --------
    file_name : str
        filename containing the cookbook
    cook_book : dict
        Dictionary containing recipes.
        keys - Name of the dish, values - List of dictionaries with data on ingredients
    Methods
    ------
    """
    def __init__(self, file_name):
        """
        Reads a list of recipes from a file and places the resulting data into a dictionary
        :param file_name: file to read
        """
        self.file_name = file_name
        self.cook_book = {}
        with open(self.file_name) as file_recipes:
            for line in file_recipes:
                dish = line.strip()
                count_ingredients = int(file_recipes.readline())
                temp_list = []
                for item in range(count_ingredients):
                    ingredients, quantity, measure = file_recipes.readline().split('|')
                    ingredients = ingredients.strip()
                    quantity = int(quantity.strip())
                    measure = measure.strip()
                    temp_list.append(
                        {"ingredient_name": ingredients, "quantity": quantity, "measure": measure}
                    )
                self.cook_book[dish] = temp_list
                file_recipes.readline()


best_cookbook = CookBook('recipes.txt')
pprint(best_cookbook.cook_book)
