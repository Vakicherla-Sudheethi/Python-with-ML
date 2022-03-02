n=int(input())
for i in range(n+1):
    temp=i
    rev=0
    while(temp>0):
        rem=temp%10
        rev=rev*10+rem
        temp=temp//10
    if(i==rev):
        print("%d"%i,end=" ")
        
