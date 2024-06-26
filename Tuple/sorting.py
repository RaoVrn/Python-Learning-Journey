# The goal of this script is to sort the elements of a tuple in alphabetical order

# Define a tuple of characters (not a list!)
tuple = ("C", "D", "A", "A", "B", "B", "A")

# Tuples are immutable, so we can't sort them in-place. Instead, we convert to a list, sort, and then convert back to a tuple.
list_version = list(tuple)
list_version.sort()
sorted_tuple = tuple(list_version)

# Print the sorted tuple
print(sorted_tuple)