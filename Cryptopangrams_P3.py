# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 07:21:01 2019

@author: mayur
"""

from collections import OrderedDict         
import numpy
from functools import reduce


#Efficient way to get a list of primes
def primesfrom2to(n):
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

#Efficient way to get a list of factors
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
#Function to decipher the list of primes        
def decipher(a):
    global d_t
    b=list(OrderedDict.fromkeys(sorted(a)))
    #x,y=l_p.index(b[0]),l_p.index(b[len(b)-1])
    for i in a:
        d_t.append(chr(b.index(i)+65))

#Function to split the given set of products into two primes assuming it has only two prime factors
#The code has to be updates if the number has multiple prime factors
def split_primes_l(l):
    l_p=list(primesfrom2to(a))
    l_f=sorted(list(factors(l[0])))
    l_d_n=[]
    c=0
    for i in l_p:
        if i in l_f:                        #Find the prime factors of the number
            l_d_n.extend([i,l[0]/i])        #Assume the order of the prime factors as smaller first then the greater 
            break
    for i in range(1,len(l)):               #Split the set of numbers into primes
        if (l[i]%l_d_n[-1])==0:
            l_d_n.append(l[i]/l_d_n[-1])
        else:                               #If order is wrong, interchange them
            l_d_n=l_d_n[:2:]
            l_d_n[0],l_d_n[1]=l_d_n[1],l_d_n[0]
            c=1
            break
    
    if c==1:
        for i in range(1,len(l)):
            if (l[i]%l_d_n[-1])==0:
                l_d_n.append(l[i]/l_d_n[-1])
    return l_d_n



d_t=[]
f_o=[]
n=int(input())
for i in range(n):
    x,y=0,0
    d_t=[]
    l_n=[]
    a,b=input().split()
    a,b=int(a),int(b)
    c=input().split()
    c=list(map(int,c))
    l_n=split_primes_l(c)
    decipher(l_n)
    f_o.append(d_t)


a=1
for i in f_o:
    print("case #",a,": ",sep="",end="")
    for j in i:
        print(j,end="")
    print()
    a+=1