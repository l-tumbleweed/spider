import requests
import json

# drop &callback=jsonp1
url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_movie_score_hot/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=1538042663900"

headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
           "Referer": "https://m.douban.com/movie/doubantop"}

response = requests.get(url, headers=headers)

print(response.content.decode())
# json_str = response.content.decode()
#
# ret1 = json.loads(json_str)
# print(ret1)

# with open("douban.json", "w", encoding="utf-8") as f:
#     f.write(json.dumps(ret1, ensure_ascii=False, indent=2))

# network >> filter 中可以过滤 url
