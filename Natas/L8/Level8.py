#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import L8_decode
import re
import requests as req

user = "natas8"
passwd = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"

# TODO: 抓取 Source code & decode text
# ViewSourceCode = "index-source.html"

# url = f"http://{user}.natas.labs.overthewire.org/{ViewSourceCode}"

# response = req.get(url, auth=(user, passwd))
# content = response.text

# with open("Natas/response.html", "w") as f:
#     print(content, file=f)

cipher = "3d3d516343746d4d6d6c315669563362"
cheaperText = L8_decode.decodeSecret(cipher)

# TODO: 使用 POST method 取得 Flag

url = f"http://{user}.natas.labs.overthewire.org/"

data = {'secret': cheaperText, 'submit': 'submit'}

response = req.post(url, auth=(user, passwd), data=data)
content = response.text

# with open("Natas/response.html", "w") as f:
#     print(content, file=f)

answer = re.findall(
    "Access granted. The password for natas9 is (.*)\n", content)[0]
print(answer)
