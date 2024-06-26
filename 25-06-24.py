import numpy as np

'''
NumPy, short for Numerical Python, is a library consisting of multidimensional array objects and a collection of routines for processing those arrays. It provides high-performance vector, matrix, and higher-dimensional data structures for Python. Some of the key features of NumPy include:

Arrays: NumPy's main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers.

Mathematical Functions: NumPy provides a large set of mathematical functions that can be performed on arrays. These include arithmetic operations, trigonometric functions, statistical functions, and more.

Broadcasting: NumPy's broadcasting capability allows universal functions to deal with arrays of different shapes during arithmetic operations.

Linear Algebra: NumPy provides a rich set of functions for linear algebra operations, such as matrix multiplication, matrix decomposition, eigenvalues, and more.

Integration with Other Libraries: NumPy seamlessly integrates with other libraries in the scientific Python ecosystem, such as SciPy (scientific computing), Matplotlib (data visualization), and pandas (data manipulation).

'''


import numpy as np
a=np.array([[1,2,3],[2,3,4]])
print(a)


import numpy as n
a=n.array([[1,2,3]])
print(a.shape)


import numpy as np
a=np.array([1,2,3,4,5,6])
print(a.reshape(2,3))


import numpy as np
a=np.array([[1,2,3,4],[9,6,7,8]])
print(a.reshape(1,8))


import numpy as np
a=np.array([1,2,3,4,5,6])
for x in a:
  print(x)


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
for x in a:
  print(x)


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
for x  in a:
  for y in x:
    print(y)


import numpy as np

a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(a):
  print(x)



import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
x=np.concatenate((a,b))
print(x)



import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.array([7,8,9])
y=np.concatenate((a,b,c))
x=np.stack((a,b,c),axis=1)
print(x)
print(y)


import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])
arr3= np.array([7,8,9])

arr = np.vstack((arr1, arr2,arr3))

x=np.stack((arr1,arr2,arr3),axis=1)
print(arr)
print(x)
print(np.add(arr,x))




import numpy as np
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])

a1=np.stack((a,b),axis=1)
a2=np.hstack((a,b)) #row
a3=np.vstack((a,b)) #coloums
a4=np.dstack((a,b)) #height
print(a1)
print(a2)
print(a3)
print(a4)


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])
print(newarr[3])

