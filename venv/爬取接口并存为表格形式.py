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
    list2 = []
    fp2 = open('detail.xls', 'w', encoding='utf-8')
    for n in list1:
        detail = response_json["paths"][n]
        list2.append(detail)
        print(response_json["paths"][n])
        fp2.write(n)
        fp2.write(':')
        fp2.write('\n')
        json.dump(detail, fp2, ensure_ascii=False)
        fp2.write('\n')
    fp2.close()

