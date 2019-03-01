import numpy as np

a = np.arange(0, 60, 5)

print('Original array:\n')
print(a)

a = a.reshape(3, 4)

print('\nArray after reshaping:\n')
print(a)

print('\nModified array is:\n')

for x in np.nditer(a):
	print(x)

b = a.T

print('\nTranspose of the original array is:\n') 
print(b)

print('\nModified array is:\n')

for x in np.nditer(b):
	print(x)

c = b.copy(order = 'C')

print('\nIteration Order:\n')
print(c)
print('\nSorted in C-style order:\n')

for x in np.nditer(c):
	print(x)

d = b.copy(order = 'F')

print('\n')
print(d)
print('\nSorted in F-style order:\n')

for x in np.nditer(d):
	print(x)

print('\nSorted in C-style order of original array:\n')

for x in np.nditer(a, order = 'C'):
	print(x)

print('\nSorted in F-style order of original array:\n')

for x in np.nditer(a, order = 'F'):
	print(x)

print('\nModifying Array Values:')
print('\nOriginal array:\n')
print(a)

for x in np.nditer(a, op_flags = ['readwrite']):
	x[...] = 2 * x

print '\nModified array is:\n'
print(a)

print('\nExternal Loop:')
print('\nOriginal array:\n')
print(a)

print('\nModified array is:\n')

print('\nSorted in F-style order:\n')
for x in np.nditer(a, flags = ['external_loop'], order = 'F'):
	print(x)

print('\nSorted in C-style order:\n')
for x in np.nditer(a, flags = ['external_loop'], order = 'C'):
	print(x)


m = np.arange(0, 60, 5) 
m = m.reshape(3, 4)
n = np.array([1, 2, 3, 4], dtype = int)

print('\nBroadcasting Iteration:')
print('\nFirst array:\n')
print(m)

print('\nSecond array:\n')
print(n)

print ('\nModified array is:\n') 
for x,y in np.nditer([m,n]):
	print("%d:%d" % (x,y))
