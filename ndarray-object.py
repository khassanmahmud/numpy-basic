import numpy as np 

a = np.array([1, 2, 3]) 

# More than one dimensions.
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Minimum dimensions. 
d = np.array([1, 2, 3, 4, 5], ndmin = 2)

# dtype parameter. 
e = np.array([1, 2, 3, 4, 5], dtype = complex)

print(a)
print(b)
print(c)
print(d)
print(e)