#the program that prints the table in the given range--3 upto 50 multiples
'''n,r=map(int,input().split( ))
i=1
while True:#or can use r<=n*i--for natural breaking
    #while true is infinte loop
    print(n,"X",i,"=",n*i)
    i+=1
    if n*i>r:#manual breaking
        break
o/p:
    3 50
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
3 X 10 = 30
3 X 11 = 33
3 X 12 = 36
3 X 13 = 39
3 X 14 = 42
3 X 15 = 45
3 X 16 = 48'''
#2)
"""sample i/p:
3 22 or 4 18
o/p:
7 or 4 5"""
'''n,r=map(int,input().split())
if r%n==0:
    print(r//n)#//-->that returns coefficients
else:
    a=r//n
    b=a+1
    if r-(n*a)==(n*b)-r:
        print(a,b)
    elif r-(n*a)>(n*b)-r:
        print(b)
    else:
        print(a)
o/p:
    #1)
    3 22
7
#2)
4 18
4 5 '''
#program to print lcm of two given numbers
'''a,b=map(int,input().split())
t=2
lcm=1
while True:
    if a%t==0 and b%t==0:
        print(a,b)
        a=a//t
        b=b//t
        print("a and b values are",a,b)
        lcm=lcm*t
    else:
        t+=1
        if a<t or b<t:
                  break
print("lcm : ",lcm*a*b)
o/p:
    12 24
12 24
a and b values are 6 12
6 12
a and b values are 3 6
3 6
a and b values are 1 2
lcm :  24'''
#program to print GCD
'''a,b=map(int,input().split())
while True:
      if a<b:
            b=b%a#no need to change a value
      else:
            a,b=b,a
      if b==0:
            print("gcd: ",a)
            break
o/p:
    42 57
gcd:  3'''



