import pandas as pd
import seaborn as sns
import numpy as np

x=pd.read_csv("C:/Users/Kumari/OneDrive/Desktop/coding/titanic_train.csv")


#print(x.head(5))

#print(x.isnull())

#print(x.isnull().sum())

#print(x.info())


#x1=x["Age"].fillna(value=0)
#print(x1)

#print(x1.isnull().sum())



x2=x.fillna(method="pad")
print(x2)