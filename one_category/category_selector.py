import json


def load_file(file: str):
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
        print(f"ERROR: file - {file} does not exist."
              f"You can create it by running the script --> 'category_lists/list_categories_generator.py'.")
    else:
        return requested_file


def category_choice(path_to_list_categories, path_to_dico_categories):
    """Asks the user to choose a category.
    Can display the list of all categories if needed.

                Args:
                    path_to_list_categories (str): path to the list with all categories
                    path_to_dico_categories (str): path to the list of categories with url
                Returns:
                    tuple: (first page url of the desired category, category name )
                """
    catego_dico = load_file(file=path_to_dico_categories)
    catego_list = load_file(file=path_to_list_categories)

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


