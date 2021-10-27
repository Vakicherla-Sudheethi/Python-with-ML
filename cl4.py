#russian peasant method for multiplication
'''a,b=map(int,input().split())
result=0
while a>0:
    if a%2!=0:
        result=result+b
    b=b*2
    a=a//2
print(result)
o/p:
    12 25
300'''
#collatz sequence
'''a=int(input())
while a>1:
    if a%2!=0:
      a=(a*3)+1
      print(a)
    else:
        a=a//2
        print(a)
o/p:
  3
10
5
16
8
4
2
1'''
#collatz sequnece with two inputs
'''n,m=map(int,input().split())
c=0
while c<m-1:
    if n==1:
        print(-1)
        break
    c+=1
    if n%2:
        n=n*3+1
    else:
        n=n//2
else:
    print(n)
o/p:
    3 4
16'''
                    
