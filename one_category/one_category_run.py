import csv
from pathlib import Path
import time

from list_urls_book_one_category import get_urls_book_category
from one_product.one_product_functions import extract_one_book, extract_cover_choice
from category_selector import category_choice

END_MESSAGE = "INFORMATION: End of extraction"
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

# choose book category
choose_a_category = category_choice()
url_category_to_scrap = choose_a_category[0]
category_name = choose_a_category[1]


# Extract cover True or False
cover = extract_cover_choice()


start = time.time()


# list of urls of the chosen category
url_list_for_category = get_urls_book_category(url_to_scrap=url_category_to_scrap)
print(url_list_for_category)

# data extraction path
current_dir = Path.cwd()
path_to_extract = current_dir / ".." / "extracts"
path_to_extract.mkdir(exist_ok=True)
path_to_extract_one_category = path_to_extract / "extract_one_category"
path_to_extract_one_category.mkdir(exist_ok=True)

category_name = category_name.replace(" ", "_")
path_directory_category = path_to_extract_one_category / category_name
path_directory_category.mkdir(exist_ok=True)
path_directory_img = path_directory_category / "img_directory"
if cover:
    path_directory_img.mkdir(exist_ok=True)
extract_file = f"{category_name}_extract.csv"


# extract data for each book, stock in a list
i = 1
datas_list = []
for url in url_list_for_category:
    print(f"{i}/{len(url_list_for_category)}")

    data = extract_one_book(book_url=url, cover=cover, img_path=path_directory_img)
    datas_list.append(data)

    i += 1

# save datas to csv file
with open(file=f'{path_directory_category}/{extract_file}',
          mode='w',
          encoding="utf-8",
          newline="") as f:
    writer = csv.DictWriter(f, fieldnames=LABELS)
    writer.writeheader()
    for elem in datas_list:
        writer.writerow(elem)

print(END_MESSAGE)


end = time.time()
print(f"Execution time: {end - start} sec")
