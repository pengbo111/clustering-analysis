from pylab import *  # 支持中文
import time
import xlwt
import json
import matplotlib.pyplot as plt
import xlsxwriter
import pandas as pd

mpl.rcParams['font.sans-serif'] = ['SimHei']

if __name__ == '__main__':
    # 打开名字文件
    name_file = open(r"C:\Users\Administrator\Desktop\Python聚类\数据爬取_以文本形式保存\names.txt", "r")
    name_text = name_file.read()
    name_list = name_text.split("\n")  # 保存名字到name_list
    name_file.close()

    item = 0

    book = xlwt.Workbook()      #新建工作簿
    sheet1 = book.add_sheet("sheet1")        #新建工作表
    sheet1.write(0, 0, r"时间\名称")        #保存表头为时间
    for temp in name_list:
        if(temp==""):
            break;
        item = item+1
        #依次读取文件夹中各个文本数据
        sheet1.write(0, item, temp)
        print(temp)
        with open(r'C:\Users\Administrator\Desktop\Python聚类\数据爬取_以文本形式保存\{name}.txt'.format(name=temp), 'r') as file:
            file_text = file.read()
            json_text = json.loads(file_text)
            #x = []  # 保存时间坐标
            #y = []  # 保存价格坐标
            for i in range(len(json_text)):

                if item == 1:
                    sheet1.write(i+1, item-1, json_text[i][0])
                #x.append(time_str)
                #y.append(json_text[i][1])
                sheet1.write(i+1, item, json_text[i][1])
    book.save(r'C:\Users\Administrator\Desktop\Python聚类\数据_以Excel保存.xls')
