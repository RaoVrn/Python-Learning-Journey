# Create a Python dictionary to store "key : values" by inputting them from the user

# Create an empty dictionary to store key-value pairs
dict = {}

# Ask the user how many entries they want to add to the dictionary
n = int(input("Enter the number of entries you want to add in the dictionary: "))

# Loop through the number of entries specified by the user
for i in range(0, n):
    # Ask the user to input a key for the dictionary
    key = input("Enter the key: ")
    
    # Ask the user to input a value for the key
    value = input("Enter the value of the key: ")
    
    # Add the key-value pair to the dictionary
    dict[key] = value

# Print the resulting dictionary
print("The dictionary is:", dict)