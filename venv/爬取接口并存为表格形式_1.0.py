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
    fp2 = open('detail.xls', 'w', encoding='utf-8')
    for n in list1:
        detail = response_json["paths"][n]
        key1 = "get"
        key2 = "post"
        key3 = "put"
        key4 = "delete"
        if key1 in detail:
            fp2.write("GET:")
            fp2.write(n)
            fp2.write('\n')
            fp2.write('摘要:')
            json.dump(detail[key1]['summary'], fp2, ensure_ascii=False)
            fp2.write('\n')
            fp2.write('参数:')
            json.dump(detail[key1]['parameters'], fp2, ensure_ascii=False)
            fp2.write('\n')
            fp2.write('响应:')
            json.dump(detail[key1]['responses'], fp2, ensure_ascii=False)
            fp2.write('\n')
        if key2 in detail:
            fp2.write("POST:")
            fp2.write(n)
            fp2.write('\n')
            fp2.write('摘要:')
            json.dump(detail[key2]['summary'], fp2, ensure_ascii=False)
            fp2.write('\n')
            fp2.write('参数:')
            json.dump(detail[key2]['parameters'], fp2, ensure_ascii=False)
            fp2.write('\n')
            fp2.write('响应:')
            json.dump(detail[key2]['responses'], fp2, ensure_ascii=False)
            fp2.write('\n')
        if key3 in detail:
            fp2.write("PUT:")
            fp2.write(n)
            fp2.write('\n')
            fp2.write('摘要:')
            json.dump(detail[key3]['summary'], fp2, ensure_ascii=False)
            fp2.write('\n')
            fp2.write('参数:')
            json.dump(detail[key3]['parameters'], fp2, ensure_ascii=False)
            fp2.write('\n')
            fp2.write('响应:')
            json.dump(detail[key3]['responses'], fp2, ensure_ascii=False)
            fp2.write('\n')
        if key4 in detail:
            fp2.write("DELETE:")
            fp2.write(n)
            fp2.write('\n')
            fp2.write('摘要:')
            json.dump(detail[key4]['summary'], fp2, ensure_ascii=False)
            fp2.write('\n')
            fp2.write('参数:')
            json.dump(detail[key4]['parameters'], fp2, ensure_ascii=False)
            fp2.write('\n')
            fp2.write('响应:')
            json.dump(detail[key4]['responses'], fp2, ensure_ascii=False)
            fp2.write('\n')
        fp2.write('\n')
    fp2.close()

