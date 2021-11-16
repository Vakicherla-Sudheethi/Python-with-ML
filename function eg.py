#1)
#program that prints a number with even and odd on bothsides
'''def fun(n):
    en=0
    on=0
    p1=0
    p2=0
    while n:
        #digit by digit logic
        d=n%10
        n=n//10
        if d%2:
            on=d*pow(10,p1)+on
            p1+=1
        else:
            en=d*pow(10,p2)+en
            p2+=1
    print(en,on)
n=int(input())
fun(n)'''
##o/p:
##    6271916
##626 7191
#2)program that prints the number is even odd or mixed
def fun(n):
    num=0
    c=0
    while n:
        d=n%10
        n=n//10
        c=c+d
        if num%2==0 and c%2:
            return "even odd"
        if num%2 and c%2==0:
            return "odd even"
    if num%2:
        return "odd"
    return "even"
n=int(input())
print(fun(n))
