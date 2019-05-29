from pylab import *  # 支持中文
import time
import xlwt
import json


mpl.rcParams['font.sans-serif'] = ['SimHei']

if __name__ == '__main__':
    # 打开名字文件
    name_file = open(r"C:\Users\Administrator\Desktop\任务\names.txt", "r")
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
        with open(r'C:\Users\Administrator\Desktop\任务\{name}.txt'.format(name=temp), 'r') as file:
            file_text = file.read()
            json_text = json.loads(file_text)
            for i in range(len(json_text)):
                time_unix = (json_text[i][0] - json_text[i][0] % 1000)/1000
                time_tuple = time.gmtime(time_unix)  # 返回时间元组
                # 将时间元组转化为字符串
                time_str = time.strftime("%Y%m%d%H%M%S", time_tuple)
                if item == 1:
                    sheet1.write(i+1, item-1, time_str)

                sheet1.write(i+1, item, str((json_text[i][1]-json_text[i][1]%1000000)/1000000))
    book.save(r'C:\Users\Administrator\Desktop\爬虫数据.xlsx')
