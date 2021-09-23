#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import re


# TODO: Upload file && see source code.
user = "natas15"
passwd = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

viewSourceCode = 'index-source.html'

url = f"http://{user}.natas.labs.overthewire.org/?debug=debug"

data = {"username": "\" admin #"}

response = req.post(url, auth=(user, passwd), data=data)

content = response.text

with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
    print(content, file=f)


# TODO: Get the answer
# answer = re.findall("", content)[0]
# print(answer)
