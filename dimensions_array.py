from numpy import *

# single dimensions array
arr1 = array([1, 2, 3, 4, 5])
print("single dimensions array")
print(arr1)

# two dimensions array (2D)
arr2 = array([[1,2,3],[4,5,6]])
print("\n======================")
print("\ntwo dimensions array (2D)")
print(arr2)

# three dimensions array (3D)

arr3 = array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("\n======================")
print("\nthree dimensions array (3D)")
print(arr3)

# The ndim Attribute

print("\n======================")
print("\nThe ndim Attribute")
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# The Shape Attribute

print("\n======================")
print("\nThe Shape Attribute")
print(arr1.shape)
print(arr2.shape)
print(arr3.shape)

# The size Attribute

print("\n======================")
print("\nThe size Attribute")
print(arr1.size)
print(arr2.size)
print(arr3.size)

# The itemsize Attribute

print("\n======================")
print("\nThe itemsize Attribute")
print(arr1.itemsize)
print(arr2.itemsize)
print(arr3.itemsize)

# The dtype Attribute

print("\n======================")
print("\nThe dtype Attribute")
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)

# The nbytes Attribute

print("\n======================")
print("\nThe nbytes Attribute")
print(arr1.nbytes)
print(arr2.nbytes)
print(arr3.nbytes)
