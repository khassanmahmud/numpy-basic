import numpy as np

a = np.arange(10)
s = slice(2, 7, 2)

print a
print s
print a[s]

b = a[2:7:2]
print b

# slice single item.
c = a[5]
print c 

# slice items starting from index. 
d = a[2:]
print d

# slice items between indexes. 
e = a[2:5]
print e

f = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print f

# slice items starting from index.
print 'Now we will slice the array from the index a[1:]' 
print f[1:]

g = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])

print '\nOur array is:\n'
print g

# This returns array of items in the second column.
print '\nThe items in the second column are:\n'  
print g[...,1]

# Now we will slice all items from the second row. 
print '\nThe items in the second row are:\n' 
print g[1,...]

# Now we will slice all items from column 1 onwards.
print '\nThe items column 1 onwards are:\n' 
print g[...,1:]