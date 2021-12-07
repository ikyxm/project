import requests
import pymongo
from lxml import etree
con = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = con['douban']
table = db['movie']

for page in range(0,250,25):
    url = f'https://movie.douban.com/top250?start={page}&filter='
    h = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    resp = requests.get(url,headers=h)
    text = resp.text

    ele = etree.fromstring(text,parser=etree.HTMLParser())
    path = '/html/body/div[3]/div[1]/div/div[1]/ol/li[*]'
    nodes = ele.xpath(path)

    for node in nodes:
        title = node.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
        score = node.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
        table.insert({'title':title,'score':score})