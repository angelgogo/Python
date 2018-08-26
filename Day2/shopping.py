#!/usr/bin/env python
# -*- coding:utf-8 -*-
shopping=[
    ("Iphone",8500),
    ("Ipade", 4200),
    ("Huawei P20", 8500),
    ("Light", 500),
    ("OPPO", 2500),
    ("TV", 3400)
]

buying=[]
sallary=input("Please input your sallary:")
if sallary.isdigit():
    int(sallary)
    for shangpin in shopping:
        print(shopping.index(shangpin)+1,shangpin)
    select=input("Please Choose your like:<<<")
    if select.isdigit():
        select=int(select)
        if 0 < select and select <= int(len(shopping)):
            choose_list=shopping[select]
            if choose_list[1] <=int(sallary):
                sallary -=int(choose_list[1])
                buying.append(choose_list)
                print("You choose  ",buying,"  and your last sallary is ",sallary)
            else:
                print("哥们，你的钱不够捏！")
else:
    print("You input is %s ,is not a number!"%sallary)
