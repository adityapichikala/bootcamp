import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3,axis=1)
print(newarr[0][2])
print(newarr)


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)




import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

for i in x:
  print(arr[i])



import numpy as np
a=np.array([1,4,3,2,9,7])
print(np.sort(a))


import numpy as np
ar=np.zeros(4)
ar1=np.ones(3)
ar2=np.ones((2,3))
print(ar1)
print(ar)
print(ar2)


import numpy as np
a=np.arange(5)
print(a)


import numpy as np
a=np.eye(3)
print(a)
a2=np.eye(3,4)
print(a2)



import numpy as np
a=np.random.rand(3)
a1=np.random.randn(2,3)
a2=np.random.ranf(3)
print(a2)
print(a)
print(a1)


import numpy as np
#a=np.random.randint(min,max,totalvalues)
a=np.random.randint(5,20,5)
print(a)


import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a.shape)
x=a.reshape(3,4)
print(x)
y=a.reshape(2,3,2)
print(y)

print(y.reshape(-1))



import numpy as np
var= np.array([1,2,3,4])
var2=np.array([6,7,8,9])
varad=np.add(var,var2)
varadd=var+3
varsub=var-1
varmul=var*2
varmod=var%2
print(varadd)
print(varsub)
print(varmul)
print(varmod)
print(var+var2)#or we can use add function
print(varad)
print(np.reciprocal(var))



import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[4,5,6],[1,2,3]])
print(np.add(a,b))



import numpy as np
a=np.array([3, 7,5,9,1])
print("min:",np.min(a),"position of min:",np.argmin(a))
print("max:",np.max(a),"position of max:",np.argmax(a))
print("square root of:",np.sqrt(a))




import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(np.min(a,axis=0))


import numpy as np
a=np.array([1,2,3])
print(np.sin(a))
print(np.cos(a))



import numpy as np
a=np.array([1,2,3,4])
print(np.cumsum(a))
x=np.array([3,4,3])
print(np.cumsum(x))



import numpy as np
a=np.array([1,2,3])
print(a)
b=np.array([[1],[2],[3]])
print(b)
print(np.add(a,b))


import numpy as np
a=np.array([1,2,3])
print(a.shape)
b=np.array([[1,2,3],[5,6,7],[4,8,9]])
print(b.shape)
print(np.add(a,b))



import numpy as np
a=np.array([[[1,2]]])
print(a[0,0,1])



import numpy as np
a=np.array([1,2,3,4,5,6])
print("slicing",a[0:4:2])



import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a)
print(a.ndim)
for i,j in np.ndenumerate(a):
  print(i,j)



import numpy as np
a=np.array([1,2,5,7,9])
print(np.searchsorted(a,4))
#searchsorted function tells us where can we keep the given element in the series


import numpy as np
a=np.array([1,2,3,'a','b',6,'s'])
f=[True,False,True,False,False,True,True]
print(a[f])#filter




import numpy as np
a=np.array([1,2,3,4,5,6])
np.random.shuffle(a)
print(a)#random module shuffle function

'''
Pandas is a high-performance Python library designed for data manipulation and analysis. It provides flexible and powerful tools for working with structured data, allowing you to perform complex operations with minimal code. Some key features of Pandas include:

DataFrames and Series: Pandas uses DataFrames (2D tables) and Series (1D arrays) to represent structured data, similar to tables in a database or Excel.

Comprehensive Data Operations: With Pandas, you can filter, sort, group, merge, concatenate, pivot, and reshape data with ease.

Handling Missing Data: Pandas offers a variety of methods to detect and handle missing or null values.

Integration with Other Libraries: Pandas integrates well with other Python libraries used in data science, like NumPy, SciPy, and matplotlib




Benefits of Using Pandas for Data Cleaning and Analysis

Pandas provides numerous benefits for data cleaning and analysis, making it a popular choice among data scientists and analysts. Here are some key advantages:

Ease of Use: Pandas has a simple and intuitive API, allowing you to perform complex operations with minimal code.

Flexibility: Whether you're cleaning data, performing exploratory analysis, or building models, Pandas offers the flexibility to meet a variety of needs.

Handling Large Datasets: Pandas can handle large datasets efficiently, allowing you to work with millions of rows without significant performance issues.

Comprehensive Data Cleaning: Pandas provides extensive tools for data cleaning, including handling missing data, removing duplicates, and standardizing data formats.

Advanced Data Analysis: With Pandas, you can perform complex operations like group-by, rolling statistics, and multi-level indexing, enabling in-depth analysis.

Pandas is an essential tool for data science and analysis because it simplifies data manipulation, enhances productivity, and integrates with other data science libraries. By using Pandas, data scientists can focus more on analysis and modeling, confident that their data is properly structured and cleaned.



'''


import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)


import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())



import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df)



import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

print(df)


import pandas as pd

df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True)

print(df)



import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df)

