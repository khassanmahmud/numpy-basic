import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
c = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])


print('ndarray.shape\n')
print(a)
print(a.shape)

# This resizes the ndarray.
a.shape = (3, 2)

print('\n')
print(a)
print(a.shape)

print('\n')
print(b.shape)
print(c.shape)

d = a.reshape(2, 3);

print('\nndarray.reshape\n')
print(d)
print(d.shape)

# An array of evenly spaced numbers. 
e = np.arange(24)

print('\nndarray.ndim\n')
print(e)

e.ndim

# Now reshape it. 
f = e.reshape(2, 4, 3)

# f is having three dimensions.
print(f)

# dtype of array is int8 (1 byte). 
g = np.array([1, 2, 3, 4, 5], dtype = np.int8)

# dtype of array is now float32 (4 bytes).
h = np.array([1, 2, 3, 4, 5], dtype = np.float32)

print('\nndarray.itemsize\n')
print(g)
print(g.itemsize)
print(h)
print(h.itemsize)

i = np.array([1, 2, 3, 4, 5])

print('\nndarray.flags\n')
print(i)
print(i.flags)