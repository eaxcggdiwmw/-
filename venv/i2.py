from http import cookiejar
import urllib.request

print
"第二种方法"
request = urllib.request.Request(url)
# 模拟Mozilla浏览器进行爬虫
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib.request(request)
print
response2
print
len(response2.read())


