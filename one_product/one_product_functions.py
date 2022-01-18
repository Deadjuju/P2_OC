import requests
from bs4 import BeautifulSoup
import time

UPC_TEXT = "UPC"
PRICE_INCLUDING_TAX = "Price (incl. tax)"
PRICE_EXCLUDING_TAX = "Price (excl. tax)"
AVAILABILITY = "Availability"


def validate_url():
    """Return the url to scrap after checking it

                Args:
                Returns:
                    url (str): the url to scrap
                """
    while True:
        url = input("Please type the url of the book you want to analyze:\n  --> ")
        if url.startswith("https://books.toscrape.com"):
            response = requests.get(url=url)
            if response.status_code == 200:
                print(f"INFORMATION: -- {url} -- Valid URL. ")
                return url
            else:
                print("\nTrying to connect....")
                time.sleep(1)
                print(f"ERROR: -- {url} -- This url does not work.")
        else:
            if url.startswith("https://"):
                print(f"ERROR: -- {url} -- This url does not link to the site of 'Books to Scrape'.")
            else:
                print(f"ERROR: -- {url} -- is not an url. Please enter an URL.")


def extract_td_from_th(table: BeautifulSoup, caracteristic_name: str):
    """Returns the data from the book characteristics table based on the characteristic name.

            Args:
                table (BeautifulSoup): BeautifulSoup object pointing to the table of characteristics
                caracteristic_name (str): Name of the desired characteristic

            Returns:
                caracteristic (str): the desired caracteristic
            """
    trs = table.find_all("tr")
    for tr in trs:
        th = tr.find("th").get_text()
        td = tr.find("td").get_text()
        if th == caracteristic_name:
            caracteristic = td
            return caracteristic


def number_in_stock(table: BeautifulSoup, caracteristic_name):
    """Returns the quantity of items in stock.

                Args:
                    table (BeautifulSoup): BeautifulSoup object pointing to the table of characteristics
                    caracteristic_name (str): Name of the desired characteristic

                Returns:
                    int: number of items available
                """
    number_available_str = extract_td_from_th(table=table, caracteristic_name=caracteristic_name)
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


def extract_cover(title: str, img_url: str, path_to_extract_images):
    """Extract the cover of a book.

            Args:
                title (str): title of the book
                img_url(str): url of the cover
                path_to_extract_images (WindowsPath): path to save the cover
            """
    # format title
    title = format_text(string_to_format=title)
    # generate img
    with open(f'{path_to_extract_images}\\{title}.jpg', 'wb') as f:
        img = requests.get(img_url)
        f.write(img.content)


def format_text(string_to_format):
    """Remove special characters from a string .

                Args:
                    string_to_format (str): string to format
                Returns:
                    str: formatted string
                """
    special_chars = "?!#$%^&*():'’,.;\"'/ "
    for special_char in special_chars:
        string_to_format = string_to_format.replace(special_char, '_')
    return string_to_format


def extract_cover_choice():
    """Ask the user if he wants to extract the covers.

                Returns:
                    Bool: True if the user wants to extract the images
                """
    choice = input("Do you want to extract book covers?\n"
                   "Type 'Y' for yes.\n"
                   "|| --> ").lower()
    if choice == "yes" or choice == "y" or choice == "oui":
        return True
    else:
        return False


def extract_one_book(book_url: str, cover=False, img_path=None):
    """Extract data from a work.

            Args:
                book_url (str): URL to scrape
                cover(bool): True to extract cover
                img_path(): Path to extract img

            Returns:
                dic: dictionary containing the desired data
            """

    # Connect to the site and if all goes well (response 200) we continue
    response = requests.get(url=book_url)
    response.raise_for_status()

    if response.status_code == 200:

        # parse the page
        soup = BeautifulSoup(response.content, 'lxml')
        # product_page_url section
        product_page_url = book_url
        # prepare table
        table = soup.find("table", {"class": "table-striped"})

        # upc section, price_including_tax, price_excluding_tax, number_available
        universal_product_code = extract_td_from_th(table=table, caracteristic_name=UPC_TEXT)
        price_including_tax = extract_td_from_th(table=table, caracteristic_name=PRICE_INCLUDING_TAX)
        price_excluding_tax = extract_td_from_th(table=table, caracteristic_name=PRICE_EXCLUDING_TAX)
        number_available = number_in_stock(table=table, caracteristic_name=AVAILABILITY)

        # title
        title = soup.find("h1").get_text()
        # print(f"Title: {title}")

        # product_description
        try:
            product_description = soup.find("div", {"id": "product_description"}).findNext('p').get_text()
        except AttributeError:
            product_description = "- NO DESCRIPTION -"

        # category
        breadcrumb = soup.find("ul", {"class": "breadcrumb"})
        category = breadcrumb.find("li", {"class": "active"}).findPrevious("li").find("a").get_text()

        # review_rating
        product_main = soup.find("div", {"class": "product_main"})
        str_rating = product_main.find("p", {"class": "star-rating"})["class"][1]
        review_rating = rating(str_rating=str_rating)

        # image_url
        img = soup.find("img")["src"]
        image_url = img.replace("../..", "https://books.toscrape.com")

        if cover:
            extract_cover(title=title, img_url=image_url, path_to_extract_images=img_path)

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
