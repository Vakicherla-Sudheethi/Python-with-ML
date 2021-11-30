#twin prime
'''from primeFun import *
a,b=map(int,input().split())
c=0
while a<=b:
    if a%2 and isprime(a) and isprime(a+2):
        c+=1
        a+=2
    a+=1
print(c)'''
#safe prime
'''from funs import *
num=int(input())
if isprime(num):
    print("prime")
    if isprime(num//2):
        print("safe prime")
    else:
        print("not a safe prime")
else:
    print("not a prime")'''
#good prime
'''from funs import *
num=int(input())
if isprime(num):
    print("prime")
    i=2
    while True:
        L=num-i
        if isprime(L):
            break
        i+=2
    i=2
    while True:
        R=num-i
        if isprime(R):
            break
        i+=2
    if L*R<num*num:
        print("good prime")
    else:
        print("not Good prime")        
else:
    print("not prime")'''
