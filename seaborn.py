'''

import matplotlib.pyplot as plt

x=[2,4,6,8,10]
y=[4,16,36,64,100]
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.plot(x,y,label="x^2")
plt.title("ploting of square graph")
plt.legend()

plt.grid(True)
plt.show()
'''


import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

'''
data=sns.load_dataset("flights")  #store in a dataframe 
data.head(10)
'''

'''
data=sns.load_dataset("flights")
sns.lineplot(x="year",y="passengers",data=data)

'''

x=[1,2,3,4,5]
y=[1,4,9,16,25]
data=pd.DataFrame({"x":x,"y":y})

sns.lineplot(x="x",y="y",data=data)

