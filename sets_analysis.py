# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# 1. add() - Adds an element to the set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
# Error Condition: No specific error condition. It will always work as long as the set exists.

# 2. update() - Adds multiple elements to the set
my_set.update([7, 8, 9])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Error Condition: If the argument passed is not iterable (e.g., an integer or None).
# Example:
# my_set.update(10)  # TypeError: 'int' object is not iterable

# 3. remove() - Removes a specific element from the set
my_set.remove(5)
print(my_set)  # Output: {1, 2, 3, 4, 6, 7, 8, 9}
# Error Condition: If the element to be removed is not found in the set.
# Example:
# my_set.remove(10)  # KeyError: 10

# 4. discard() - Removes a specific element (does not raise an error if the element is not found)
my_set.discard(10)  # No error, even though 10 is not in the set
print(my_set)  # Output: {1, 2, 3, 4, 6, 7, 8, 9}
# Error Condition: No specific error condition. It will not raise an error if the element is not found.

# 5. pop() - Removes and returns an arbitrary element from the set
popped_element = my_set.pop()
print(popped_element)  # Output: Random element (e.g., 1)
print(my_set)  # Output: Remaining set after popping (e.g., {2, 3, 4, 6, 7, 8, 9})
# Error Condition: If the set is empty.
# Example:
# empty_set = set()
# empty_set.pop()  # KeyError: 'pop from an empty set'

# 6. clear() - Removes all elements from the set
my_set.clear()
print(my_set)  # Output: set()
# Error Condition: No specific error condition. It will always work as long as the set exists.

# 7. copy() - Returns a shallow copy of the set
my_set = {1, 2, 3}
copied_set = my_set.copy()
print(copied_set)  # Output: {1, 2, 3}
# Error Condition: No specific error condition. It will always work as long as the set exists.

# 8. union() - Returns a new set with elements from both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
# Error Condition: No specific error condition. It will always work as long as the sets exist.

# 9. intersection() - Returns a new set with common elements
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}
# Error Condition: No specific error condition. It will always work as long as the sets exist.

# 10. difference() - Returns a new set with elements in the first set but not in the second
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}
# Error Condition: No specific error condition. It will always work as long as the sets exist.

# 11. symmetric_difference() - Returns a new set with elements in either set but not in both
symmetric_diff_set = set1.symmetric_difference(set2)
print(symmetric_diff_set)  # Output: {1, 2, 4, 5}
# Error Condition: No specific error condition. It will always work as long as the sets exist.

# 12. issubset() - Checks if all elements of a set are present in another set
print(set1.issubset({1, 2, 3, 4}))  # Output: True
# Error Condition: No specific error condition. It will always work as long as the sets exist.

# 13. issuperset() - Checks if a set contains all elements of another set
print(set1.issuperset({1, 2}))  # Output: True
# Error Condition: No specific error condition. It will always work as long as the sets exist.

# 14. isdisjoint() - Checks if two sets have no common elements
print(set1.isdisjoint({4, 5}))  # Output: True
# Error Condition: No specific error condition. It will always work as long as the sets exist.

# 15. len() - Returns the number of elements in the set
print(len(set1))  # Output: 3
# Error Condition: No specific error condition. It will always work as long as the set exists.

# 16. min() - Returns the smallest element in the set
print(min(set1))  # Output: 1
# Error Condition: If the set is empty or contains elements of different types that cannot be compared.
# Example:
# empty_set = set()
# print(min(empty_set))  # ValueError: min() arg is an empty sequence
# mixed_set = {1, 2, "three"}
# print(min(mixed_set))  # TypeError: '<' not supported between instances of 'str' and 'int'

# 17. max() - Returns the largest element in the set
print(max(set1))  # Output: 3
# Error Condition: If the set is empty or contains elements of different types that cannot be compared.
# Example:
# empty_set = set()
# print(max(empty_set))  # ValueError: max() arg is an empty sequence
# mixed_set = {1, 2, "three"}
# print(max(mixed_set))  # TypeError: '>' not supported between instances of 'str' and 'int'

# 18. sum() - Returns the sum of all elements in the set
print(sum(set1))  # Output: 6
# Error Condition: If the set contains non-numeric elements (e.g., strings).
# Example:
# mixed_set = {1, 2, "three"}
# print(sum(mixed_set))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'