#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import re

user = "natas0"
passwd = user

url = "http://%s.natas.labs.overthewire.org" % user

response = req.get(url, auth=(user, passwd))
content = response.text



# with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
#     print(content, file=f)

# . => 在 default 模式，匹配除了'\n'的任意字符。
# \* => 對它前面的 regular expression 匹配 0 到任意次重復。
answer = re.findall("<!--The password for natas1 is (.*) -->", content)[0]
print(answer)
