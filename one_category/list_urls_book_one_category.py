import requests
from bs4 import BeautifulSoup
import lxml


def get_urls_book_category_first_page(url_category):
    """Extract urls's book from 1st page for one category.

                Args:
                    url_category (str): URL to scrape

                Returns:
                    list: urls of all books on the page
                """
    print("INFORMATION: Start loading book urls _ _ _ ")
    response = requests.get(url=url_category)
    response.raise_for_status()

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")

        # target the div with the set of books
        div_books = soup.find("div", {"class": "col-sm-8 col-md-9"})
        # print(div_books)
        h3s = div_books.find_all("h3")

        # Get urls
        url_list = []
        for h3 in h3s:
            url_book = h3.find("a")["href"].replace("../../..", "https://books.toscrape.com/catalogue")
            url_list.append(url_book)

        return url_list


def get_urls_book_category(url_to_scrap: str):
    """Extract all urls from all books for a single category.

                Args:
                    url_to_scrap (str): URL to scrape

                Returns:
                    list: List of urls
                """
    # Store the category url, minus the ending ("index.html")
    url_to_scrap_without_index = url_to_scrap.split("index.html")[0]

    # Get the urls of the first page for each book
    url_list = get_urls_book_category_first_page(url_category=url_to_scrap)

    # Check for the existence of a "next" button
    i = 1
    while True:
        print(f"Page {i}")
        response = requests.get(url=url_to_scrap)
        response.raise_for_status()
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "lxml")

            # get url from the next page
            next_class = soup.find("li", {"class": "next"})
            if next_class is not None:
                new_url = next_class.find("a")["href"]
                if i == 1:
                    # end of url == index.html
                    url_to_scrap = url_to_scrap.replace("index.html", new_url)
                    i += 1
                else:
                    url_to_scrap = f"{url_to_scrap_without_index}{new_url}"
                    i += 1

                # Get the others book urls
                url_list += get_urls_book_category_first_page(url_category=url_to_scrap)
            else:
                print("INFORMATION: No more urls to extract!\nGenerate the list...")
                break

    print(f"Number of Url: {len(url_list)}.")

    return url_list


