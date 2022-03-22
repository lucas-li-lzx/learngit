#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/2/27 9:54
# @Author  : Lucas
# @File    : 字典生成式.py
# @Software: PyCharm


# 字典生成式类似于列表生成式

# 用for循环生成一个字典：
user_dict = dict()
for i in range(10):
    user_dict[i] = i ** 2
print(user_dict)

# 用字典生成式生成一个字典
user_dict = {x:x ** 2 for x in range(10)}
print(user_dict)

# 字典生成式for后面加上if判断
# 在一个字典生成式中，for前面的if ... else是表达式要成对出现，而for后面的if是过滤条件，不能带else
user_dict = {x:x for x in range(1, 11) if x % 2 == 0}
print(user_dict)

user_dict = dict()
for x in range(1, 11):
    if x % 2 == 0:
        user_dict[x] = x
print(user_dict)

user_dict = {x:x if x % 2 == 0 else -x for x in range(1, 11)}
print(user_dict)

user_dict = dict()
for x in range(1, 11):
    if x % 2 == 0:
      user_dict[x] = x
    else:
      user_dict[x] = -x
print(user_dict)
