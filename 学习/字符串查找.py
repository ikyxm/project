'''
https://www.baidu.com/s?wd=%E7%99%BE%E5%BA%A6%E7%83%AD%E6%90%9C&sa=ire_dl_gh_logo_texing&rsv_dl=igh_logo_pcs
'''
path = 'https://www.baidu.com/s?wd=%E7%99%BE%E5%BA%A6%E7%83%AD%E6%90%9C&sa=ire_dl_gh_logo_texing&rsv_dl=igh_logo_pcs'

#find,index,rfind,rindex
#find 从左往右查找，只要遇到一个符合要求的，则返回位置，如果没找到任何要求的，则返回-1
i = path.find('/s')
url = path[:i]
print(url)
#rfind从右到左，只要遇到一个符合要求的，则返回位置，如果没找到任何要求的，则返回-1
i = path.rfind('=')
name = path[i+1:]
print(name)
# index从左往右查找，只要遇到一个符合要求的，则返回位置，如果没找到任何要求的，则报错ValueError: substring not found
# i = path.index('#')
# url = path[:i]
# print(url)

'''
查找字符串有几个符号
'''
#count:统计指定字符的个数
n = path.count('=')
print(n)