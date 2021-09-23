#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import json

# ? cheapText ^ key = ciphertext
# ? => cheapText ^ ciphertext = key


def xor_encrypt(inp, key):
    text = inp
    outText = ''

    for i in range(len(text)):
        s = chr(ord(text[i]) ^ ord(key[i % len(key)]))
        outText += s
    return outText


def get_xor_encrypt_key(cipherText, defaultdata):
    key = ''
    repeat_key = xor_encrypt(cipherText, defaultdata)

    for i in repeat_key:
        if i in key:
            break
        key += i

    return key


def key_test(cipherText, defaultdata):
    key = get_xor_encrypt_key(cipherText, defaultdata)
    cheapText = xor_encrypt(cipherText, key)
    if cheapText == defaultdata:
        return True
    else:
        return False


# TODO: Get xor_encrypt() key
encrypt_cipher = base64.b64decode(
    "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=").decode('utf-8')
# ! 因為我的VSCode會在我存檔的時候自動排版，會多加了空格，所以用.replace()把空格去掉
# ? .dumps() => 將 Python 對象編碼成 JSON 字符串
defaultdata = json.dumps(
    {"showpassword": "no", "bgcolor": "#ffffff"}).replace(' ', '')

if (key_test):
    key = get_xor_encrypt_key(encrypt_cipher, defaultdata)
else:
    assert "The key is not currect!!!"


# TODO: Encrypt cheapText to ciphertext
cheapText = json.dumps(
    {"showpassword": "yes", "bgcolor": "#ffffff"}).replace(' ', '')
encrypt = xor_encrypt(cheapText, key).encode('utf-8')
cipherText = base64.b64encode(encrypt).decode('utf-8')
print(cipherText)
