#i/p:5
#o/p: 1 2 3 4 5 4 3 2 1 
"""def fun(n):
    for i in range(1,n+1):
        #n-=1
        print(i,end=" ")
        n-=1
    else:
        while n<i-1:
            i-=1
            print(i,end=" ")
            #n+=1
n=int(input())
fun(n)"""
'''o/p:
5
1 2 3 4 5 4 3 2 1

7
1 2 3 4 5 6 7 6 5 4 3 2 1'''
#or

"""def fun(n):
    for i in range(n*2-1):
        if i<n:
            print(i+1,end=" ")
            i+=1
        else:
            n-=1
            print(n,end=" ")
n=int(input())
fun(n)"""
#i/p:n=4532
##o/p:
##453 2
##45  3
##4   5
##0  4
"""n=int(input())
while n:
    d=n%10
    n=n//10
    print(n,d)"""
'''o/p:
4532
453 2
45 3
4 5
0 4'''
#count the no of digits
#i/p:4532
#o/p:4
'''def fun(n):
    count=0
    while n:
        d=n%10
        n=n//10
        count+=1
    print(count)
n=int(input())
fun(n)'''
'''o/p:
767
3'''
#same program using recursion
"""def fun(num):
    if num<10:
        return 1
    return 1+fun(num//10)
num=int(input())
print(fun(num))"""
'''
o/p:
464643
6'''
def fun(n):
    count=0
    while n:
                d=n%10
                n=n//10
                count+=1
    print(count)
n=int(input())
fun(n)
