# coding = utf-8
from parse import parse_url
import json

class DoubanSpider:
    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_movie_score_hot/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=0"

    def get_content_list(self, html_str):  # 提取数据
        dict_data = json.loads(html_str)
        content_list = dict_data["subject_collection_items"]
        total = dict_data["total"]
        return content_list, total

    def save_content_list(self, content_list):
        number = 0
        with open("douban1.json", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
                number += 1
        print("succeed save >>", number)

    def run(self):
        num = 0
        total = 100
        while num < total + 18:
            # 1.start_url
            url = self.temp_url.format(num)
            print(url)
            # 2.发送请求，获取响应
            html_str = parse_url(url)
            # 3.提起数据
            content_list, total = self.get_content_list(html_str)
            # 4.保存
            self.save_content_list(content_list)
            # 5.构造下一页的url地址
            num += 18
            # start_url = self.temp_url.format(num)
            # html_str = parse_url(start_url)
            # content_list = self.get_content_list(html_str)
            # self.save_content_list(content_list)

if __name__ == "__main__":
    douban = DoubanSpider()
    douban.run()
