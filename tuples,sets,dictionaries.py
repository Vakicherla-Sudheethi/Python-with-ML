'''--TUPLES---
>we cannot modify them as they are immutable
>>> a=(9,7,6,2,2545,0)
>>> type(a)
<class 'tuple'>
>>> len(a)
6
>>> max(a)
2545
>>> min(a)
0
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.sort()
AttributeError: 'tuple' object has no attribute
'sort'
#we can delete the whole tuple but cannot delete a
single tuple
----SET---
##set is an unordered list without duplicate values
>>> a={4,6,56}
>>> type(a)
<class 'set'>
>>> b={3,3,4,5}
>>> len(b)
3
>>> #doesnt allow dupliacte elements
>>> b
{3, 4, 5}
>>> #set doesnt have a particular index
>>> #so set is aclled as a unordered list
>>> #accessing element in set
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a[0]
TypeError: 'set' object is not subscriptable
>>> #can add elements in set
>>> a.add(34)
>>> a
{56, 34, 4, 6}
>>> a.add(6)#existing element
>>> a
{56, 34, 4, 6}
>>> #deleting an item
>>> a.remove(56)
>>> a
{34, 4, 6}
>>> a.remove(1)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.remove(1)
KeyError: 1
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a
NameError: name 'a' is not defined
#find  the index of the thrid highest element
#1
a=list(map(int,input().split()))
print('elements in a:',a)
a.sort()
print('sorting of a:',a)
b=set(a)
print('b is set:',b)
c=list(b)
print('c is the list:',c)
print('the thrid element',c[3])
#2
a=list(map(int,input().split()))
b=set(a)
c=list(b)
a.sort()#print(sorted(list(set(a))[-3]))
print(a[-3])
----Dictionaries----
{KEY,VALUE}=single element
it is key value based
>>> d={'s1':2,'s2':3,'s3':4}
>>> d
{'s1': 2, 's2': 3, 's3': 4}
>>> type(d)
<class 'dict'>
>>> d['s1']
2
#accessing is only done through keys
#data management is properly done onlly through dictionaries
>>> len(d)
3
>>> d.keys()
dict_keys(['s1', 's2', 's3'])
>>> d.values()
dict_values([2, 3, 4])
>>> d['s4']=[23]
>>> d
{'s1': 2, 's2': 3, 's3': 4, 's4': [23]}
>>> del d['s3']
>>> d
{'s1': 2, 's2': 3, 's4': [23]}
>>> #modify
>>> d['s2']=34
>>> d
{'s1': 2, 's2': 34, 's4': [23]}
'''


