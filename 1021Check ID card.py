#Author:Yuki
# -*- coding: utf-8 -*-
#2017/10/10

count = int(input())
t = 0
ZZ = []
flag=[]
num=[]
k=0
tt=0
weights = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
while t <= count - 1:
    k=0
    numin = input()
    num.append(numin)
    flagstr = numin.isdigit()
    if flagstr == True:
        for i,j in zip(range(0,17),range(0, 17)):
             k+= int(numin[i])*weights[j]
        Z=k%11
        if Z==0:
            M=1
        elif Z==1:
            M=0
        elif Z==2:
            M='X'
        elif Z==3:
            M=9
        elif Z==4:
            M=8
        elif Z==5:
            M=7
        elif Z==6:
            M=6
        elif Z==7:
            M=5
        elif Z==8:
            M=4
        elif Z==9:
            M=3
        elif Z==10:
            M=2
        ZZ.append(M)
        #print(ZZ[tt])
        if int(numin[17]) == ZZ[tt]:
            flag.append(True)
        else:
            flag.append(False)
        t+=1
        tt+=1

    else:
        flag.append(False)
        t+=1

for t_ in range(0,count):
    if flag[t_]==False:
        print(num[t_])
if False not in flag:
        print("All passed")




