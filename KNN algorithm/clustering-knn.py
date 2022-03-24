#----CLUSTERING----
import pandas as pd
df=pd.read_excel(r'C:\Users\fluff\OneDrive\Desktop\Py+ML\kmeans1.xlsx')

df.head()
df.columns
df.shape

df.dropna(inplace=True)
df=df.dropna()

#deleting the columns
df1=df.drop(['ID Tag', 'Model','Department'],
            axis=1,)
#df.drop(['Department'],axis=1,inplace=True)
df.shape

from sklearn.cluster import KMeans
km=KMeans(n_clusters=3)
km.fit(df1)

x=km.predict(df1)

df['cluster']=x
df.shape

df.sort_values(['cluster'],inplace=True)

df.to_csv(r'C:\Users\fluff\OneDrive\Desktop\Py+ML\kmpredicvted.csv')



