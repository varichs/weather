#! /data/python3.6/bin/python3

from bs4 import BeautifulSoup
import requests
import csv


def csv_writer(csv_data, csv_name, csv_path):
    field = ['Day', 'T', 'TM', 'Tm', 'SLP', 'H', 'PP', 'VV', 'V', 'VM', 'VG', 'RA', 'SN', 'TS', 'FG']
    with open(csv_path + '/' + csv_name, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = field)
        writer.writeheader()
            
        writer.writerows(csv_data)


url = "https://en.tutiempo.net/climate/01-2016/ws-591340.html"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
data = soup.find("table", "medias mensuales")
rows = data.find_all("tr")
field = ['Day', 'T', 'TM', 'Tm', 'SLP', 'H', 'PP', 'VV', 'V', 'VM', 'VG', 'RA', 'SN', 'TS', 'FG']

data = []
for row in rows:
    dataTmp = []
    for column in row:
        #print(column)
        dataTmp.append(column.text)
        #print("\n")#
    #break
    dictData = dict(zip(field, dataTmp))
    data.append(dictData)

csv_writer(data, 'test', './')

#print(dataTmp)
'''
保存数据到csv文件
'''

