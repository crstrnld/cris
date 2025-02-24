# Assignment 2

def check_input_types(arg1, arg2, arg3):
    # Check if the types of the inputs are correct
    if isinstance(arg1, str) and isinstance(arg2, int) and isinstance(arg3, float):
        return "Valid input types"
    else:
        return "Invalid input types"

# Demonstrate the function with various test cases
print(check_input_types("hai", 10, 23.4))       
print(check_input_types("100", 5, 24.6))           
print(check_input_types("world", 1.5, "1.1"))    
