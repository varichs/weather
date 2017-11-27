#! /data/python3.6/bin/python3

from bs4 import BeautifulSoup
import requests

url = "https://en.tutiempo.net/climate/01-2016/ws-591340.html"
html = requests.get(url).content
soup = BeautifulSoup(html)

print(soup.decode('utf-8'))