#This is from Udemy DSA Course

mylist = ['a', 'b', 'c', 'd', 'e']

#list.pop(index) method is used to delete the element present in that index

mylist.pop(2) #This will delete the element at index 2 and will return the updated list
#if we donot give any index, .pop() will delete the last element
#this method has space complexity of O(1) as no extra memory is being created
#it has time complexity of O(n) of we are speicifying index in pop and if we are not specifying any index then it is O(1)

#another method to delete element is del method
del mylist[2]
#with delete method we can delete multiple elements using indexing
del mylist[2:4]
#This has time complextiy of O(n)

#ANother method is remove method. list.remove(element) is used when we donot know the index of element we want to delete
mylist.remove('e')
#This has time complextiy of O(n)





