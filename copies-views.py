import numpy as np

# No Copy.
a = np.arange(6)

print('No Copy:')
print('\nMain array:\n')
print(a)

print('\nApplying id() function:\n')
print(id(a))

b = a

print('\na is assigned to b:\n') 
print(b)

print('\nb has same id():\n') 
print(id(b))

b.shape = 3, 2

print('\nChange shape of b:\n') 
print(b)

print('\nShape of a also gets changed:\n') 
print(a)

# View or Shallow Copy.
c = np.arange(6)

print('\nView or Shallow Copy:')
print('\nMain array:\n')
print(c)

d = c.view()

print('\nCreate view of a:\n') 
print(d)

print('\nid() for both the arrays are different:\n') 
print(id(c))
print(id(d))

# Change the shape of b. It does not change the shape of a 
d.shape = 2, 3

print('\nShape of d:\n') 
print(d)

print('\nShape of c:\n') 
print(c)

e = np.array([[10, 10], [2, 3], [4, 5]])

print('\nMain array:\n')
print(e)

f = e[:, :2]
print('\nCreate a slice:\n') 
print(f)

# Deep Copy.
g = np.array([[10, 10], [2, 3], [4, 5]])

print('\nDeep Copy:')
print('\nMain array:\n')
print(g)


h = g.copy()

print('\nCreate a deep copy of g:') 
print('Array h is:\n') 
print(h)

#b does not share any memory of a 
print('\nCan we write h is g:\n') 
print h is g

print('\nCan we write h is not g:\n') 
print h is not g

print('\nChange the contents of h:') 

h[0, 0] = 100

print('\nModified array h:\n') 
print(h)

print('\ng remains unchanged:\n') 
print(g)