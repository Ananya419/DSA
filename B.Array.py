#  Array:
# Creating an Array

import array

my_array = array.array('i') #---------> O(1)(SPACE & TIME COMPLEXITY)
print(my_array)

my_array1 = array.array('i',[1,2,3,4,5])   # we can not provide string over here like'a' or something else like that
print(my_array1)                           # if we are defining it as integer then all elements must be an integer

import numpy as np
np_array = np.array([],dtype=int) #------------> O(1)(SPACE & TIME COMPLEXITY)
print(np_array)

np_array1 = np.array([1,2,3,4,5]) # ------------>O(N)(SPACE & TIME COMPLEXITY)
print(np_array1)                                # as the no. pf elements is increases the time to store its element will also increase proportionally

