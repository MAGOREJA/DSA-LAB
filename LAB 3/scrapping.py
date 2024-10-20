from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time as sleep


service = Service(
    executable_path="D:/chromedriver-win64/chromedriver.exe"
)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

products = []  # List to store name of the product
prices = []  # List to store price of the product
description = []  # List to store description of the product

driver.get("https://www.elo.shopping/collections/men")

content = driver.page_source

soup = BeautifulSoup(content, features="html.parser")
# print(soup)
for a in soup.findAll("li", attrs={"class": "grid__item"}):
    # print(a)
    name = a.find("div", attrs={"class": "card__information"})
    price = a.find("div", attrs={"class": "price "})
    description = a.find("div", attrs={"class": "card-information"})
    if name != None and price != None and description != None:
        products.append(name["title"])
        prices.append(price.text)
        description.append(price.text)
    if len(products) == 50:
        break

df = pd.DataFrame({"Product Name": products, "Price": prices, "Description": description})
df.to_csv("dayta.csv", index=False, encoding="utf-8")