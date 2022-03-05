#Series
import pandas as p
a=[1,2,3,4]
d=pd.Series(a)
print(d)

#o/p:
'''Name: Year, dtype: int64
0    1
1    2
2    3
3    4'''

#DataFrames
#multiple columns declaration ca be done through dataframes
b=[[2,3,4],[7,8,9]]
e=pd.DataFrame(b)
print(e)

'''o/p:
dtype: int64
   0  1  2
0  2  3  4
1  7  8  9'''

#Defining of columns
#A row or column can be accessed in dataframe if it contains names
b=[[2,3,4],[7,8,9]]
e=pd.DataFrame(b,columns=['c','java','python'])
print(e)
'''o/p:
   0  1  2
0  2  3  4
1  7  8  9
   c  java  python
0  2     3       4
1  7     8       9
'''

#Single column accessing 
b=[[2,3,4],[7,8,9]]
e=pd.DataFrame(b,columns=['c','java','python'])
print(e['c'])

'''o/p:
0    2
1    7'''


#Properties and behaviour of data frame
print(e.size)#o/p:6
print(e.shape)#o/p:(2, 3)


#reading a csv file
data=pd.read_csv(r"C:\Users\fluff\OneDrive\Desktop\Py+ML\IMDB-Movie-Data.csv")
print(data)

'''o/p:
 Rank                    Title  ... Revenue (Millions) Metascore
0       1  Guardians of the Galaxy  ...             333.13      76.0
1       2               Prometheus  ...             126.46      65.0
2       3                    Split  ...             138.12      62.0
3       4                     Sing  ...             270.32      59.0
4       5            Suicide Squad  ...             325.02      40.0
..    ...                      ...  ...                ...       ...
995   996     Secret in Their Eyes  ...                NaN      45.0
996   997          Hostel: Part II  ...              17.54      46.0
997   998   Step Up 2: The Streets  ...              58.01      50.0
998   999             Search Party  ...                NaN      22.0
999  1000               Nine Lives  ...              19.64      11.0

[1000 rows x 12 columns]'''

#Names of corresponding problems
data=pd.read_csv(r"C:\Users\fluff\OneDrive\Desktop\Py+ML\IMDB-Movie-Data.csv")
print(data.columns)

'''o/p:
Index(['Rank', 'Title', 'Genre', 'Description', 'Director', 'Actors', 'Year',
       'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)',
       'Metascore'],
      dtype='object')'''

#printing all years
data=pd.read_csv(r"C:\Users\fluff\OneDrive\Desktop\Py+ML\IMDB-Movie-Data.csv")
print(data["Year"])
'''o/p:
0      2014
1      2012
2      2016
3      2016
4      2016

995    2015
996    2007
997    2008
998    2014
999    2016'''

#Unique- prints data in that years
data=pd.read_csv(r"C:\Users\fluff\OneDrive\Desktop\Py+ML\IMDB-Movie-Data.csv")
print(data['Year'].unique())
#count the number of unique
a=data['Year'].unique()
print(len(a))
'''o/p:
[2014 2012 2016 2015 2007 2011 2008 2006 2009 2010 2013]
11'''

#to know that the no.of movies released in individual years
print(data['Year'].value_counts())
'''o/p:
2016    297
2015    127
2014     98
2013     91
2012     64
2011     63
2010     60
2007     53
2008     52
2009     51
2006     44'''

#Using condition where movie rating is above 6
data[data['Rating']>6.0]
'''o/p:
 Rank                    Title  ... Revenue (Millions) Metascore
0       1  Guardians of the Galaxy  ...             333.13      76.0
1       2               Prometheus  ...             126.46      65.0
2       3                    Split  ...             138.12      62.0
3       4                     Sing  ...             270.32      59.0
4       5            Suicide Squad  ...             325.02      40.0
..    ...                      ...  ...                ...       ...
991   992         Taare Zameen Par  ...               1.20      42.0
992   993     Take Me Home Tonight  ...               6.92       NaN
994   995                Project X  ...              54.72      48.0
995   996     Secret in Their Eyes  ...                NaN      45.0
997   998   Step Up 2: The Streets  ...              58.01      50.0

[790 rows x 12 columns]'''

#accessing with two conditions 
#when both the conditions are true then it'll execute
data[(data['Rating']>6.0) &
     (data["Revenue (Millions)"]>100.0)]
'''o/p:
 Rank  ... Metascore
0       1  ...      76.0
1       2  ...      65.0
2       3  ...      62.0
3       4  ...      59.0
4       5  ...      40.0
..    ...  ...       ...
903   904  ...      76.0
907   908  ...      62.0
924   925  ...      72.0
935   936  ...      66.0
946   947  ...       NaN

[224 rows x 12 columns]'''

#to check any empty spaces in the given data
#if there is empty space it gives true
#or else it gives out false
data.isnull()
'''o/p:
 Rank  Title  Genre  ...  Votes  Revenue (Millions)  Metascore
0    False  False  False  ...  False               False      False
1    False  False  False  ...  False               False      False
2    False  False  False  ...  False               False      False
3    False  False  False  ...  False               False      False
4    False  False  False  ...  False               False      False
..     ...    ...    ...  ...    ...                 ...        ...
995  False  False  False  ...  False                True      False
996  False  False  False  ...  False               False      False
997  False  False  False  ...  False               False      False
998  False  False  False  ...  False                True      False
999  False  False  False  ...  False               False      False

[1000 rows x 12 columns]'''

#Particular column are true and false by isnull()
data['Revenue (Millions)'].isnull().value_counts()

'''o/p:
False    872
True     128
Name: Revenue (Millions), dtype: int64'''


#trying to fill the empty faces
#first delete the empty places
#modify in a variable as the operations performed on data will effect the data
z=data.dropna()
print(z.shape)
'''o/p:
Rank                     Title  ... Revenue (Millions) Metascore
0       1   Guardians of the Galaxy  ...             333.13      76.0
1       2                Prometheus  ...             126.46      65.0
2       3                     Split  ...             138.12      62.0
3       4                      Sing  ...             270.32      59.0
4       5             Suicide Squad  ...             325.02      40.0
..    ...                       ...  ...                ...       ...
993   994  Resident Evil: Afterlife  ...              60.13      37.0
994   995                 Project X  ...              54.72      48.0
996   997           Hostel: Part II  ...              17.54      46.0
997   998    Step Up 2: The Streets  ...              58.01      50.0
999  1000                Nine Lives  ...              19.64      11.0

[838 rows x 12 columns]
(838, 12)
'''

#to replace empty values by filling them
data=data.fillna(0)
data['Revenue (Millions)'].isnull().value_counts()

'''o/p:
False    1000'''

