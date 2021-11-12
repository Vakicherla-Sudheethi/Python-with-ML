'''
import csv

f=open(r'C:\Users\fluff\OneDrive\Desktop\Py+ML\sample.csv')
d=csv.reader(f)

for i in d:
    print(i)'''
#program  to print only one column
'''import csv


f=open(r'C:\Users\fluff\OneDrive\Desktop\Py+ML\sample.csv')
d=csv.reader(f)

for i in d:
    print(i[3])'''
#program to print no.of male and female
'''import csv
f=open(r'C:\Users\fluff\OneDrive\Desktop\Py+ML\sample.csv')
d=csv.reader(f)
m=0
f=0
for i in d:
    if i[3]=='Male':
        m+=1
    else:
        f+=1
print(m,f)'''
#the above same program using pandas
'''import pandas as pd
data=pd.read_csv(r'C:\Users\fluff\OneDrive\Desktop\Py+ML\sample.csv')
print(data['Gender'].value_counts())
'''
'''o/p:
Female    760
Male      240
Name: Gender, dtype: int64
0      Female
1      Female
2        Male
3      Female
4      Female
 
995    Female
996    Female
997    Female
998      Male
999    Female
Name: Gender, Length: 1000, dtype: object'''
'''import pandas as pd
a=[1,2,3,4,6]
data=pd.Series(a,name='marks',index=['a','b','c','d','e'])
print(data)'''
#creating a table in pandas
'''import pandas as pd
a=[[1,2,3,4],[3,4,2,1],[6,5,4,2,]]
data=pd.DataFrame(a,columns=['s1','s2','s3','s4'],index=['a','b','c'])
print(data)'''
'''o/p:
 s1  s2  s3  s4
a   1   2   3   4
b   3   4   2   1
c   6   5   4   2'''
#program to print the countries
'''import pandas as pd
data=pd.read_csv(r'C:\Users\fluff\OneDrive\Desktop\Py+ML\sample.csv')
print(data['Country'])'''
'''o/p:
0      United States
1      Great Britain
2             France
3      United States
4      United States
     
995    United States
996    United States
997    United States
998    United States
999    United States
Name: Country, Length: 1000, dtype: object'''
'''
print(data['Id'])
print(data['Age'])
0      1562
1      1582
2      2587
3      3549
4      2468

995    2654
996    6525
997    3265
998    3265
999    6125
Name: Id, Length: 1000, dtype: int64
0      32
1      25
2      36
3      25
4      58
       ..
995    34
996    28
997    32
998    39
999    29
Name: Age, Length: 1000, dtype: int64'''
#to plot a graph using matplotlib 
'''
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv(r'C:\Users\fluff\OneDrive\Desktop\Py+ML\sample.csv')
data.plot(x='Age',y='Id')
plt.show()'''
  
