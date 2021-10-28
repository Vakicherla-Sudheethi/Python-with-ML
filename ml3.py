#prime number
'''n=int(input())#7#6
for i in range(2,n):#2,7--2,3,4,5,6#2,6---2,3,4,5
    if n%i==0:#not in 2,3,4,5,6#6/2---done
        print('not prime')#loop is not executed#printed
        break#comes out of loop with 6 as not prime
else:
    print('prime')#executed'''
'''
o/p:
3
prime
4
not prime'''
#another method--efficient method than previous
'''import math
n=int(input())
b=int(math.sqrt(n))
for i in range(2,b+1):
    if n%2==0:
        print('not prime')
        break
else:
    print('prime')
o/p:
    2
prime
4
not prime
'''
#another method
'''import math
n=int(input())
b=int(math.sqrt(n))
for i in range(2,n//2+1):
    if n%2==0:
        print('not prime')
        break
else:
    print('prime')
o/p:
    2
prime'''
#prime number inn range of 2,30

'''for n in range(2,31):
        for i in range(2,n):
                        if n%i==0:
                             #print('not prime')
                            break
         else:
             print(n)
o/p:
    2
3
5
7
11
13
17
19
23
29'''
#prime numbers in the given range
'''a=int(input())
b=int(input())
for n in range(a,b+1):
        for i in range(2,n):
                        if n%i==0:
                             #print('not prime')
                            break
        else:
             print(n)'''
#to find the previous prime number in the given range
'''n=int(input())
for j in range(n,0,-1):
        for i in range(2,j):
                        if j%i==0:
                             #print('not prime')
                            break
        else:
             print(j)
             break
o/p:
    10
7'''




