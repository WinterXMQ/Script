###该脚本用于测试蚂蚁pt是否正常工作###

import urllib.request as request
from os import system  
import re

url="http://pt.antsoul.com/index.php"
try:
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener = request.build_opener()
    opener.addheaders = [headers]
    response = opener.open(url).read().decode("utf8")
    result = re.findall(r'Magi Madoka Magica',response)
   # print(response)
   
    if result:
       # print(result)
        print("It's Ok")
    else:
        print('Server Error')
       # system('reboot')
except request.URLError as e:
    print ("URL ERROR\n")
    print (e.reason)
   # system('reboot')
except request.HTTPError as e:
    print ("HTTP ERROR")
    print (e.reason)
   # system('reboot')

