    # Creating a list of fruits
fruits = ["apple", "banana", "cherry", "date"]

# Display the original list
print("Original list of fruits:", fruits)

# Accessing elements in the list
print("First fruit:", fruits[0])  # Accessing the first element
print("Last fruit:", fruits[-1])   # Accessing the last element

# Adding elements to the list
fruits.append("elderberry")  # Add to the end of the list
print("After appending elderberry:", fruits)

fruits.insert(2, "fig")      # Insert 'fig' at index 2
print("After inserting fig at index 2:", fruits)

# Removing elements from the list
fruits.remove("banana")      # Remove 'banana' from the list
print("After removing banana:", fruits)

removed_fruit = fruits.pop()  # Remove and return the last item
print("Removed the last fruit:", removed_fruit)
print("List after popping last item:", fruits)

# Iterating through the list
print("Iterating through the list of fruits:")
for fruit in fruits:
    print(fruit)

# List length
print("Number of fruits in the list:", len(fruits))

# Sorting the list
fruits.sort()
print("Sorted list of fruits:", fruits)

# Reversing the list
fruits.reverse()
print("Reversed list of fruits:", fruits)
