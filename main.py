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
    amount_ingredients : dict
        Ingredient Dictionary.
        keys - Ingredient name, values - Ingredient data dictionary
    Methods
    ------
    getingredients(self, dishes, person_count):
        Accepts a list of dishes from the cook_book and the number of persons.
    """
    def __init__(self, file_name):
        """
        Reads a list of recipes from a file and places the resulting data into a dictionary
        :param file_name: file to read
        """
        self.file_name = file_name
        self.cook_book = {}
        self.amount_ingredients = {}
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

    def getingredients(self, dishes, person_count):
        """
        Accepts a list of dishes from the cook_book and the number of persons
        :param dishes: List of dishes for calculating the amount of ingredients
        :param person_count: Number of persons for cooking
        :return: List of ingredients for cooking
        """
        for dish in dishes:
            for item in self.cook_book:
                if item == dish:
                    for el in self.cook_book[dish]:
                        if self.amount_ingredients.get(el['ingredient_name']) is None:
                            quantity = el['quantity'] * person_count
                            temp_dict = dict(quantity=quantity, measure=el['measure'])
                            self.amount_ingredients[el['ingredient_name']] = temp_dict
                        else:
                            quantity = el['quantity'] + el['quantity'] * person_count
                            temp_dict = dict(quantity=(el['quantity'] + quantity), measure=el['measure'])
                            self.amount_ingredients[el['ingredient_name']] = temp_dict

        return self.amount_ingredients


def write_sorted_files(list_files, out_files):
    """
    Opens files in a list, counts the number of lines in the file.
    The result of calculations is placed in a dictionary, the key is the file name,
    the value is the number of lines in the file.
    The contents of the source files are written to the resulting file in the order
    of increasing number of lines in them.
    :param list_files: Source files list
    :param out_files:  The resulting file
    :return: A file containing information from all source data
    """
    data_files = dict()
    for files in list_files:
        with open(files) as files_read:
            lines = files_read.readlines()
            data_files[files_read.name] = len(lines)
    data_files_sorted = list(data_files.items())
    data_files_sorted.sort(key=lambda i: i[1])

    with open(out_files, 'w') as files_out:
        pass
    with open(out_files, 'a') as files_out:
        for item in data_files_sorted:
            with open(item[0]) as file_in:
                files_out.write(str(item[0]) + '\n')
                files_out.write(str(item[1]) + '\n')
                for line in file_in:
                    files_out.write(line.strip() + '\n')

    return data_files_sorted


best_cookbook = CookBook('recipes.txt')
pprint(best_cookbook.cook_book)

# pprint(best_cookbook.getingredients(['Омлет', 'Фахитос'], 2))
pprint(best_cookbook.getingredients(['Запеченный картофель', 'Омлет'], 2))

print(write_sorted_files(['1.txt', '2.txt', '3.txt'], 'out.txt'))
