#----KNN algorithms implementation on a data set----
#iris data set
import pandas as pd
h=['sl','sw','pl','pw','class']
data=pd.read_csv(r'C:\Users\fluff\OneDrive\Desktop\Py+ML\iris123.csv',names=h)

#to check the data is printed or not
#it prints the top 5 lines
#data.head(!0)#Prints the top 10 lines
data.head()
#reads the last 5 lines -just to check that the data is printed or not
data.tail()
data.shape

data=data.fillna(2)

#x is declared as independent varibles and y is as target variable
#iloc means integer location
#[: means the rows representation 
#,:4] means the strting row to ending row
#,4]means only 4th row- its 0 1 2 3 4 so 4 is the class thus class will be taken
#.values means then x and y are coverted into numpyi.e arrays which are previously present as pandas
#[after execution]
#type(x)#numpy.ndarray
#type(y)#numpy.ndarray
x=data.iloc[:,:4].values
y=data.iloc[:,4].values
x.shape#(150,4)
y.shape#(150,)
#print(y)

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=1)
#random_state makes all 80 for training and remaining for testing
xtrain.shape#o/p: (120, 4)
xtest.shape#o/p:(30,4)
ytrain.shape#o/p:(120,)
ytest.shape#o/p:(30,)

#import algorithm--knn
from sklearn.neighbors import KNeighborsClassifier
modelknn=KNeighborsClassifier(n_neighbors=1)
#k val is set to 1

modelknn.fit(xtrain,ytrain)

ypred=modelknn.predict(xtest)
ypred.shape

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred)*100)#96.66666666666667 #100.0

#future value prediction
print(modelknn.predict([[5.4,3.9,1.3,0.4]]))
#['Iris-setosa']




