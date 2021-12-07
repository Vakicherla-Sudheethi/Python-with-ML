#1
'''a=list(map(int,input().split()))
print('elements in a:',a)
a.sort()
print('sorting of a:',a)
b=set(a)
print('b is set:',b)
c=list(b)
print('c is the list:',c)
print('the thrid element',c[3])'''
#2
'''a=list(map(int,input().split()))
b=set(a)
c=list(b)
a.sort()#print(sorted(list(set(a))[-3]))
print(a[-3])'''
##a={}
##n=int(input())
##for i in range(n):
##    k=input()
##    a[k]=list(map(int,input().split()))
##print(a)
'''o/p:
2
s1
2 3 4
s2 
4 5 6
{'s1': [2, 3, 4], 's2 ': [4, 5, 6]}'''
#takes the list as ip and returns the count of it as a dictionary with the elements as index and the no of occurances as
#values
#1
'''l=list(map(int,input().split()))
s=set(l)
d={}
for i in s:
    d[i]=l.count(i)
print(d)'''
##7 7 7 1 9 8 8 8 9
##{8: 3, 1: 1, 9: 2, 7:3}
#2
'''l=list(map(int,input().split()))
s=set(l)
d={}
for i in l:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)'''
#----STRINGS-----
'''number based string
-can be converted into a string
character base ]d string
-cannot be converted into a string
>>> a='3'
>>> b='hello'
>>> c=a+b
>>> c
'3hello'
>>> d=4
>>> a+d
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a+d
TypeError: can only concatenate str (not "int") to str
>>> a*d
'3333'
>>> b*d
'hellohellohellohello'
>>> len(b)
5
>>> b
'hello'
>>> b[0]
'h'
>>> b[-1]
'o'
>>> max(b)
'o'
>>> b.index('o')
4
>>> b.index('l')
2
>>> b.upper()
'HELLO'
>>> b.lower()
'hello'
>>> b.isupper()
False
>>> b.islower()
True 
>>> #string can be splitted into a list
>>> r="ram#sai.com"
>>> r.split()
['ram#sai.com']
>>> r.split('#')
['ram', 'sai.com']
>>> r.split('.')
['ram#sai', 'com']
>>> r.index('i')
6
>>> r.rindex('i')
6
>>> #srting to list conversion
>>> r
'ram#sai.com'
>>> t=list(r)
>>> t
['r', 'a', 'm', '#', 's', 'a', 'i', '.', 'c', 'o', 'm']
>>>#list to string
>>> t=''.join(r)
>>> t
'ram#sai.com'
>>> t=''.join(r)
>>> t
'ram#sai.com'
>>> r.startswith('h')
False
>>> t.startswith('r')
True
>>> t
'ram#sai.com'











