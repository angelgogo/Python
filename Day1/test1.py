#!/usr/bin/env python
# -*- coding:utf-8 -*-
print ( 'Please input your name:' )
name = input ()
print ( 'Please input your age:' )
age =  input ()

while True:
    if not age.isdigit():
        print("Please reenter the age, age is number:")
        age = input()
    elif age.isdigit():
        break
print ( 'my name is :' + name + '\nmy age is:' + str(age) )


print(range(10))