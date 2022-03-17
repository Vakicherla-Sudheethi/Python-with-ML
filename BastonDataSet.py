#--------REGRESSION---------
import pandas as pd
names=['crim','zn','indus','chas','nox','rm','age','dis','rad','tax','ptratio','b','lstat','medev']
d=pd.read_csv(r"C:\Users\fluff\OneDrive\Desktop\Py+ML\boston.csv",names=names)

d.isnull()
d.value_counts()
d.drop_duplicates()

x=d.iloc[:,:13].values
y=d.iloc[:,13].values
x.shape
y.shape

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=1)
xtrain.shape#(404, 13)
xtest.shape#(102, 13)
ytrain.shape#(404,)
ytest.shape#(102,)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(xtrain,ytrain)
ypred=model.predict(xtest)

#in regression we dont find accuracy we find the error
from sklearn.metrics import mean_squared_error
import math
print(math.sqrt(mean_squared_error(ytest,ypred)))
#4.8353734582005465

