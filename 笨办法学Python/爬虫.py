# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 13:18:58 2018
 
@author: Lenovo
"""
 
# -*- coding: utf-8 -*-
 
import requests
import urllib
import random
from datetime import datetime
# python2 和 python3的兼容代码
try:
    # python2 中
    import cookielib
    print(f"user cookielib in python2.")
except:
    # python3 中
    import http.cookiejar as cookielib
    print(f"user cookielib in python3.")
 
# session代表某一次连接
huihuSession = requests.session()
# 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
huihuSession.cookies = cookielib.LWPCookieJar(filename = "huihuCookies.txt")
 
userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
header = {
    # "origin": "https://passport.huihu.cn",
    "Referer": "https://zabbix.sh.synyi.com/index.php",
    'User-Agent': userAgent,
}
 
def huihuLogin(account, password):
    #
    print ("开始模拟登录嘻嘻嘻")
 
    postUrl = "https://zabbix.sh.synyi.com/index.php"
    postData = {
        "username": account,
        "password": password,
    }
     
    # 使用session直接post请求
    responseRes = huihuSession.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200   
    #responseRes = requests.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print(f"statusCode = {responseRes.status_code}")
    #print(f"text = {responseRes.text}")
    huihuSession.cookies.save()

if __name__ == "__main__":
    # 从返回结果来看，有登录成功
    huihuLogin("Admin", "zabbix")
