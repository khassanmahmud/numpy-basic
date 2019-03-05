import numpy as np

# numpy.amin() and numpy.amax()
a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])

print('\nnumpy.amin() and numpy.amax():')
print('\nMain array:\n')
print(a)

print('\nApplying amin() function:\n') 
print(np.amin(a))

print('\nApplying amin() function again:\n') 
print(np.amin(a, 1))

print('\nApplying amin() function again:\n') 
print(np.amin(a, axis = 1))

print('\nApplying amin() function again:\n') 
print(np.amin(a, 0))

print('\nApplying amin() function again:\n') 
print(np.amin(a, axis = 0))

print('\nApplying amax() function:\n')
print(np.amax(a))

print('\nApplying amax() function again:\n')
print(np.amax(a, 1))

print('\nApplying amax() function again:\n')
print(np.amax(a, axis = 1))

print('\nApplying amax() function again:\n')
print(np.amax(a, 0))

print('\nApplying amax() function again:\n')
print(np.amax(a, axis = 0))

print('\nnumpy.ptp():')
print('\nMain array:\n')
print(a)

print('\nApplying ptp() function:\n') 
print(np.ptp(a))

print('\nApplying ptp() function along axis 1:\n') 
print(np.ptp(a, 1))

print ('\nApplying ptp() function along axis 0:\n' )
print(np.ptp(a, 0))

# numpy.percentile()
b = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])

print('\nnumpy.percentile():')
print('\nMain array:\n')
print(b)

print('\nApplying percentile() function:\n') 
print(np.percentile(b, 50))

print('\nApplying percentile() function along axis 1:\n') 
print(np.percentile(b, 50, axis = 1))

print('\nApplying percentile() function along axis 0:\n') 
print(np.percentile(b, 50, axis = 0))


# numpy.median()
c = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])

print('\nnumpy.median():')
print('\nMain array:\n')
print(c)

print ('\nApplying median() function:\n') 
print(np.median(c))

print('\nApplying median() function along axis 1:\n') 
print(np.median(c, axis = 1))

print('\nApplying median() function along axis 0:\n') 
print(np.median(c, axis = 0))

# numpy.mean()
d = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])

print('\nnumpy.mean():')
print('\nMain array:\n')
print(d)

print ('\nApplying mean() function:\n') 
print(np.mean(d))

print('\nApplying mean() function along axis 1:\n') 
print(np.mean(d, axis = 1))

print('\nApplying mean() function along axis 0:\n') 
print(np.mean(d, axis = 0))

# numpy.average()
e = np.array([1, 2, 3, 4])

print('\nnumpy.average():')
print('\nMain array:\n')
print(e)

print('\nApplying average() function:\n') 
print(np.average(e))

# This is same as mean when weight is not specified. 
wts = np.array([4, 3, 2, 1])

print('\nApplying average() function again:\n') 
print(np.average(e, weights = wts))

# Returns the sum of weights, if the returned parameter is set to True. 
print('\nSum of weights:\n') 
print(np.average([1, 2, 3, 4], weights = [4, 3, 2, 1], returned = True))

f = np.arange(6).reshape(3, 2)
wt = np.array([3, 5])

print('\nMain array:\n')
print(f)

print('\nWT array:\n')
print(wt)

print('\nModified array:\n') 
print(np.average(f, axis = 1, weights = wt))

print('\nModified array:\n') 
print(np.average(f, axis = 1, weights = wt, returned = True))

# Standard Deviation.
g = np.array([1, 2, 3, 4])

print('\nStandard Deviation:\n')
print(np.std([1, 2, 3, 4]))
print(np.std(g))

# Variance.
h = np.array([1, 2, 3, 4])

print('\nVariance:\n')
print(np.var([1, 2, 3, 4]))
print(np.var(h))