# ACTIVITY 6: LIST MANIPULATION

# Original List
boys = ["Joesper", "Richford", "Roniel", "Anthony", "Lynel", "Jeff", "Laurence", 
        "Nicho", "Arvic", "Louie", "Abad", "Nico", "Doms", "Clyde", "Justine"]

# Prints the original list
print("Original List of Boys - BSIE 1A:")
print(boys)

# Print a specific item/element in the list
print("")
index = int(input("Enter an index number: "))
print("Item:", boys[index])

# Print a range of items/elements in the list
print("")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
end += 1                                                 # since di included yung end index, kailangan dagdagan ng 1 para ma-include yung item sa end index
print("Items in range:", boys[start:end])

# Replace a specific item
print("")
remove = int(input("Enter index number to replace: "))
boys.pop(remove)                                         # function to remove an item in the list
replace = input("Enter replacement: ")
boys.insert(remove, replace)                             # function to insert an item in the list (remove and replace are just variable names)
print(boys)

# Print length of the list
print("")
print("The total number of students in the list is:", len(boys))

# Add a new item
print("")
new_item = input("Enter new item to add on the list: ")
boys.append(new_item)                                    # function to add an item at the end of the list
print(boys)

# Delete a specific item
print("")
delete = int(input("Enter index number to delete: "))
boys.pop(delete)                                         # function to remove an item in the list
print(boys)

# Sorts the list in descending order
print("")
print("Sorted List in Descending Order:")
boys.sort(reverse=True)
print(boys)

# Converts the list to a tuple
print("")
x = tuple(boys)                                          # function to convert a list to a tuple
print("Tuple:")
print(x)

print("The data type is:", type(x))                      # to check the data type of the variable x
