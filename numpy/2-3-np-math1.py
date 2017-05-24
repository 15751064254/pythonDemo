import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)
print(a)
print(b)

print('a - b')
c = a - b
print(c)

print('a + b')
c = a + b
print(c)

print('a * b')
c = a * b 
print(c)

print('b**2')
c = b**2
print(c)

print('sin')
c = 10 * np.sin(a)
print(c)

print('b < 3')
print(b)
print(b < 3)


a = np.array([[1, 1], [0, 1]])
b = np.arange(4).reshape((2,2))
print(a)
print(b)
