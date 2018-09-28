import requests

url = "http://wwww.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

response = requests.get(url, headers=headers)

# print(response)
# response.encoding = "utf-8"
# print(response.text)

# print(response.content)
# print(response.content.decode())

# print(response.url)
# print(response.headers)

# print(response.request.url)
print(response.request.headers)
