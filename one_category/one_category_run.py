from list_urls_book_one_category import get_urls_book_category


URL_CATEGORY = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

url_book_final = get_urls_book_category(url=URL_CATEGORY)

print(url_book_final)

