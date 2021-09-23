#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import re

from requests.sessions import session

user = "natas5"
passwd = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

url = "http://%s.natas.labs.overthewire.org/" % user

# TODO: 將 loggedin 參數的值改為 1
cookies = {'loggedin': '1'}

# TODO: Session test
# session = req.Session()
# print(session)
# response = session.get(url, auth=(user, passwd))
# content = response.text

# TODO: req.get
response = req.get(url, auth=(user, passwd), cookies=cookies)

# TODO: 看此網站的 cookies
# content = response.cookies

# TODO: .content & .text 差別
# response.content => 直接 output 會是 byte 的格式，較不會出現亂碼
# response.text => 直接輸出會是由 request lib 推測 web page 的編碼去 decode 為 str，較容易出現亂碼
# TODO: for example
# content = response.content.decode('utf-8')
content = response.text

# TODO: get this level password
# . => 在 default 模式，匹配除了'\n'的任意字符。
# \* => 對它前面的 regular expression 匹配 0 到任意次重復。
answer = re.findall("The password for natas6 is(.*)</div>", content)[0]
print(answer)

# TODO: output get content to response.html
# with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
#     print(content, file=f)
