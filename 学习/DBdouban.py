import requests
from  lxml  import etree
urls = [
    'http://127.0.0.1:5004/top250.htm',
    'http://127.0.0.1:5004/top250start=25&filter=.htm',
    'http://127.0.0.1:5004/top250start=50&filter=.htm'
]
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
import pymongo
connection = pymongo.MongoClient() # 与mongodb服务器建立连接
db = connection.DbDouban # 选定数据库（导致mongodb服务器自动创建数据库DbDouban)
table = db.TableMovie
# fname = 'saved.txt'
# fd = open(fname, mode='w', encoding='utf-8') #打开文件
for url in urls: #循环处理每一个分页
    # 1.下载网页
    response = requests.get(url, headers = headers)
    text = response.text
    text = text.encode(response.encoding).decode('utf-8')
    # 2.解析网页，提取出电影节点列表
    elements = etree.fromstring(text, etree.HTMLParser())
    movies = elements.xpath('/html/body/div[3]/div[1]/div/div[1]/ol/li[*]')
    for movie in movies: #循环处理每一个电影
        # 提取出每个电影的<标题,评分>
        titles = movie.xpath('./div/div[2]/div[1]/a/span[1]/text()')
        title = titles[0]
        ratings = movie.xpath('./div/div[2]/div[2]/div/span[2]/text()')
        rating = ratings[0]
        #将<标题,评分>存储到mongodb
        table.insert({'title':title, 'rating':rating})
        print(title , rating)
#         #存储到文件
#         s = title + ',' + rating + '\n'
#         fd.write(s)
# fd.close()


