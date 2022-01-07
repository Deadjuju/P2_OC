import json


with open(file="../category_lists/dico_category_list.json", mode="r", encoding="utf-8") as f:
    catego_dico = json.load(f)
with open(file="../category_lists/category_list.json", mode="r", encoding="utf-8") as f:
    catego_list = json.load(f)


def category_choice():
    while True:
        which_category = input("Please type the name of the category to scrape:\n"
                               "To see the categories type 'list'\n"
                               "-->  | ").lower()
        if which_category in catego_dico:
            return catego_dico[which_category]
        else:
            if which_category == "list" or which_category == "l":
                print(catego_list)
            else:
                print(f"ERREUR: -- {which_category}-- does not exist. Please type a correct category.")


