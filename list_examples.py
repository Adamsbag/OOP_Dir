def fun(lst = [1,2]):
    lst.append(100)
    return lst
lst1 = fun([])
lst2 = fun([])
lst3 = fun([])
lst4 = fun([])
print(lst1,lst2,lst3,lst4)
