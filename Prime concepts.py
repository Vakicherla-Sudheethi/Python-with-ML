'''def fun(num):
    if num<=0:
        return 1
    return num+fun(fun(num-2)-1)
print(fun(5))'''
#op:12
'''def fun(num):
    if num<=0:
        print("*")
        return 1
    return fun(fun(num-2)-1)
print(fun(5))'''
##o/p:
##*
##*
##*
##*
##1
#co-primes
'''def gcd(a,b):
    while True:
        if a>b:
            a,b=b,a
        b=b%a
        if b==0:
            return a
from funs import gcd
a,b=map(int,input().split())
if(a%2 or b%2) and gcd(a,b)==1:
    print("co-primes")
else:
    print("not a co-primes")'''
#semi prime
'''from funs import *
num=int(input())
sq=int(sqrt(num))
if isprime(num):
    print('prime')
else:
    print('not a prime')
    for i in range(2,sq+1):
        if num%i==0 and isprime(i) and isprime(num//i):
            print("semi prime")
            break
    else:
        print("not a semi prime")'''
#Perfect number
'''from math import *
num=int(input())
sq=int(sqrt(num))
s=1
for i in range(2,sq+1):
    if num%i==0:
        s=s+i+num//i
if s==num:
    print("perfect")
else:
    print("not perfect")'''
