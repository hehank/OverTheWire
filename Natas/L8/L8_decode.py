#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import base64


def decodeSecret(secret):
    # hex => text
    cheapText = (bytes.fromhex(secret)).decode('utf-8')
    # string reverse
    cheapText = cheapText[::-1]
    # base64 decode
    cheapText = base64.b64decode(cheapText).decode('utf-8')
    return cheapText


if __name__ == "__main__":
    # test
    cipher = decodeSecret('3d3d516343746d4d6d6c315669563362')
    print(cipher)
