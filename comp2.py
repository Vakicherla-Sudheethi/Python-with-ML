#good pairs program
'''a=list(map(int,input().split()))
c=0
n=len(a)
for i in range (n):
    for j in range(i+1,n):
        if a[i]==a[j]:
            c+=1
print(c)'''
##o/p:
##2 2  3 3 
##2
#candies problem
##candies=list(map(int,input().split()))
##c=[]
def fun(candies):
    c=[]
    candy=int(input())
    can=max(candies)
    for i in range(len(candies)):
        if candies[i]+candy>=can:
            c.append(True)
        else:
            c.append(False)
    return c
candies=list(map(int,input().split()))
print(fun(candies))
'''
o/p:
2 3 4 5 
3
[True, True, True, True]'''
