import numpy as np

a = np.array([0, 30, 45, 60, 90])

# Convert to radians by multiplying with pi/180 

print('Trigonometric Functions:')
print('Array containing sine, cos and tan values:\n') 
sin = np.sin(a * np.pi/180)
cos = np.cos(a * np.pi/180)
tan = np.tan(a * np.pi/180)

print(sin)
print(cos)
print(tan)

print('\nCompute sine, cos and tan inverse of angles. Returned values are in radians.\n')
invSin = np.arcsin(sin)
invCos = np.arccos(cos)
invTan = np.arctan(tan)

print(invSin)
print(invCos)
print(invTan)

print('\nCheck result by converting to degrees:\n') 
print(np.degrees(invSin))
print(np.degrees(invCos))
print(np.degrees(invTan))

# Functions for Rounding.
b = np.array([1.0, 5.55, 123, 0.567, 25.532])

print('\nRounding:')
print('Original array:\n') 
print(b)

print('\nAfter rounding:\n') 
print(np.around(b))
print(np.around(b, decimals = 1))
print(np.around(b, decimals = -1))

# Functions for Flooring.
c = np.array([-1.7, 1.5, -0.2, 0.6, 10])

print('\nFlooring:')
print('Original array:\n') 
print(c)

print('\nThe modified array:\n') 
print(np.floor(c))

# Functions for Ceiling.
print('\nCeiling:')
print('Original array:\n') 
print(c)

print('\nThe modified array:\n') 
print(np.ceil(c))