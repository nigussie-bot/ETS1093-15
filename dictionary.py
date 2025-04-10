# Creating a dictionary of fruits and their colors
fruits = {
    "apple": "red",
    "banana": "yellow",
    "mango": "red",
    "avocado": "green"
}

# Display the original dictionary
print("Original dictionary of fruits:", fruits)

# Accessing values in the dictionary
print("Color of apple:", fruits["apple"])  # Accessing value by key

# Adding key-value pairs to the dictionary
fruits["zyton"] = "purple"  # Add a new fruit with its color
print("After adding zyton:", fruits)

# Updating a value in the dictionary
fruits["banana"] = "green"  # Change the color of banana
print("After updating banana's color:", fruits)

# Removing key-value pairs from the dictionary
del fruits["avocado"]  # Remove 'avocado' from the dictionary
print("After removing avocado:", fruits)

# Using pop() to remove a key and return its value
removed_color = fruits.pop("mango")  # Remove 'mango' and get its color
print("Removed mango, its color was:", removed_color)
print("Dictionary after popping mango:", fruits)



# Checking if a key exists in the dictionary
if "apple" in fruits:
    print("Apple is in the dictionary.")

# Getting the number of key-value pairs in the dictionary
print("Number of fruits in the dictionary:", len(fruits))

# Clearing the dictionary
fruits.clear()
print("Dictionary after clearing all items:", fruits)
