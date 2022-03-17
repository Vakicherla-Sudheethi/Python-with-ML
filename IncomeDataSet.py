import pandas as pd
#headers are given manually
names=['age','sector','sal','qualification','work-experience',
       'marital-status','profession','relation','skintone',
       'gender','debt','a','b',
       'country','salary']
#d is a data frame
d=pd.read_csv(r"C:\Users\fluff\OneDrive\Desktop\Py+ML\income.csv",names=names)

d.isnull()
d.value_counts()

d.drop_duplicates()

d[d['profession']=='?'].count()

d['profession']=d['profession'].replace(to_replace="?",value="prof-specialty")
d['sector']=d['sector'].replace(to_replace=" ?",value="Private")

#label encoding is a process which can give numnbers to thecorresponding strings in a data set
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
d['sector']=le.fit_transform(d['sector'])
d['qualification']=le.fit_transform(d['qualification'])
d['marital-status']=le.fit_transform(d['marital-status'])
d['profession']=le.fit_transform(d['profession'])
d['relation']=le.fit_transform(d['relation'])
d['skintone']=le.fit_transform(d['skintone'])
d['gender']=le.fit_transform(d['gender'])
d['country']=le.fit_transform(d['country'])





d.head(10)
d.shape

#training
x=d.iloc[:,:14].values
y=d.iloc[:,14].values
x.shape#(32561, 14)
y.shape#(32561,)
type(x)#numpy.ndarray

#testing
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=1)
xtrain.shape#(26048, 14)
xtest.shape#(6513, 14)
ytrain.shape#(26048,)
ytest.shape#(6513,)

#apply algorithm
from sklearn.neighbors import KNeighborsClassifier
modelknn=KNeighborsClassifier(n_neighbors=5)

modelknn.fit(xtrain,ytrain)

ypred=modelknn.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred)*100)
#78.79625364655305

print(modelknn.predict([[39,6,77516,9,13,4,0,1,4,1,2174,0,40,39]]))
#[' <=50K']