# -*- coding: utf-8 -*-
#
import requests
import sys

url = "  "
r = requests.get(url, timeout=5)
code = r.status_code

if code == 200:
    print("页面访问正常")
    #sys.exit()
else:
    print("页面无法访问")
    #sys.exit(2)
