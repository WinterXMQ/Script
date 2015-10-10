# coding=utf-8
###该脚本用于测试蚂蚁pt是否正常工作###
import urllib2
import urllib
from os import system
import SendMail
import cookielib
import re

def testError(content):
    """
    测试错误信息
    :param content: bool, True -> Error; False -> No Error
    """
    rp = re.compile("Memcache"), re.compile("MySql Error")
    for pt in rp:
        rs = pt.findall(content)
        if rs:
            return True
        else:
            return False

def dealError(content):
    print('Server Error')
    SendMail.sendErrorInfo(res)                             # 发送错误数据

# def Init():
#     cj = cookielib.CookieJar()
#     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#     urllib2.install_opener(opener)
url="https://pt.antsoul.com/login.php"
try:
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11' }
    req = urllib2.Request(url, headers = headers)
    res = urllib2.urlopen(req).read().decode("UTF-8")           # 返回的数据内容
    # print(res.encode("UTF-8"))
   
    if not testError(res):                                          # 处理错误
        dealError(res)
    else:
        print("OK!")

except urllib2.URLError as e:
    print ("URL ERROR\n")
    print (e.reason)
except urllib2.HTTPError as e:
    print ("HTTP ERROR")
    print (e.reason)

