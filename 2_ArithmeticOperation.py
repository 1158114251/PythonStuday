#!/usr/bin/python3
#coding=utf-8
"""
python3 条件语句后面后面加冒号
python3 print是一个函数不在是一个关键字所以注意括号

05时30分38秒

"""

name  =input("input your username:")
passwd=input("input your password:")

if name=="zhangfei" and passwd =="123" :
	print ("success login")
elif name=="zhangfei" or passwd =="123" :
	print ("username or passwd error")
else:
	print ("all error")




