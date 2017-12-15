import glob
import os
import csv

def all_files(pattern, search_path, pathsep = os.pathsep): 
  for path in search_path.split(pathsep): 
    for match in glob.glob(os.path.join(path, pattern)): 
      yield match 

def cal_ssd(t, f, v):
    try:
      # pass
      t = float(t)
      f = float(f)
      v = float(v)
    except:
      # pass
      t = 0
      f = 0
      v = 0
    return (1.818 * t + 18.18) * (0.88 + 0.002 * f) + (t - 32) / (45 - t) - 3.2 * v + 18.2
'''
保存数据到csv文件
'''
def csv_writer(csv_data, csv_name):
    field = ['Ymd', 'Year', 'Month','SSD', 'Day', 'T', 'TM', 'Tm', 'SLP', 'H', 'PP', 'VV', 'V', 'VM', 'VG', 'RA', 'SN', 'TS', 'FG']
    with open(csv_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = field)
        writer.writeheader()            
        writer.writerows(csv_data)
# print(type(all_files('*.csv', './')))      
# print(all_files('*.csv', './').__next__()) 
field = ['Ymd', 'Year', 'Month','SSD', 'Day', 'T', 'TM', 'Tm', 'SLP', 'H', 'PP', 'VV', 'V', 'VM', 'VG', 'RA', 'SN', 'TS', 'FG']
dateDict = []
for match in all_files('*.csv', './'):   
  # print(match)
  # print(match[2:-4])
  #年份与月份的字符串
  date_year_month = match[2:-4]
  year_month = date_year_month.split("-")
  # print(year_month)
  year = year_month[0]
  month = year_month[1]
  
  with open(match, 'r') as csv_file:
    reader = csv.reader(csv_file)
    j = int(0)
    
    for i in reader:
      if j == 0:
        j = j + 1
        continue
      date = []
      y_m_d = year + '-' + month + '-' + i[0]      
      date.append(y_m_d)
      date.append(year)
      date.append(month)      
      date.append(cal_ssd(i[1], i[5], i[8]))
      date.extend(i) 
      
      dateDict.append(dict(zip(field, date)))
     
# print(dateDict)
csv_writer(dateDict, 'final.csv')
      