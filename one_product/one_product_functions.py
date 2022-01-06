import requests
from bs4 import BeautifulSoup

UPC_TEXT = "UPC"
PRICE_INCLUDING_TAX = "Price (incl. tax)"
PRICE_EXCLUDING_TAX = "Price (excl. tax)"
AVAILABILITY = "Availability"


def extract_td_from_th(table, caracteristic: str):
    trs = table.find_all("tr")
    for tr in trs:
        th = tr.find("th").get_text()
        td = tr.find("td").get_text()
        # print(f"{th}: {td}")
        if th == caracteristic:
            product_page_url = td
            return product_page_url


def number_in_stock(table, caracteristic):
    number_available_str = extract_td_from_th(table=table, caracteristic=caracteristic)
    if number_available_str.startswith("In stock"):
        number_available = int(number_available_str.split("In stock (")[1].split(" available)")[0])
        return number_available
    else:
        return 0


def rating(str_rating: str):
    """Convert rating str in int

        Args:
            str_rating (str): Rating in strings

        Returns:
            int: Rating in int
        """
    if str_rating == "One":
        return 1
    elif str_rating == "Two":
        return 2
    elif str_rating == "Three":
        return 3
    elif str_rating == "Four":
        return 4
    elif str_rating == "Five":
        return 5


def extract_one_book(book_url: str):
    response = requests.get(url=book_url)
    response.raise_for_status()

    if response.status_code == 200:

        # parse the page
        soup = BeautifulSoup(response.content, 'lxml')

        # product_page_url section
        product_page_url = book_url

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

        return {
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
