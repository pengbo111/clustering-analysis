import requests
from lxml import etree
import json


# 输入一个url，返回一个response
def GetResponse(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
    }
    session = requests.session()
    session.post(url, headers=headers)
    response = session.get(url, headers=headers)
    return response.text


# 输入一个response返回一个HTML对象
def GetHTML(str):
    return etree.HTML(str)


# 输入HTML对象，返回指定信息
def GetMessage(html, xpath_str):
    html_message = html.xpath(xpath_str)
    return html_message


if __name__ == '__main__':

    # 主页面HTML获取
    response_sum = GetResponse("https://coinmarketcap.com/")
    html_sum = GetHTML(response_sum)

    # 获取各个图片的名称'
    imag_name = GetMessage(html_sum, '//span[@class="hidden-xs"]/text()')

    # 获取各个图片的连接
    imag_link = GetMessage(html_sum, '//a[@class="volume"]/@href')

    sub_imag_link = []

    for i in imag_link:
        subsection = i.split('/')  # 划分imag
        imag_web = "https://graphs2.coinmarketcap.com/{}/{}/1514739661000/1517418061000".format(subsection[1], subsection[2])
                                                    # 2018.1.1.1.1.1  -  2018.2.1.1.1.1
        sub_imag_link.append(imag_web)

    i = -1
    j = 0

    for e in sub_imag_link:
        i = i + 1

        response_sub = GetResponse(e)
        try:
            json_style = json.loads(response_sub)
            json_style_message = json_style['market_cap_by_available_supply']
            j = j+1
        except:
            continue
        with open(r"C:\Users\Administrator\Desktop\Python聚类\数据爬取_以文本形式保存\{num}.{name}.txt".format(num=j, name=imag_name[i]), 'a') as file:
            file.write(json.dumps(json_style_message))
            print("ok {0}  {1}".format(j,imag_name[i]))
            print("*****************************************************")
            with open(r"C:\Users\Administrator\Desktop\Python聚类\数据爬取_以文本形式保存\{name}.txt".format(name="names"), 'a') as file_name:
                file_name.write("{}".format(j)+"."+imag_name[i] + "\n")
