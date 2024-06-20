# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Initial list:", my_list)

# Adding an element to the list
my_list.append(6)
print("List after adding an element:", my_list)

# Removing an element from the list
my_list.remove(3)
print("List after removing an element:", my_list)

# Modifying an element in the list
my_list[2] = 10  # Changing the third element (index 2) to 10
print("List after modifying an element:", my_list)


# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nInitial dictionary:", my_dict)

# Adding an element to the dictionary
my_dict['d'] = 4
print("Dictionary after adding an element:", my_dict)

# Removing an element from the dictionary
del my_dict['b']
print("Dictionary after removing an element:", my_dict)

# Modifying an element in the dictionary
my_dict['c'] = 10  # Changing the value of key 'c' to 10
print("Dictionary after modifying an element:", my_dict)


# Creating a set
my_set = {1, 2, 3, 4, 5}
print("\nInitial set:", my_set)

# Adding an element to the set
my_set.add(6)
print("Set after adding an element:", my_set)

# Removing an element from the set
my_set.remove(3)
print("Set after removing an element:", my_set)

# Note: Sets are unordered collections of unique elements, so there's no direct way to modify an element.
# Instead, we remove an element and add a new one if needed.
if 4 in my_set:
    my_set.remove(4)
    my_set.add(10)
print("Set after modifying an element (by removing 4 and adding 10):", my_set)