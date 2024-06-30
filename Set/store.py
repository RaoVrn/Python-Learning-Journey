# Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)

# Method-I
# Since sets cannot store duplicate values, we cannot have both 9 and 9.0 in the set.
# However, we can store them as string and integer types respectively to differentiate them.
set_1 = {9, "9.0"}  # create a set with integer and string values

print(set_1)  # print the set


"""
Method-II
# In this method, we store both values as strings in the set.
# Although they have different data types in reality, storing them as strings allows us to differentiate them in the set.
"""
set_2 = {"9", "9.0"}  # create a set with string values

print(set_2)  # print the set


"""
Method-III
# In this method, we store both values as string and float types in the set.
# Similar to Method-I, this allows us to differentiate them in the set.
"""
set_3 = {"9", 9.0}  # create a set with string and float values

print(set_3)  # print the set