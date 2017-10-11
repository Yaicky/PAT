#Author:Yuki
# -*- coding: utf-8 -*-
#2017/10/10
sets = {}  #dictionary
nums = input()
num = set(nums)
for item in sorted(num):
    print(str(item) + ":" + str(nums.count(item)))


