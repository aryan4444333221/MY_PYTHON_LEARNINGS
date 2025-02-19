# Creating a list
my_list = [1, 2, 3, 4, 5]
list1 = []
list2 = [1, 2, "three"]
print(my_list)  # Output: [1, 2, 3, 4, 5]

# 1. append() - Adds an element to the end of the list
my_list.append(6)
my_list.append(6,2)  # TypeError: list.append() takes exactly one argument 
my_list.append() # TypeError: list.append() takes exactly one argument 
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# 2. extend() - Adds multiple elements to the end of the list
my_list.extend([7, 8, 9])
my_list.extend([7, 8, 9],2) # TypeError: list.append() takes exactly one argument
list1.extend(2) #NameError: name 'my_list' is not defined
my_list.extend(2) # TypeError: "int" is not iterable
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. insert() - Inserts an element at a specific position
my_list.insert(2, 10)  # Insert 10 at index 2
my_list.insert() #TypeError: insert expected 2 arguments
print(my_list)  # Output: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

# 4. remove() - Removes the first occurrence of a value
my_list.remove(10)  # Removes 10
list1.remove(10)  # ValueError: list.remove(x): x not in list
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 5. pop() - Removes and returns the element at a specific position
popped_element = my_list.pop(3)  # Removes element at index 3 (value 4)
popped_element = my_list.pop(293) # IndexError: pop index out of range
popped_element = my_list.pop() # IndexError: pop index out of range
print(popped_element)  # Output: 4
print(my_list)  # Output: [1, 2, 3, 5, 6, 7, 8, 9]

# 6. index() - Returns the index of the first occurrence of a value
index_of_5 = my_list.index(5)
index_of_5 = my_list.index(38923) # ValueError: 38923 is not in list
index_of_5 = my_list.index() # TypeError: index expected at least 1 argument, got 0
print(index_of_5)  # Output: 3

# 7. count() - Returns the number of occurrences of a value
my_list.append(5)  # Add another 5
count_of_5 = my_list.count(5)
count_of_5 = list1.count(5) # No Error returns 0
print(count_of_5)  # Output: 2

# 8. sort() - Sorts the list in ascending order
my_list.sort()
my_list.sort(reverse=True) # Method to Reverse using sort method
list2.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'
print(my_list)  # Output: [1, 2, 3, 5, 5, 6, 7, 8, 9]


# 9. reverse() - Reverses the order of the list
my_list.reverse()
print(my_list)  # Output: [9, 8, 7, 6, 5, 5, 3, 2, 1]

# 10. copy() - Returns a shallow copy of the list
copied_list = my_list.copy()
print(copied_list)  # Output: [9, 8, 7, 6, 5, 5, 3, 2, 1]

# 11. clear() - Removes all elements from the list
my_list.clear()
print(my_list)  # Output: []

# 12. len() - Returns the length of the list
length = len(copied_list)
print(length)  # Output: 9
