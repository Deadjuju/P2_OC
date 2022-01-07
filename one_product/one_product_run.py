import requests
from bs4 import BeautifulSoup
import lxml
import csv
from pathlib import Path

from one_product_functions import extract_one_book

URL = "https://books.toscrape.com/catalogue/william-shakespeares-star-wars-verily-a-new-hope-william-shakespeares" \
      "-star-wars-4_871/index.html"
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


datas = extract_one_book(book_url=URL)
print(datas)

datas_list = [datas]

# data extraction path
current_dir = Path.cwd()
print(current_dir.cwd())
path_to_extract_one_product = current_dir / ".." / "extracts" / "extract_one_product"
path_to_extract_one_product.mkdir(exist_ok=True)


# save data to csv file
with open(file=f'{path_to_extract_one_product}/extract.csv', mode='w', encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=LABELS)
    writer.writeheader()
    for elem in datas_list:
        writer.writerow(elem)

print(END_MESSAGE)
