import csv
from pathlib import Path
import time

from one_product_functions import extract_one_book, validate_url, format_text, extract_cover_choice


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


# type a correct url
url = validate_url()

start = time.time()


# data extraction path
current_dir = Path.cwd()
path_to_extract = current_dir / ".." / "extracts"
path_to_extract.mkdir(exist_ok=True)
path_to_extract_one_product = path_to_extract / "extract_one_product"
path_to_extract_one_product.mkdir(exist_ok=True)


# Extract cover True or False
cover = extract_cover_choice()


# Extract data
datas = extract_one_book(book_url=url, cover=cover, img_path=path_to_extract_one_product)


# Format title
title = datas["title"]
formatted_title = format_text(string_to_format=title)
file_name = f"{formatted_title}_extract"


# save data to csv file
with open(file=f'{path_to_extract_one_product}/{file_name}.csv',
          mode='w',
          encoding="utf-8",
          newline="") as f:
    writer = csv.DictWriter(f, fieldnames=LABELS)
    writer.writeheader()
    writer.writerow(datas)

print(f"END_MESSAGE -> {datas['title']}")

end = time.time()
print(end - start)
