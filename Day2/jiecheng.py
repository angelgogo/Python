#!/usr/bin/env python
# -*- coding:utf-8 -*-
def jiecheng(num):
    if num == 0:
        return 1
    return num * jiecheng(num - 1)

def pjiecheng(num):
    print(jiecheng(num))
