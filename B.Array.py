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
    for i in array: #--------->O(n)   
        print(i)    #--------->O(1)  both after combining became O(n) time complexity and O(1) space complexity

traverseArray(arr1)
traverseArray(arr2)


# ACCESSING AN ELEMENT OF AN ARRAY
from array import *
arr1 = array('i', [1,2,3,4,5,6])
def accessElement(array, index):
    if index >= len(array):   #----------->O(1)
        print('There is not any element in this index')  # ---->O(1)
    else:
        print(array[index]) # ------>O(1)   
        # it means it has O(1) time complexity

accessElement(arr1, 1)
accessElement(arr1, 8)
accessElement(arr1, 6)


# SEARCHING AN ELEMENT
from array import *
arr1 = array('i', [1,2,3,4,5,6])

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(my_array1,8))


# DELETING AN ELEMENT FROM ARRAY 
from array import *
arr1 = array('i', [1,2,3,4,5,6])

arr1.remove(1)
print(arr1)
arr1.remove(4)
print(arr1)


from array import *

# 1). CREATE AN ARRAY AND TRAVERSE

my_array = array('i',[1,2,3,4,5,])

for  i in my_array:
    print(i)

