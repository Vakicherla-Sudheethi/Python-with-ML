"""i=1
while i<=10:
    print(i,end=" ")
    i+=1
else:
    print("hai")"""
#program to print table
'''n=int(input())
i=1
for i in range(11):
    print(n,"X",i,"=",n*i)
    i+=1
o/p:
    5
5 X 0 = 0
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50'''
#to take two inputs 
'''n,m=map(int,input().split(" "))
for i in range(m):
    print(n,"X",i,"=",n*i)
    i+=1
o/p:
5 8
5 X 0 = 0
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35'''
#take three inputs and r1 and r2 are two ranges
'''n,r1,r2=map(int,input().split( ))
for i in range(r1,r2+1):
    print(n,"X",i,"=",n+i)
o/p:
    5 X 3 = 8
5 X 4 = 9
5 X 5 = 10
5 X 6 = 11
5 X 7 = 12
5 X 8 = 13'''
# to get in the requires output of 5 table from 7 and 3
'''n,r1,r2=map(int,input().split( ))
for i in range(r2,r1+1):
    print(n,"X",i,"=",n*i)
    i+=1
for i in range(r1,r2+1):
    print(n,"X",i,"=",n*i)
    i+=1    
o/p:
    5 7 3
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35'''
#OR
'''n,r1,r2=map(int,input().split())#n=5
if r1<r2:#3 7
    for i in range(r1,r2+1):
        print(n,"X",i,"=",n*i)
else:#7 3
    for i in range(r2,r1+1):
        print(n,"X",i,"=",n*i)
o/p:
   1) 5 3 7
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
2)
5 7 3
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35'''
#program to skip the multiples of the given number
'''n,m=map(int,input().split( ))
for i in range(20):
    if i%n==0:
        continue
    print(n,"X",i,"=",n*i)
o/p:
    3 10
3 X 1 = 3
3 X 2 = 6
3 X 4 = 12
3 X 5 = 15
3 X 7 = 21
3 X 8 = 24
3 X 10 = 30
3 X 11 = 33
3 X 13 = 39
3 X 14 = 42
3 X 16 = 48
3 X 17 = 51
3 X 19 = 57'''

    
   
        
    
    




    
