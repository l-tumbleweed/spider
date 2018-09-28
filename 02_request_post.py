import requests
import json

sentence = input("请输入需要翻译的语句：")

url = "https://fanyi.baidu.com/basetrans"

query_string = {"query": sentence,
                "from": "zh",
                "to": "en"
                }
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safar"}
response = requests.post(url, data=query_string, headers=headers)

# print(response.content.decode())

html_str = response.content.decode()
dict_ret = json.loads(html_str)

# ret = dict_ret["trans"][0]["dst"]
ret = dict_ret["dict"]["symbols"][0]["parts"][0]["means"][0]
print("the word translate is result: ", ret)

