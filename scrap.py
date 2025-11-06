import requests

from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

for i in range(len(quotes)):
    print(quotes[i].text, "-", authors[i].text)
