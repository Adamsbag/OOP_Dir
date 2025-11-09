lst = [x for x in range(10)]
print(lst) # print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst1 = [x for x in range(10) if x %2 == 0]
print(lst1) # print [0, 2, 4, 6, 8]

lst2 = [[x for x in range(10) if x %2 == 0] for _ in range(5)] # print the list of even numbers 5 times
print(lst2) # print [[0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8]]



