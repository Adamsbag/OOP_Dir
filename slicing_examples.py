lst = [1,2,3,4,5,6,7,8,9,10,11] # Can take any types of variables and is mutable while a tup() is immutable cannot and is not mutable
print(lst[1:6]) #print [2, 3, 4, 5, 6]

print(lst[1:6:2]) #print [2, 4, 6] from index 1 to 6 jumping every other index

print(lst[:-1]) #print every element but the last one

print(lst[-1:]) #print [11] displays only the last element

print(lst[::-1]) # print [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] reverse the list

lst[2:4] = [100, 200]
print(lst) # print [1, 2, 100, 200, 5, 6, 7, 8, 9, 10, 11] replace 3, 4 with 100, 200






