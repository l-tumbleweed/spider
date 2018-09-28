import requests

url = "https://m.weibo.cn/"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
"Cookie": "SUB=_2A252qOAhDeRhGeRG41UR9SrJzjuIHXVSUoBprDV6PUJbkdAKLUbAkW1NTenqgUbqs9eZRfAXAt7aIABfZ9JoEVao; SUHB=0h15UTnvGzr0sx; SCF=AuIEx7TnekXHYrehb64h_sVrZwtsdfOzNZH4OImAYBt229KO30chj_juX0f_meiQlUdiWNCFi_18fH1zfrtKdt4.; SSOLoginState=1538035826"}

response = requests.get(url, headers=headers)

with open("profile1.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode())

# 获取登录 post 请求的地址
# 进入登录页面 >> 清空 network >> tick hte Preserve log >> click login button
