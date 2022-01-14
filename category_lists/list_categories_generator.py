import requests
from bs4 import BeautifulSoup
import json

URL = "https://books.toscrape.com/"

response = requests.get(url=URL)
response.raise_for_status()

category_dico = {}
category_list = []
if response.status_code == 200:

    # parse the page
    soup = BeautifulSoup(response.content, 'lxml')
    div_categories = soup.find("div", {"class": "side_categories"}).find("li").find_all("li")

    for category in div_categories:
        # Get the category (key) and the associated url (value)
        link_category = category.find("a")
        catego = link_category.get_text().strip().lower()

        url = f"https://books.toscrape.com/{link_category['href']}"

        # dico = {catego: url}

        category_dico[catego] = url
        category_list.append(catego)

print(category_dico)


# Save list of categories
with open(file="dico_category_list.json", mode="w", encoding="utf-8") as json_f:
    json.dump(obj=category_dico, fp=json_f, indent=4, ensure_ascii=True)

# Save dict with list of categories & url
with open(file="category_list.json", mode="w", encoding="utf-8") as json_f:
    json.dump(obj=category_list, fp=json_f, indent=4, ensure_ascii=True)

print("SUCCESS: List & dictionary Correctly Generated")
