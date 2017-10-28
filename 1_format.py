# coding:utf-8
#! usr/bin/python3
"""
python的输入输出
格式化

"""
name = input("input your name:")
age  = input("input your age:")
work = input("input your work:")

info = """
___________info______________

name :%s
age  :%s
work :%s
___________end________________
"""%(name,age,work)
print(info)
