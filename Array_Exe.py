import array
a = array.array('i',[10,20,30,40,50])
for i in range(5):
    print(a[i])
    
print("=============================")

import array as ar
a = ar.array('i',[60,70,80,90,100])
for i in range(5):
    print(a[i])
    
print("=============================")

from array import *
a = array('i',[1,2,3,4,5])
for i in range(5):
    print(a[i])

#append
a.append(6)
print("After append:", a)

#insert
a.insert(1, 14)
print("After insert:", a)

#extend
a.extend([7, 8, 8, 1])
print("After extend:", a)

#pop
a.pop(1)
print("After pop:", a)

#remove
a.remove(8)
print("After remove:", a)

#index
x = a.index(8)
print("Index of 8 is:", x)

#count
total = a.count(1)
print("Count of 1 is:", total)

#tolist
py_list = a.tolist()
print("As a Python list:", py_list)

#fromlist
extra_list = [10, 20]
a.fromlist(extra_list)
print("After fromlist:", a)  

#reverse
a.reverse()
print("After reverse:", a)
