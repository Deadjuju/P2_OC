import json
import csv
from pathlib import Path
import requests
import time

from one_category.list_urls_book_one_category import get_urls_book_category
from one_product.one_product_functions import extract_one_book, extract_cover_choice
from entire_site_functions import save_extract


start = time.time()
END_MESSAGE = "INFORMATION: End of extraction of entire site."
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


# Extract cover True or False
cover = extract_cover_choice()


# data extraction path
current_dir = Path.cwd()
path_to_extract = current_dir / ".." / "extracts"
path_to_extract.mkdir(exist_ok=True)
path_to_extract_entire_site = path_to_extract / "extract_entire_site"
path_to_extract_entire_site.mkdir(exist_ok=True)


with open(file="../category_lists/dico_category_list.json", mode="r", encoding="utf-8") as f:
    catego_dico = json.load(f)
with open(file="../category_lists/category_list.json", mode="r", encoding="utf-8") as f:
    catego_list = json.load(f)


# iterate for each url's category
j = 1
url_list_for_category = []
for category, url_category in catego_dico.items():
    print(category, url_category)

    # create path to extract the category & the covers
    path_to_extract_category = path_to_extract_entire_site / category
    path_to_extract_category.mkdir(exist_ok=True)
    path_to_extract_images = path_to_extract_category / "images"
    if cover:
        path_to_extract_images.mkdir(exist_ok=True)

    # recupe urls to scrape (/ category)
    url_list_for_category = get_urls_book_category(url_to_scrap=url_category)
    print(f"URL LIST FOR CATEGORY: {url_list_for_category}")

    print(f"INFORMATION: Start to extract books from {category}.")

    # extract data for each book, stock in a list
    # extract covers
    i = 1
    datas_list = []
    for url in url_list_for_category:
        print(f"Category {category}: {j}/{(len(catego_dico))}\n"
              f"Page {i}/{len(url_list_for_category)}")

        data = extract_one_book(book_url=url, cover=cover, img_path=path_to_extract_images)

        datas_list.append(data)

        i += 1
    j += 1

    # save data to csv file
    save_extract(category=category,
                 path=path_to_extract_category,
                 labels=LABELS,
                 datas_list=datas_list)


print(END_MESSAGE)


end = time.time()
print(f"Execution time: {end - start} sec")
