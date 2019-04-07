# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 07:21:00 2019

@author: mayur
"""
'''
The logic is to make your moves the exact opposite of Lydia's moves. This works
since Lydia's moves are always the right number.
'''
n=int(input())
m_p=[]
m_p_l=[]
for i in range(n):
    g_s=int(input())
    l_p=input()
    m_p=[]
    for i in l_p:
        if i is "E":
            m_p.append("S")
        else:
            m_p.append("E")
    m_p_l.append(m_p)
a=1
for i in m_p_l:
    print("case #",a,": ",sep="",end="")
    for j in i:
        print(j,end="")
    print()
    a+=1
