# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print("Change x so that it is [1, 2, 3, 4]:\n", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print("\nUsing y, change x so that it is [1, 2, 3, 4, 8, 9, 10]:\n", x )

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print("\nChange x so that it is [1, 2, 3, 4, 9, 10]: \n", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print("\nChange x so that it is [1, 2, 3, 4, 9, 99, 10]:\n", x)

# Print the length of list x
print("\nPrint the length of list x:\n", len(x))
# YOUR CODE HERE

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
print("\nPrint all the values in x multiplied by 1000:")
for num in x:
    print(num * 1000)
