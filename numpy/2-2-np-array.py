import numpy as np

a = np.array([2, 23, 4])
print(a)

a = np.array([2, 23, 4], dtype = np.int)
print(a.dtype)

a = np.array([2, 23, 4], dtype = np.int32)
print(a.dtype)

a = np.array([2, 23, 4], dtype = np.float)
print(a.dtype)

a = np.array([2, 23, 4], dtype = np.float32)
print(a.dtype)

a = np.array([[2, 23, 4], [2, 23, 4]])
print(a)

print('zeros')
a = np.zeros((3, 4))
print(a)

print('ones')
a = np.ones((3, 4), dtype = np.int)
print(a)

print('empty')
a = np.empty((3, 4))
print(a)

print('arange')
a = np.arange(10, 20, 2)
print(a)

print('reshape')
a = np.arange(12).reshape((3, 4))
print(a)

print('linspace')
a = np.linspace(1, 10, 20)
print(a)

a = np.linspace(1, 10, 20).reshape((5, 4))
print(a)

