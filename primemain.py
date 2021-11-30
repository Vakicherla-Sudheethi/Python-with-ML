from math import sqrt
def fact_count(num):
    if num==1:
        return num
    fc=2
    sq=int(sqrt(num))
    for i in range(2,sq+1):
        if num%i==0:
            fc+=2
    if num==i*i:
        fc-=1
        return fc
num=int(input())
print(fact_count(num))#print(fact_count(num==2))#prime number
"""
output:
1.100 9
2.36 9
3.1 1
"""

def isprime(num):
    sq=int(sqrt(num))
    for i in range(2,sq+1):
        if num%i==0:
            return False
    return True
"""
output:
101
True
100
False"""
def iscprime(num):
    if isprime(n):
        r=0
        while num:
            s=n%10
            d=n//10
            rnum=rnum*10+s
           
        if isprime(r):
            return "prime and cprime"
        else:
            return "prime but not a cprime"
    else:
        return "not a prime"


def mprime(num):
    if isprime(num):
        r=0
        while num:
            d=num%10
            s=num//10
            if isprime(d)==False:
                return "prime not a mega prime"
        else:
            return "prime and mega prime"
    else:
        return "not a prime"
