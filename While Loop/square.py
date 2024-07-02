# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Method-I

list = []

i = 1
while (i <= 10):
    mul = i*i
    list.append(mul)
    i += 1

print(list)



# Method-II

my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list = []

i = 0

while (i < len(my_list)):
    list.append(str(my_list[i]))
    i += 1
print(list)



# Method-III

my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(my_list):
    print(my_list[i], end=' ')
    i += 1