#! /data/python3.6/bin/python3

from bs4 import BeautifulSoup
import requests

url = "https://en.tutiempo.net/climate/01-2016/ws-591340.html"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
data = soup.find("table", "medias mensuales")
rows = data.find_all("tr")
for row in rowa.find_all("td")
    print(row.text)

print(rows)