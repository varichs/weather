import matplotlib.pyplot as plt
import csv

file = './final.csv'
x = []
y = []
j = int(0)
years = {"2010":[],"2011":[],"2012":[],"2013":[],"2014":[],"2015":[],"2016":[],"2017":[]}
date = []

with open(file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for i in reader:
        if j == 0:
            j = j + 1
            continue
        yearIndex = int(i[1])
        # years[yearIndex].append(i[3])
        date_d = i[2] + '-' + i[4]
        if date.count(date_d) < 1:
            date.append(date_d)
        # x.append(i[0])
        # y.append(i[3])
# for year in years:    
#     plt.plot(date, year, label = 'ssd', lineWidth = 3, color = 'r', marker = 'o', markerfacecolor = 'blue', markersize = 12)

# plt.xlabel('日期')
# plt.ylabel('SSD')
# plt.title("厦门五年内舒适度")
# plt.legend()
# plt.show()
print(date)
