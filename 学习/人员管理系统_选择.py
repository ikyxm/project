print("----------请选择功能----------")
choice = input("请选择功能：\n1.添加学生\n2.删除学生\n3.查询学生\n4.修改学生信息\n")
if choice == "1":
    print("添加学生")
elif choice == "2":
    print("删除学生")
elif choice == "3":
    print("查询学生")
elif choice == "4":
    print("修改学生信息")
else:
    print("输入错误！")