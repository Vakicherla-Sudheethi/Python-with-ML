#missing numbers in the given array program
'''def fun(a):
    for i in range(len(a)+1):
        if i not in a:
            return i
a=list(map(int,input().split()))
print(fun(a))'''
'''
o/p:
3 0 1
2'''
def freq(num):
    a=[]
    for i in range(0,len(num),2):
        a.extend([num[i+1]]*num[i])
    return a
num=list(map(int,input().split()))
print(freq(num))
