#---FILES---
#reading contents in file
f=open("C:\desktop\python bin\hello.txt",'r')
print(f.read())
#creation of a file
f=open(r"C:\desktop\python bin\hello.txt",'x')
#x gives the indiacation to create a file
print(f.close())
#push the contents in the file
#write mode can create the file and also writes the contents
f=open(r"C:\desktop\python bin\hello.txt",'w')
#f.write('hi good morning')#in case any file is not created it creates the file and writes the msg
print(f.open())
#write mode drawback-the old data is erased and the new data is been inserted
f=open(r"C:\desktop\python bin\hello.txt",'w')
f.write('hi good morning')
print(f.open())
#to get the write statements in different lines
f=open(r"C:\desktop\python bin\hello.txt",'w')
f.write('hi good morning\n')#\n gets new line
f.write('python')
print(f.open())
#append-adds extension to the old file
f=open(r"C:\desktop\python bin\hello.txt",'a')
f.append('hi good morning')
print(f.open())
#readlines
f=open("C:\desktop\python bin\hello.txt",'r')
d=f.readlines()
f.close()
for i in d:
    print(i)
#file can be any type we can add extensions like
#word-doc,excel=xlsx,text-txt
#--deletion of files---
import os
os.remove(r"C:\desktop\python bin\hello.txt")
#remove the directory
import os
os.rmdir(r"C:\desktop\python bin\hello.txt")
#to create a directory
import os
os.mkdir(r"C:\desktop\python bin\hello.txt")



