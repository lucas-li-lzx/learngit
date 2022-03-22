#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/22 10:46
# @Author  : Lucas
# @File    : paixu.py
# @Software: PyCharm

list_01 = [66,45,23,90,78,36,88,55,13,45]
for a in range(len(list_01)-1):
    for b in range(len(list_01)-1-a):
        if list_01[b] > list_01[b+1]:
            list_01[b],list_01[b+1] = list_01[b+1],list_01[b]
print(list_01)
print(list_01)


