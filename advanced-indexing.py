import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])

b = a[[0, 1, 2], [0, 1, 0]]
c = a[[2, 1, 0], [1, 0, 1]]
d = a[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]]
e = a[[2, 2, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0]]

print('Integer Indexing:\n')
print(a)
print('\n')
print(b)
print(c)
print(d)
print(e)

f = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])

rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])

g = f[rows, cols]

print('\nMain array:\n')
print(f)
print('\nThe corner elements of this array are:\n')
print(g)

mrows = np.array([[1, 1], [2, 2]])
mcols = np.array([[0, 2], [0, 2]])

h = f[mrows, mcols]

print('\nThe middle corner elements of this array are:\n')
print(h)

orows = np.array([[0, 0], [2, 2]])
ocols = np.array([[0, 2], [0, 2]])

i = f[orows, ocols]

print('\nThe odd rows corner elements of this array are:\n')
print(i)

erows = np.array([[1, 1], [3, 3]])
ecols = np.array([[0, 2], [0, 2]])

j = f[erows, ecols]

print('\nThe even rows corner elements of this array are:\n')
print(j)

print('\nMain array:\n')
print(f)

# slicing.
k = f[1:4, 1:3]

print('\nAfter slicing, our array becomes:\n')
print(k)

# Using advanced index for column
l = f[1:4, [1, 2]]

print('\nSlicing using advanced index for column:\n') 
print(l)

print('\nBoolean Array Indexing:\n')
print('Main array:\n')
print(f)

# Now we will print the items greater than 5 
print('\nThe items greater than 5 are:\n') 
print(f[f>5])

m = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])

print('\nFiltering NaN (Not a Number):\n')
print(m)
print(m[np.isnan(m)])
print(m[~np.isnan(m)])

n = np.array([1, 2+6j, 5, 3.5+5j])

print('\nFiltering complex number:\n')
print(n)
print(n[np.iscomplex(n)])
print(n[~np.iscomplex(n)])

