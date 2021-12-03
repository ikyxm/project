'''
可变参数:**kwargs
关键字参数
在函数调用时必须传递关键字参数，才可以将其转化为key:value，装到字典中
'''

#key word
def show_book(**kwargs):
    print(kwargs)   # {}    字典

show_book()
show_book(bookname = '西游记')
show_book(bookname = '西游记',author = '吴承恩')
show_book(bookname = '西游记',author = '吴承恩',number = 5)

book = {'bookname' : '西游记','author' : '吴承恩','number' : 5}
show_book(**book)