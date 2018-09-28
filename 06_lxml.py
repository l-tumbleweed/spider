from lxml import etree
import requests

url = "https://music.douban.com/chart"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

response = requests.get(url, headers=headers)

html_str = response.content.decode()

# print(html_str)

html = etree.HTML(html_str)
# print(html)

# url_list = html.xpath("//ul[@class='col5']/li/a/@href")
# print(url_list)

# img_list = html.xpath("//ul[@class='col5']/li/a/img/@src")
# print(img_list)

retl = html.xpath("//ul[@class='col5']/li")
# print(retl)

for div in retl:
    item = {}
    if len(div.xpath(".//div/h3/a/text()")) == 0 and len(div.xpath(".//a[@class='face']/@href")) == 0 and len(div.xpath(".//div/p/text()")) == 2:
        break
    item["title"] = div.xpath(".//div/h3/a/text()")[0]
    item["href"] = div.xpath(".//a[@class='face']/@href")[0]
    item["img"] = div.xpath(".//a[@class='face']/img/@src")[0]
    item["detail"] = div.xpath(".//div/p/text()")[0]
    print(item)