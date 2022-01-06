import requests
from bs4 import BeautifulSoup
import json

URL = "https://books.toscrape.com/"

response = requests.get(url=URL)
response.raise_for_status()

dico_category_list = []
category_list = []
if response.status_code == 200:

    # parse the page
    soup = BeautifulSoup(response.content, 'lxml')
    div_categories = soup.find("div", {"class": "side_categories"}).find("li").find_all("li")

    for category in div_categories:
        # Retrieve the category (key) and the associated url (value)
        link_category = category.find("a")
        catego = link_category.get_text().strip()

        url = f"https://books.toscrape.com/{link_category['href']}"

        dico = {catego: url}

        dico_category_list.append(dico)
        category_list.append(catego)

print(dico_category_list)


with open(file="dico_category_list.json", mode="w", encoding="utf-8") as json_f:
    json.dump(obj=dico_category_list, fp=json_f, indent=4, ensure_ascii=True)

with open(file="category_list.json", mode="w", encoding="utf-8") as json_f:
    json.dump(obj=category_list, fp=json_f, indent=4, ensure_ascii=True)

print("SUCCESS: Lists Correctly Generated")
