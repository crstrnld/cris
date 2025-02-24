# Assignment 3

# Prompt the user to enter two values: x and y
x = input("Enter the first value (x): ")
y = input("Enter the second value (y): ")

# Convert the values to boolean
x_bool = bool(x)
y_bool = bool(y)

# Print the results of logical operations
print(f"x AND y: {x_bool and y_bool}")
print(f"x OR y: {x_bool or y_bool}")
print(f"NOT x: {not x_bool}")
print(f"x XOR y: {x_bool != y_bool}")

# Test the script with different input scenarios
test_inputs = [0, 1, "", "non-empty", None, 42]
for i in test_inputs:
    for j in test_inputs:
        print(f"Testing with x: {i}, y: {j} -> x XOR y: {bool(i) != bool(j)}")
