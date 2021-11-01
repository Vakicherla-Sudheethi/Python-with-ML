#---return statement---
#if a function is assignes to a varaible then it requires return statements
#or can use print outside the function
#in collatz sequnece
"""i/p:
3
o/p:
8"""
'''def sequence_count(num):
    count=1
    while num!=1:
        count+=1
        if num%2:
            num=num*3+1
        else:
            num=num//2
    return count        
num=int(input())
print(sequnece_count(num))'''
'''o/p:
3
8'''
#recursion-function calling by itself
#recursion depends on stack
'''def fun(n):
    print(n)#o/p:10,9,8,..1
    if n==1:
        return
    fun(n-1)
    #print(n)#o/p=2,3,4,5..10
fun(10)'''
#sum of n numbers in recursion using backtracking
'''def fun(n):
    if n==1:
        return 1
    return n+fun(n-1)
print(fun(5))'''
'''o/p:
15'''
#reccurance relations--in one functions when there are two calls
def fun(n):
    if n<=1:
        return 1
    return fun(n-1)+fun(n-2)
print(fun(5))
'''o/p:
8'''




