import json


def load_file_if_exist(file: str):
    """
    Checks if the desired file exists and loads it.
    If the file does not exist, the program stops.

        Args:
            file(str): file to load.

        Returns:
            list: requested file (list).
    """
    try:
        with open(file=file, mode="r", encoding="utf-8") as f:
            requested_file = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: -- {file} --\n"
              f"This file does not exist, you can generate it by executing the python file:\n"
              f"--> 'category_lists / list_categories_generator.py'. ")
        exit()
    else:
        return requested_file


dico_list_category_file = "../category_lists/dico_category_list.json"
category_list = "../category_lists/category_list.json"
catego_dico = load_file_if_exist(file=dico_list_category_file)
catego_list = load_file_if_exist(file=category_list)


def category_choice():
    """Asks the user to choose a category.
    Can display the list of all categories if needed.

                Args:
                Returns:
                    tuple: (first page url of the desired category, category name )
                """
    while True:
        which_category = input("Please type the name of the category to scrape:\n"
                               "To see the categories type 'list'\n"
                               "-->  | ").lower()
        # If the requested category exists:
        if which_category in catego_dico:
            return catego_dico[which_category], which_category
        else:
            if which_category == "list" or which_category == "l":
                print(catego_list)
            else:
                print(f"ERREUR: -- {which_category}-- does not exist. Please type a correct category.")


