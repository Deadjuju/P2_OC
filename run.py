from pathlib import Path
import time

from one_product.one_product_run import one_book
from one_category.one_category_run import one_category
from entire_site.entire_site_run import entire_site
from art import welcome


LABELS = ["product_page_url",
          "universal_ product_code (upc)",
          "title",
          "price_including_tax",
          "price_excluding_tax",
          "number_available",
          "product_description",
          "category",
          "review_rating",
          "image_url"]


def user_choice():
    while True:
        make_choice = input("What do you want to do?\n"
                            " - To extract data from a single book, type '1'.\n"
                            " - To extract data from a chosen category, type '2'.\n"
                            " - To extract data from the entire site, type '3'.\n"
                            "Your choice: || --> ")
        if make_choice == "1":
            return 1
        elif make_choice == "2":
            return 2
        elif make_choice == "3":
            return 3
        else:
            print("-" * 50)
            print("Please type 1, 2 or 3.")


# create directory extract
current_dir = Path.cwd()
path_to_extract = current_dir / "extracts"
path_to_extract.mkdir(exist_ok=True)

time.sleep(1)


welcome()

choice = user_choice()

start = time.time()

if choice == 1:
    # Data from one book
    path_to_extract_one_product = path_to_extract / "extract_one_product"
    path_to_extract_one_product.mkdir(exist_ok=True)

    one_book(labels=LABELS, path_to_extract_one_product=path_to_extract_one_product)

if choice == 2:
    # Data from one category
    one_category(labels=LABELS, path_to_extract=path_to_extract)

if choice == 3:
    # Data from the entire site
    entire_site(labels=LABELS, path_to_extract=path_to_extract)


end = time.time()
print(f"Execution time: {end - start} seconds.")

