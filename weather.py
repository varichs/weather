#! /data/python3.6/bin/python3

from bs4 import BeautifulSoup
import requests
import csv

'''
保存数据到csv文件
'''
def csv_writer(csv_data, csv_name, csv_path):
    field = ['Day', 'T', 'TM', 'Tm', 'SLP', 'H', 'PP', 'VV', 'V', 'VM', 'VG', 'RA', 'SN', 'TS', 'FG']
    with open(csv_path + '/' + csv_name, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = field)
        writer.writeheader()
            
        writer.writerows(csv_data)

def get_url(year, month, zone_code = '591340'):
    base_url = "https://en.tutiempo.net/climate/"

    url = base_url + month + '-' + year + '/ws-' + zone_code + '.html'
    return url
    

url = "https://en.tutiempo.net/climate/01-2016/ws-591340.html"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
data = soup.find("table", "medias mensuales")
rows = data.find_all("tr")
field = ['Day', 'T', 'TM', 'Tm', 'SLP', 'H', 'PP', 'VV', 'V', 'VM', 'VG', 'RA', 'SN', 'TS', 'FG']

# print(get_url('2017', '02'))

data = []
# dateRange = list(range(1, 32))
dateRange = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
 '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
for row in rows:
    if row.contents[0].text not in dateRange:
        # print(row.contents[0].text)
        continue
    dataTmp = []
    for column in row:
        # print(column)
        dataTmp.append(column.text)
        #print("\n")#
    #break
    dictData = dict(zip(field, dataTmp))
    data.append(dictData)

csv_writer(data, 'test.csv', './')
# print(data)
#print(dataTmp)


