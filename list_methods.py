lst = [1,2,3,5,11,9,6,7,4,8,10,11]

contains = 2 in lst
index = lst.index(2)
print(contains, index) # print "True 1" true if exist and 1 for the index of "2"

print(lst.count(11)) # print "2" counts how many "11" exist in the list

print(lst.sort()) #print None but put the list in order
print(lst) # Print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]

print(lst.sort(reverse=True)) # Print None but reverse the list 
print(lst) # Print [11, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(lst.reverse())
print(lst) # Print [None] and [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]

lst1 = [1,2,3,5,11,9,6,7,4,8,10,11]
print(sorted(lst1)) # Print
print(lst1) # Print []

lst2 = [1,2,3,5,11,9,6,7,4,8,10,11]
print(reversed(lst2)) # Print <list_reverseiterator object at 0x00000228E4B87FA0>
print(list(reversed(lst2))) # Print [11, 10, 8, 4, 7, 6, 9, 11, 5, 3, 2, 1] solve the reversed iterator issue
print(lst2) # Print [1, 2, 3, 5, 11, 9, 6, 7, 4, 8, 10, 11]
def fun(lst = [1,2]):
    lst.append(100)
    return lst
lst1 = fun([])
lst2 = fun([])
lst3 = fun([])
lst4 = fun([])
print(lst1,lst2,lst3,lst4)  
# prints:
# [100] [100] [100] [100]       
# Explanation:
# In this code, the function `fun` is called four times with an empty list as an argument.
# Each time, a new empty list is created and passed to the function.
# Therefore, each call to `fun` appends 100 to a different list, resulting in four separate lists,
# each containing only the value 100.








