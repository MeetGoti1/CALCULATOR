# Define a function to perform addition
def add(x, y):
  return x + y

# Define a function to perform subtraction
def subtract(x, y):
  return x - y

# Define a function to perform multiplication
def multiply(x, y):
  return x * y

# Define a function to perform division
def divide(x, y):
  # Check if the divisor is zero
  if y == 0:
    # Return an error message
    return "Cannot divide by zero"
  else:
    # Return the quotient
    return x / y

# Ask the user to enter the operation they want to perform
operation = input("Enter the operation (+, -, *, /): ")

# Ask the user to enter the first operand
x = float(input("Enter the first number: "))

# Ask the user to enter the second operand
y = float(input("Enter the second number: "))

# Perform the operation based on the user's input
if operation == "+":
  result = add(x, y)
elif operation == "-":
  result = subtract(x, y)
elif operation == "*":
  result = multiply(x, y)
elif operation == "/":
  result = divide(x, y)
else:
  result = "Invalid operation"

# Print the result
print(f"The result is {result}")
