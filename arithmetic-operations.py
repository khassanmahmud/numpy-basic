import numpy as np

a = np.arange(9, dtype = np.float_).reshape(3, 3)
b = np.array([10, 10, 10])

print('First array:\n') 
print(a)
print('\nFirst array:\n') 
print(b)

print('\nAdd the two arrays:\n') 
print(np.add(a, b))
print('\nSubtract the two arrays:\n') 
print(np.subtract(a, b))
print('\nMultiply the two arrays:\n') 
print(np.multiply(a, b))
print('\nDivide the two arrays:\n') 
print(np.divide(a, b))

# numpy.reciprocal()
c = np.array([0.25, 1.33, 1, 0, 100])
d = np.array([100], dtype = int)

print('\nnumpy.reciprocal():')
print('Original array:\n') 
print(c)
print('\nAfter applying reciprocal function:\n') 
print(np.reciprocal(c))

print('\nOriginal array:\n') 
print(d)
print('\nAfter applying reciprocal function:\n') 
print(np.reciprocal(d))

# numpy.power()
e = np.array([10, 100, 1000])
f = np.array([1, 2, 3])

print('\nnumpy.power():')
print('Original array:\n')
print(e)

print('\nApplying power function:\n') 
print(np.power(e, 2))

print('\nApplying power function again:\n') 
print(np.power(e, f))

# numpy.mod() and numpy.remainder()
g = np.array([10, 20, 30])
h = np.array([3, 5, 7])

print('\nnumpy.mod() and numpy.remainder():')
print('First array:\n')
print(g)

print('\nSecond array:\n')
print(h)

print('\nApplying mod() function:\n') 
print(np.mod(g, h))

print('\nApplying remainder() function:\n') 
print(np.remainder(g, h))

i = np.array([-5.6j, 0.2j, 11. , 1+1j])

print('\nMain array:\n')
print(i)

print('\nApplying real() function:\n') 
print(np.real(i))

print('\nApplying imag() function:\n') 
print(np.imag(i))

print('\nApplying conj() function:\n') 
print(np.conj(i))

print('\nApplying angle() function:\n') 
print(np.angle(i))

print('\nApplying angle() function again (result in degrees):\n') 
print(np.angle(i, deg = True))