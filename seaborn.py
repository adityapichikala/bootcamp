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

'''
x=[1,2,3,4,5]
y=[1,4,9,16,25]
data=pd.DataFrame({"x":x,"y":y})

sns.lineplot(x="x",y="y",data=data)

'''
'''
x=sns.load_dataset("penguins")
x
sns.lineplot(x="bill_depth_mm",y="flipper_length_mm",data=x,hue="sex" )
plt.show()

'''

'''
sns.displot(x["bill_depth_mm"])
plt.show()

'''

'''
sns.displot(x["flipper_length_mm"],bins=[170,190,200,210,220])
plt.show()
'''

'''
sns.displot(x["flipper_length_mm"])
plt.show()
'''


'''
sns.displot(x["bill_depth_mm"],kde=True)
plt.show()
'''

'''
sns.barplot(x=x.island,y=x.bill_depth_mm)
plt.show()

'''

'''
sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",hue="sex",data=x)
plt.show()
'''


'''
sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=x)
plt.show()
'''

'''
sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=x,hue="sex,size="sex",sizes=(100,60),alpha=1)
plt.show()

'''

'''
import numpy as np
var =np.linspace(1,10,10).reshape(2,5)
var
'''

'''
sns.heatmap(var,vmin=0,vmax=10)
'''


'''
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


data = np.random.rand(10, 12)

sns.heatmap(data, annot=True, cmap='coolwarm')
plt.show()

'''

'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

x=sns.load_dataset("tips")

sns.countplot("x=sex",data=x)
plt.show()
'''


'''
sns.pairplot(data=x)
plt.show()
'''

'''
sns.factorplot(x="size",y="tip",data=var)
plt.show()
'''

