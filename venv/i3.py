from http import cookiejar
import urllib.request

print
"第三种方法"

cookie = cookielib.CookieJar()
# 加入urllib2处理cookie的能力
opener = urllib.build_opener(urllib.HTTPCookieProcessor(cookie))
urllib.install_opener(opener)
response3 = urllib.request(url)
print
response3.getcode()
print
len(response3.read())
print
cookie

