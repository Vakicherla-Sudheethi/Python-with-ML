# step1-->check the module is imorted or not
#plotting of the data in graphs
'''import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[3,1,2,4]
x1=[3,4,5,6]
y1=[7,8,9,10]
plt.plot(x1,y1,c='r',label='male')#gives red color with a label of male
plt.plot(x,y,c='g',label='female')#gives green colour with a label called female
#plt.scatter(x,y)#the points are drawn without a line
#plt.plot(x,y,c='r',marker='*')
plt.title('graph b/w x and y')#title for overall graph
plt.xlabel('x values')#title for x axis
plt.ylabel('y values')#title for y axis
plt.legend()#to show the differences b/w two things
plt.show()#prints the graph'''
#------BAR GRAPHS------
'''import matplotlib.pyplot as plt
x=[i for i in range(2000,2011)]
y=[9,4,5,6,7,2,3,4,7,2,1]
plt.bar(x,y,color='red')#or can use c='red'
#plt.bar(x,y)
plt.savefig('C:\desktop\pic.jpd')#to save the given graph#adress..\pic.jpd or png
plt.show()'''
#splitting of two graphs
'''import matplotlib.pyplot as plt
x=[i for i in range(2000,2011)]
y=[9,4,5,2,4,2,3,8,9,1,3]
z=[i for i in range(11)]

plt.subplot(2,1,1)#subplot --splits the space into two parts
#(2,1,1)here 1 at last represents the 1st part of the graph
plt.bar(x,y,color='r')
plt.title('male')

plt.subplot(2,1,2)#here 2 represents the 2nd part
plt.bar(x,z,color='g')
plt.title('female')

plt.show()'''
#---PIE CHART----
'''import matplotlib.pyplot as plt
x=[30,40,20,10]
l=['c','java','p','cpp']
c=[0.05,0,0,0]
plt.pie(x,label=1,explode=c)#explode is used to highlight the graph by taking out
plt.legend()
plt.show()'''





















