import json
from pylab import *                          #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

if __name__ == '__main__':
    #打开名字文件
    name_file = open(r"C:\Users\Administrator\Desktop\Python聚类\数据爬取_以文本形式保存\names.txt", "r")
    name_text = name_file.read()
    name_list = name_text.split("\n")  #保存名字到name_list
    name_file.close()

    win = 0
    for temp in name_list:

        flag = 0    #标识变量，防止打开文件出异常
        #依次读取文件夹中各个文本数据
        try:
            file = open(r'C:\Users\Administrator\Desktop\Python聚类\数据爬取_以文本形式保存\{name}.txt'.format(name=temp), 'r')
            flag = 1
        except:
            flag = 0
            continue

        #打开文件正常
        if flag == 1:
            # 创建figure窗口;并设置比例
            plt.figure(temp, figsize=(10, 4))

            file_text = file.read()
            json_text = json.loads(file_text)

            x = []      #保存时间坐标
            y = []      #保存价格坐标
            for i in range(len(json_text)):
                x.append(json_text[i][0])
                y.append(json_text[i][1])

            plt.plot(x, y)
            plt.legend()  # 让图例生效
            plt.title(temp)
            #plt.show()
            plt.savefig(r'C:\Users\Administrator\Desktop\Python聚类\单个图片复原\{imag_name}.png'.format(imag_name=temp))       #保存图片到指定位置
            plt.close()
            file.close()
