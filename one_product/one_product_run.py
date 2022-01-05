import requests
from bs4 import BeautifulSoup
import lxml
import csv
from pathlib import Path

from one_product_functions import extract_td_from_th, number_in_stock, rating

URL = "https://books.toscrape.com/catalogue/william-shakespeares-star-wars-verily-a-new-hope-william-shakespeares" \
      "-star-wars-4_871/index.html"
UPC_TEXT = "UPC"
PRICE_INCLUDING_TAX = "Price (incl. tax)"
PRICE_EXCLUDING_TAX = "Price (excl. tax)"
AVAILABILITY = "Availability"

# Check connection to url
response = requests.get(url=URL)
response.raise_for_status()

# create empty dict
datas = {}

if response.status_code == 200:

    # parse the page
    soup = BeautifulSoup(response.content, 'lxml')

    # product_page_url section
    product_page_url = URL

    # prepare table
    table = soup.find("table", {"class": "table-striped"})
    trs = table.find_all("tr")
    # print(trs)
    for tr in trs:
        th = tr.find("th").get_text()
        td = tr.find("td").get_text()
        print(f"{th}: {td}")

    # upc section, price_including_tax, price_excluding_tax, number_available
    universal_product_code = extract_td_from_th(table=table, caracteristic=UPC_TEXT)
    print(universal_product_code)

    price_including_tax = extract_td_from_th(table=table, caracteristic=PRICE_INCLUDING_TAX)
    print(price_including_tax)

    price_excluding_tax = extract_td_from_th(table=table, caracteristic=PRICE_EXCLUDING_TAX)
    print(price_excluding_tax)

    number_available = number_in_stock(table=table, caracteristic=AVAILABILITY)
    print(f"Number available: {number_available}")

    # title
    title = soup.find("h1").get_text()
    print(f"Title: {title}")

    # product_description
    product_description = soup.find("div", {"id": "product_description"}).findNext('p').get_text()
    print(f"Description: {product_description}")

    # category
    breadcrumb = soup.find("ul", {"class": "breadcrumb"})
    category = breadcrumb.find("li", {"class": "active"}).findPrevious("li").find("a").get_text()
    print(f"Category: {category}")

    # review_rating
    product_main = soup.find("div", {"class": "product_main"})
    str_rating = product_main.find("p", {"class": "star-rating"})["class"][1]
    review_rating = rating(str_rating=str_rating)
    print(f"Review rating: {review_rating}")

    # image_url
    img = soup.find("img")["src"]
    image_url = img.replace("../..", "https://books.toscrape.com")
    print(f"Img: {image_url}")

    datas = {
        "product_page_url": product_page_url,
        "universal_ product_code (upc)": universal_product_code,
        "title": title,
        "price_including_tax": price_including_tax,
        "price_excluding_tax": price_excluding_tax,
        "number_available": number_available,
        "product_description": product_description,
        "category": category,
        "review_rating": review_rating,
        "image_url": image_url
    }

print(datas)

datas_list = [datas]
labels = ["product_page_url",
          "universal_ product_code (upc)",
          "title",
          "price_including_tax",
          "price_excluding_tax",
          "number_available",
          "product_description",
          "category",
          "review_rating",
          "image_url"]

# chemin d'extraction des données
current_dir = Path.cwd()
print(current_dir.cwd())
path_to_extract_one_product = current_dir / ".." / "extracts" / "extract_one_product"
path_to_extract_one_product.mkdir(exist_ok=True)

with open(file=f'{path_to_extract_one_product}/extract.csv', mode='w', encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=labels)
    writer.writeheader()
    for elem in datas_list:
        writer.writerow(elem)
