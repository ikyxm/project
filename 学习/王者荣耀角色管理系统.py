'''
王者荣耀角色管理系统

角色：姓名，性别，角色
添加角色
删除角色
修改角色
查询角色    单个角色
显示所有角色
退出系统
'''
import time
all_role = [] #存放所有角色'容器'
print('----------欢迎进入王者荣耀角色管理系统----------')
while True:
    choice = input('请选择功能：\n1.添加角色\n2.删除角色\n3.修改角色\n4.查询角色\n5.查询所有角色\n6.退出系统\n')
    #判断
    if choice == '1':
        print('添加角色模块：')
        name = input('\t角色名:')
        sex = input('\t性别：')
        job = input('\t职业：')
        role = [name,sex,job]
        #添加到all_role
        all_role.append(role)
        print(f'成功添加{name}到王者荣耀系统！\n')

    elif choice == '2':
        print('删除角色模块：')
        role_name = input('\t请输入角色名：')
        #查找是否存在角色名称
        for role in all_role:
            if role_name in role:
                if role_name in role:
                    #添加询问是否确认删除
                    remove = input('\t是否确认删除y/n?')
                    if remove == 'y':
                        all_role.remove(role)
                        print(f'\t成功删除角色：{role_name}')
                        break
                    else:
                        print('取消删除，退出删除角色模块！')
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        print('显示所有角色模块：')
        print('{}{}{}'.format('名称'.center(10),'性别'.center(10),'职业'.center(10)))
        for role in all_role:
            print(role[0].center(10),end='')
            print(role[1].center(10),end='')
            print(role[2].center(10),end='')
            print()
    elif choice == '6':
        print('----------正在退出王者荣耀角色管理系统----------')
        time.sleep(3)
        print('成功退出！')
        break
    else:
        print('输入错误，请重新选择！')

