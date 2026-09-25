from numpy import *
arr = array([10, 20, 30, 40, 50])
print(arr)

# Creating array using array()

a = array([1,2,3,4,5],int)
print(a)

a = array([1.1,2.2,3.3,4.4,5.5],float)
print(a)

a= array(['kelvin','jones','thomas','peter','anil'],dtype=str)
print(a)

# Creating arrays using linespace

a = linspace(1,5,5)
print(a)

a = linspace(0,10,5)
print(a)

# Creating array using logspace

a = logspace(1,4,5)
print(a)

# Creating Arrays using arange() Function

a = arange(1,10,3)
print(a)

a = arange(10)
print(a)

a = arange(5,10)
print(a)

# Creating array using zero() and ones() function

a = zeros(5,int)
print(a)

a = ones(5,int)
print(a)
