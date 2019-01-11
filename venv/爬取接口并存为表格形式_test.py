from bs4 import BeautifulSoup
import requests
import json


if __name__ == '__main__':
    url = 'http://192.168.0.58:9207/v2/api-docs'
    response = requests.get(url=url)
    html = response.text
    # print(response.json())
    response_json = response.json()
    response_str = json.dumps(response_json)
    print(response_json.keys())
    # print(response_json["paths"])
    paths = response_json["paths"]
    # 获取接口名称
    list1 = []
    fp1 = open('path.txt', 'w')
    for i in paths:
        list1.append(i)
    for j in list1:
        fp1.write(j)
        fp1.write('\n')
    fp1.close()
    # 获取接口内容
    fp2 = open('detail1.xls', 'w', encoding='utf-8')
    for n in list1:
        detail = response_json["paths"][n]
        print(detail["get"]["tags"])
        fp2.write('\n')
    fp2.close()

