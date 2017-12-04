#! /data/python3.6/bin/python3

from bs4 import BeautifulSoup
import requests
import csv
import time

'''
计算人体舒适度指数，t温度，f湿度， v风速
'''
def cal_ssd(t, f, v):
    tmp = (1.818 * t + 18.18) * (0.88 + 0.002 * f) + (t - 32) / (45 - t) - 3.2 * v + 18.2
    
    return tmp

'''
生成文件名
'''
def generate_file_name(year, month):
    file_name = './' + year + '-' + month + '.csv'
    return file_name
'''
保存数据到csv文件
'''
def csv_writer(csv_data, csv_name):
    field = ['Day', 'T', 'TM', 'Tm', 'SLP', 'H', 'PP', 'VV', 'V', 'VM', 'VG', 'RA', 'SN', 'TS', 'FG']
    with open(csv_name, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = field)
        writer.writeheader()
            
        writer.writerows(csv_data)
'''
获取某年某月，某地区的天气链接
'''
def get_url(year, month, zone_code = '591340'):
    base_url = "https://en.tutiempo.net/climate/"

    url = base_url + month + '-' + year + '/ws-' + zone_code + '.html'
    return url
'''
延迟函数，避免频繁请求
'''
def delay_sleep(sec = 30):
    time.sleep(sec)
'''
获取某年某月的数据
'''
def get_data(year, month):
    file_name = generate_file_name(year, month)
    url = get_url(year, month)
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    data = soup.find("table", "medias mensuales")
    rows = data.find_all("tr")
    field = ['Day', 'T', 'TM', 'Tm', 'SLP', 'H', 'PP', 'VV', 'V', 'VM', 'VG', 'RA', 'SN', 'TS', 'FG']
    data = []
    # dateRange = list(str(range(1, 32)))
    dateRange = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

    for row in rows:
        if row.contents[0].text not in dateRange:    
            continue
        dataTmp = []
        for column in row:            
            dataTmp.append(column.text)        
        dictData = dict(zip(field, dataTmp))
        data.append(dictData)

    csv_writer(data, file_name)


years = ['2017']
# month = [str(i) for i in range(1, 13)]
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']

for year in years:
    for month in months:
        get_data(year, month)
        delay_sleep()
        print(year + '-' + month)
        print('\n')

# url = "https://en.tutiempo.net/climate/01-2016/ws-591340.html"
# html = requests.get(url).content
# soup = BeautifulSoup(html, "html.parser")
# data = soup.find("table", "medias mensuales")
# rows = data.find_all("tr")
# field = ['Day', 'T', 'TM', 'Tm', 'SLP', 'H', 'PP', 'VV', 'V', 'VM', 'VG', 'RA', 'SN', 'TS', 'FG']

# # print(get_url('2017', '02'))

# data = []
# # dateRange = list(str(range(1, 32)))
# dateRange = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
#  '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
#  '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

# for row in rows:
#     if row.contents[0].text not in dateRange:
    
#         continue
#     dataTmp = []
#     for column in row:
        
#         dataTmp.append(column.text)
       
#     dictData = dict(zip(field, dataTmp))
#     data.append(dictData)

# csv_writer(data, 'test.csv', './')



