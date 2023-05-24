#This is from Udemy DSA Course

import array
my_array1 = array.array('i', [1,2,3,4])

#to insert an element in array we can use array.insert(index, element)
my_array1.insert(0, 6)

#to search an element in an array
def linear_search(arr, target):
    for i in range(len(array)):
        if arr[i] == target:
            return i
        else:
            return "Element not present in array"
