import xlrd
import json
from pylab import *                          #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
import numpy as np
import pandas as pd

if __name__ == '__main__':
    #打开名字文件
    workbook = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\Python聚类\数据_以Excel保存_横向.xlsx')
    table = workbook.sheet_by_index(0)

    # 获取行数
    nrows = table.nrows
    # 获取列数
    ncols = table.ncols

    #获取x轴坐标值
    x_axis = table.row_values(0)

    # 获取各行数据
    row_list = []
    for i in range(1, nrows):
        row_data = table.row_values(i)
        row_list.append(row_data)


    for cla in range(0,6):

        y_axis = []

        for i in range(0, nrows-1):
            if (row_list[i][746] == cla):
                y_axis.append(row_list[i])

        # 创建Figure
        #fig = plt.figure()
        # 创建figure窗口;并设置比例
        fig = plt.figure('第{}类'.format(cla), figsize=(20,10))

        for j in range(0, len(y_axis)):
            #z = round(np.sqrt(j+1))
            # 创建一个或多个子图(subplot绘图区才能绘图)
            y_axis[j][0] = fig.add_subplot(6,6 ,j+1)

            plt.plot(x_axis[1:746], y_axis[j][1:746])  # 绘图及选择子图746
            plt.sca(y_axis[j][0])
        #图片保存
        plt.savefig(r'C:\Users\Administrator\Desktop\Python聚类\聚类整合图片\第{temp}组.png'.format(temp=cla))  # 保存图片到指定位置
        plt.close()
