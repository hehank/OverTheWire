#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import re

user = "natas6"
passwd = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

url = "http://%s.natas.labs.overthewire.org/" % user

# 使用 ppst method 時要加入的變數
data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit": "submit"}

# post method
response = req.post(url, data=data, auth=(user, passwd))
content = response.text

# with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
#     print(content, file=f)

# . => 在 default 模式，匹配除了'\n'的任意字符。
# \* => 對它前面的 regular expression 匹配 0 到任意次重復。
answer = re.findall(
    "Access granted. The password for natas7 is (.*)", content)[0]
print(answer)
