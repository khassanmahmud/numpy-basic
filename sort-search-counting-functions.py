import numpy as np

# numpy.sort()
a = np.array([[3, 7], [9, 1]])

print('\nnumpy.sort():')
print('\nMain array:\n')
print(a)

print('\nApplying sort() function:\n') 
print(np.sort(a))

print('\nSort along axis 1:\n') 
print(np.sort(a, axis = 1))

print('\nSort along axis 0:\n') 
print(np.sort(a, axis = 0))

# Order parameter in sort function.
dt = np.dtype([('name', 'S10'), ('age', int)])
b = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype = dt)

print('\nMain array:\n')
print(b)

print('\ndt array:\n')
print(dt)

print('\nOrder by name:\n') 
print(np.sort(b, order = 'name'))

print('\nOrder by age:\n') 
print(np.sort(b, order = 'age'))

# numpy.argsort()
c = np.array([3, 1, 2])

print('\nnumpy.argsort():')
print('\nMain array:\n')
print(c)

print('\nApplying argsort() to d:\n') 
d = np.argsort(c)
print(d)


print('\nReconstruct original array in sorted order:\n') 
print(c[d])

print('Reconstruct the original array using loop:\n') 
for i in d:
	print(c[i])

# numpy.lexsort()
nm = ('raju','anil','ravi','amar')
dv = ('f.y.', 's.y.', 's.y.', 'f.y.')

print('\nnumpy.lexsort():')
print('\nm array:\n')
print(nm)

print('\ndv array:\n')
print(dv)

ind = np.lexsort((nm, dv))

print('\nApplying lexsort() function:\n') 
print(ind)

print('\nUse this index to get sorted data:\n') 
print([nm[i] + ", " + dv[i] for i in ind])

# numpy.argmax() and numpy.argmin()
e = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])

print('\nnumpy.argmax() and numpy.argmin():')
print('\nMain array:\n')
print(e)

print('\nApplying argmax() function:\n') 
print(np.argmax(e))

print('\nApplying argmin() function:\n') 
print(np.argmin(e))

print('\nIndex of maximum number in flattened array:\n') 
print(e.flatten())

print('\nArray containing indices of maximum along axis 1:\n') 
maxindex = np.argmax(e, axis = 1) 
print(maxindex)

print('\nArray containing indices of maximum along axis 0:\n') 
maxindex = np.argmax(e, axis = 0)
print(maxindex)

print('\nArray containing indices of minimum along axis 1:\n') 
minindex = np.argmin(e, axis = 1)
print(minindex)

print('\nArray containing indices of minimum along axis 0:\n') 
minindex = np.argmin(e, axis = 0)
print(minindex)

print('\nFlattened array max:\n') 
maxindex = np.argmax(e)
print(e.flatten()[maxindex])

print('\nFlattened array min:\n') 
minindex = np.argmin(e)
print(e.flatten()[minindex])

# numpy.nonzero()
f = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])

print('\nnumpy.nonzero():')
print('\nMain array:\n')
print(f)

print('\nApplying nonzero() function:\n')
print(np.nonzero(f))

# numpy.where()
g = np.arange(9.).reshape(3, 3)

print('\nnumpy.where():')
print('\nMain array:\n')
print(g)


print('\nIndices of elements > 3:\n') 
h = np.where(g > 3)
print(h)

print('\nUse these indices to get elements satisfying the condition:\n'); 
print(g[h])

# numpy.extract()
i = np.arange(9.).reshape(3, 3)

print('\nnumpy.extract():')
print('\nMain array:\n')
print(i)

# Define a condition.
condition = np.mod(i, 2) == 0

print('\nElement-wise value of condition\n') 
print(condition) 

print('\nExtract elements using condition\n') 
print(np.extract(condition, i))