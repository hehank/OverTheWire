#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import re
import base64
from urllib import parse


user = "natas11"
passwd = "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"

viewSourceCode = 'index-source.html'

cookies = {'data': 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'}

url = f"http://{user}.natas.labs.overthewire.org/"

response = req.get(url, auth=(user, passwd), cookies=cookies)

# TODO: Get cookies
# unquote => decode url encoded
# content = parse.unquote(response.cookies["data"])

# TODO: Get the answer
content = response.text
answer = re.findall("The password for natas12 is (.*)<br>", content)[0]
print(answer)

# with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
#     print(content, file=f)
