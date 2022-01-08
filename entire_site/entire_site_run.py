import json
import csv
from pathlib import Path
import requests

from one_category.list_urls_book_one_category import get_urls_book_category
from one_product.one_product_functions import extract_one_book


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


# data extraction path
current_dir = Path.cwd()
path_to_extract = current_dir / ".." / "extracts"
path_to_extract.mkdir(exist_ok=True)
path_to_extract_entire_site = path_to_extract / "extract_entire_site"
path_to_extract_entire_site.mkdir(exist_ok=True)
path_to_extract_category = path_to_extract_entire_site / "categories"
path_to_extract_category.mkdir(exist_ok=True)
path_to_extract_images = path_to_extract_entire_site / "images"
path_to_extract_images.mkdir(exist_ok=True)


with open(file="../category_lists/dico_category_list.json", mode="r", encoding="utf-8") as f:
    catego_dico = json.load(f)
with open(file="../category_lists/category_list.json", mode="r", encoding="utf-8") as f:
    catego_list = json.load(f)


# iterate for each url's category
j = 1
for category, url_category in catego_dico.items():
    print(category, url_category)

    # recupe urls to scrape (/ category)
    url_list_for_category = get_urls_book_category(url=url_category)

    print(f"INFORMATION: Start to extract book from {category}")

    # extract data for each book, stock in a list
    i = 1
    datas_list = []
    for url in url_list_for_category:
        print(f"Category {category}: {j}/{(len(catego_dico))}\n"
              f"Page {i}/{len(url_list_for_category)}")

        data = extract_one_book(book_url=url)
        # print(f"Data\n{data}")

        # generate img
        title = data["title"]
        specialChars = "?!#$%^&*():'’,.;\"'/ "
        for specialChar in specialChars:
            title = title.replace(specialChar, '_')
        url_image = data["image_url"]
        f = open(f'{path_to_extract_images}\\{title}.jpg', 'wb')
        img = requests.get(url_image)
        f.write(img.content)
        f.close()

        datas_list.append(data)

        i += 1
    j += 1

    # save data to csv file
    file_name = f"{category.replace(' ', '_')}__extract.csv"
    with open(file=f'{path_to_extract_category}/{file_name}', mode='w', encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=LABELS)
        writer.writeheader()
        for elem in datas_list:
            writer.writerow(elem)

print(END_MESSAGE)

