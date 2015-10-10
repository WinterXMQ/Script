# coding=utf-8
__author__ = 'ming'
from os import system, remove

def sendErrorInfo(content, email = "WinterXMQ@qq.com", tmpfile = '/tmp/error-html'):
    content = "Errorpacmsn\n" + content
    f = file(tmpfile, "w+")
    f.write(content)
    f.close()
    print('cat %s | mail -s "Antsoul-Error" %s' % (tmpfile, email))
    system('cat %s | mail -s "Antsoul-Error" %s' % (tmpfile, email))
    # remove(tmpfile)

sendErrorInfo("123123")