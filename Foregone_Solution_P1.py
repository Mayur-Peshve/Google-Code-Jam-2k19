# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 07:20:59 2019

@author: mayur
"""
'''
The logic I used was to subtract from the given number, a number with 1s 
present only at those locations where 4s are present.
For Example: 940 is split as 930 and 30.
This can be done for any and all inputs 
'''
n=int(input())
k=[]
for i in range(n):
    k.append(int(input()))

def split_n(n):
    a=n
    while "4" in str(a):
        i=str(a).index("4")
        l=len(str(a))
        k=l-i-1
        p=pow(10,k)
        a=a-p           
    return (a,n-a)
for i in range(len(k)):
    a,b=split_n(k[i])
    print("case #",i+1,": ",a," ",b,sep="")