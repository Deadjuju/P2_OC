import csv
import time

from one_category.list_urls_book_one_category import get_urls_book_category
from one_product.one_product_functions import extract_one_book, extract_cover_choice
from one_category.category_selector import category_choice

END_MESSAGE = "INFORMATION: End of extraction"


def one_category(labels, path_to_extract, path_to_list_categories, path_to_dico_categories):
    # choose book category
    choose_a_category = category_choice(path_to_list_categories=path_to_list_categories,
                                        path_to_dico_categories=path_to_dico_categories)
    url_category_to_scrap = choose_a_category[0]
    category_name = choose_a_category[1]

    # Extract cover True or False
    cover = extract_cover_choice()

    # list of urls of the chosen category
    url_list_for_category = get_urls_book_category(url_to_scrap=url_category_to_scrap)
    print(url_list_for_category)

    # data extraction path
    path_to_extract_one_category = path_to_extract / "extract_one_category"
    path_to_extract_one_category.mkdir(exist_ok=True)

    category_name = category_name.replace(" ", "_")
    path_directory_category = path_to_extract_one_category / category_name
    path_directory_category.mkdir(exist_ok=True)
    path_directory_img = path_directory_category / "img"
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
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for elem in datas_list:
            writer.writerow(elem)

    print(END_MESSAGE)
