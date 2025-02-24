# Assignment 1

a=input("Please enter the first number (a): ")
b=input("Please enter the second number (b): ")
c=input("Please enter the third number (c): ")

# Check if the conditions are met
if (a > b or b > c) and (a % 2 == 0 and c % 2 != 0) and (b != c):
    print("Conditions met")
else:
    print("Conditions not met")


# Assignment 2

def check_input_types(arg1, arg2, arg3):
    # Check if the types of the inputs are correct
    if isinstance(arg1, str) and isinstance(arg2, int) and isinstance(arg3, float):
        return "Valid input types"
    else:
        return "Invalid input types"

# Demonstrate the function with various test cases
print(check_input_types("hello", 5, 3.14))       # Output: Valid input types
print(check_input_types(100, 5, 3.14))           # Output: Invalid input types
print(check_input_types("world", 2.5, "1.1"))    # Output: Invalid input types


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
