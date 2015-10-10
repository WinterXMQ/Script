# coding=utf-8
__author__ = 'ming'
from os import system, remove
import time

def sendErrorInfo(content, email = None, tmpfile = 'error.html'):

    # 错误信息写入文本
    content = "Testing ..... \n Error\n" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "\n" + content
    f = file(tmpfile, "w+")
    f.write(content.encode("UTF-8"))
    f.close()
    # Email 列表
    if email is None :
        email = "WinterXMQ@qq.com", "jonathan.swjtu@gmail.com", "15321689@qq.com"
    # 发邮件的信息
    from_name = "Antsoul Test"
    fr = "root@antsoul.com"
    title = "Test Mail"
    subject = "Antsoul Error Report"

    # 发送邮件
    for item in email:
        commend = r'echo -e "To: \"%s\" <%s>\nFrom: \"%s\" <%s>\nSubject: %s\n\n`cat %s`" | /usr/sbin/sendmail -t' %(title, item, from_name, fr, subject, tmpfile)
        print(commend)
        system(commend)
    # remove(tmpfile)

if __name__ == "__main__":
    sendErrorInfo("123123")