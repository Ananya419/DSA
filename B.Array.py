#  Array:
# CREATING  AN ARRAY

import array

my_array = array.array('i') #---------> O(1)(SPACE & TIME COMPLEXITY)
print(my_array)

my_array1 = array.array('i',[1,2,3,4,5])   # we can not provide string over here like'a' or something else like that
print(my_array1)                           # if we are defining it as integer then all elements must be an integer

import numpy as np
np_array = np.array([],dtype=int) #------------> O(1)(SPACE & TIME COMPLEXITY)
print(np_array)

np_array1 = np.array([1,2,3,4,5]) # ------------>O(N)(SPACE & TIME COMPLEXITY)
print(np_array1)                                # as the no. of elements is increases the time to store its element will also increase proportionally





# INSERTING AN ARRAY
my_array1 = array.array('i',[1,2,3,4,5])   
print(my_array1)
# for adding a new element at the begning of an arrray
my_array1.insert(0,6)
print(my_array1)

# for adding an element at the mid of the array
my_array1 = array.array('i',[1,2,3,4,5])   
print(my_array1)
my_array1.insert(3,6)
print(my_array1)


# for adding an element at the end of the array
my_array1 = array.array('i',[1,2,3,4,5])   
print(my_array1)
my_array1.insert(5,6)
print(my_array1)


# ARRAY TRAVERSAL
from array import *
arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d',[1.3,1.5,1.6])

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)