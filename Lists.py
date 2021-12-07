#arrays-list,set,tuple,dictionary which are heterogeneous data types
#LIST-declare,modify,delete
'''1.declaration:
syntax:a[]
2.acess:by using their  index position
eg:len(a),max(a),min
#---operations performed on numbers list---
>>> a=[56,45,8,9,2,1]
>>> type(a)
<class 'list'>
>>> len(a)
6
>>> max(a)
56
>>> min(a)
1
>>> a.sort()#it will modify the existing list
>>> print(a)
[1, 2, 8, 9, 45, 56]
>>> a.sort(reverse=True)
>>> a
[56, 45, 9, 8, 2, 1]
#operations performed in combined list
>>> b=[23,45.67,True,'ram@gmail.com']
>>> len(b)
4
>>> max(b)#when list is of same function i.e items of same datatype then it will work
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    max(b)
TypeError: '>' not supported between instances of 'str' and 'float'
>>> b.sort()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    b.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
#other functions performed
>>> a.count(7)#return the number of apperances
0
>>> a.count(2)
1
---using strings---
>>> c=['python','c','java','cpp']
>>> max(c)
'python'#the output are based on ASCII value
>>> min(c)
'c'
----fun to find ASCII----
>>> ord('a')
97
>>> ord('A')
65
---ASCII to normal---
>>> chr(100)
'd'
#sorting is done on the ASCII value
>>> c
['python', 'c', 'java', 'cpp']
>>> c.sort()
>>> c
['c', 'cpp', 'java', 'python']
>>> d=[12,4,14,8,45]
>>> #   0 1  2 3 4--9index places
>>> d[3]
8
>>> d[5]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d[5]
IndexError: list index out of range
>>> d[4]
45
>>> d=[12,4,14,8,45]
>>> #   0 1  2 3 4--9index places
>>> d[3]
8
>>> d[5]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d[5]
IndexError: list index out of range
>>> d[4]
45
>>> d[:]
[12, 4, 14, 8, 45]
>>> d[1:3]
[4, 14]
>>> d[:4]
[12, 4, 14, 8]
>>> d[2:17]
[14, 8, 45]
>>> d[2:]
[14, 8, 45]
>>> d[::]
[12, 4, 14, 8, 45]
>>> d[::1]
[12, 4, 14, 8, 45]
>>> d[::2]
[12, 14, 45]
>>> d[::3]
[12, 8]
>>> d[::-1]
[45, 8, 14, 4, 12]
>>> d[::-2]
[45, 14, 12]
>>> d[::-3]
[45, 4]
>>> d[1:3:-1]
[]
>>> d[5:3:-1]
[45]
>>> d[3:5:-1]
[]
>>> d[4:2:-1]
[45, 8]
>>> d[3:2:-1]
[8]
>>> d[5:2:-1]
[45, 8]
>>> e=[7,8,5,0,7,5,9]
>>> e[5:2:-1]
[5, 7, 0]
>>> e[5:1:-1]
[5, 7, 0, 5]
>>> e
[7, 8, 5, 0, 7, 5, 9]
>>> #-7 -6 -5 -4 -3 -2 -1
>>> e[-2:-6:-1]
[5, 7, 0, 5]
>>> e.index(5)
2
#list update---replacement in the list
>>> e=[7,8,5,2,1,8]
>>> e[5]=3
>>> e
[7, 8, 5, 2, 1, 3]
>>> e[2:5]=[9,5,3]
>>> e
[7, 8, 9, 5, 3, 3]
>>> e.append(2)#adds element to last place
>>> e
[7, 8, 9, 5, 3, 3, 2]
>>> e.insert(2,34)
>>> e
[7, 8, 34, 9, 5, 3, 3, 2]
>>> e.extend(a)
>>> e
[7, 8, 34, 9, 5, 3, 3, 2, 56, 45, 9, 8, 2, 1]
>>> #2.delete the ele in the middle
>>> e.pop(3)
>>> e
[7, 8, 34, 5, 3, 3, 2, 56, 45, 9, 8, 2]
>>> #3.delete the ele by mentioning it with no index place
>>> e.remove(56)
>>> e
[7, 8, 34, 5, 3, 3, 2, 45, 9, 8, 2]
>>> del e[2]
>>> e
[7, 8, 5, 3, 3, 2, 45, 9, 8, 2]
>>> w=[5,6,8,9]
>>> x=w
>>> del w[2]
>>> w
[5, 6, 9]
>>> x
[5, 6, 9]
#----delete---
>>> del c
>>> c
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> c.clear()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    c.clear()
NameError: name 'c' is not defined
>>> a.clear()
>>> a
[]
'''
#find min and max from user ip using list
'''a=list(map(int,input().split()))
print(max(a),min(a))'''
###o/p:
##2 3 4 4 2 8
#8 2
#how to create a list in for loop
#based on index
'''a=list(map(int,input().split()))
for i in range(len(a)):
    print(i,a[i])'''
#based on elements
'''a=list(map(int,input().split()))
for i in a:
    print(i,a.index(i))'''
#print length of a list without using length function
'''l=list(map(int,input().split()))
c=0
for i in l:
    c+=1
print(c)'''
# program to know about the no.of occurances in the list
'''a=list(map(int,input().split()))
b=int(input())
c=0
for i in a:
    if b==i:
        c+=1
print(c)'''
a=list(map(int,input().split()))
x=0
for i in a:
    if i>x:
        x=i
print(x)
'''o/p:
5 6 8 2 9 
9'''

