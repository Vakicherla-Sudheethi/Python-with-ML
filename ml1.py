#functions 
'''a=10
b=20
def add():#func def
    print(a+b)#no output
#there is only function def but no function call
add()#func call
add()
print('done')
add()#repetition of fun call for n times
'''
#one function works for two diff inputs
'''def add(a,b):#def add(m,n)#parameters given at func def are called formal parameters(for namesake)
    print(a+b)#print(m+n)#the size of the parameters is considered
a=int(input())
b=int(input())
add(a,b)#parameters which can be given at call are called actual parameters
#add(a,b,c)--makes error as the size of both parameters
#thus,the no.of actual parameters=no.of formal parametrs.
add(1,5)'''
#actual implementation by importing the modules
'''def add(a,b):
    print(a+b)
ANOTHER FILE:
import ml1#imports the ml1 file
a=int(input())
b=int(input())
ml1.add(a,b)
'''
#importing inbuilt modules in python
'''import math#imports all the functions of math module
print(math.sqrt(25))#returns 5.0
print(math.pow(2,4))#returns 16.0'''








