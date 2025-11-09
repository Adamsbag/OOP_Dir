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
def fun(lst = [1,2]):
    lst.append(100)
    return lst
lst1 = fun()
lst2 = fun()
lst3 = fun()
lst4 = fun()
print(lst1,lst2,lst3,lst4)
# prints:
# [1, 2, 100, 100, 100, 100]
# Explanation:
# In this code, the function `fun` is called four times without any arguments.
# Since the default argument is a mutable list, the same list is used across all calls.
# Each time the function is called, 100 is appended to this same list.
