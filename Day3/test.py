#!/usr/bin/env python
# -*- coding:utf-8 -*-
def test1(a, b, c, **abc):
    print(a)
    print(b)
    print(c)
    print(abc)
    print(abc['name'])


test1(1, 2, 3, name="123123", age="12")
