# Function to add two numbers  
def add(num1, num2): 
    return num1 + num2 
  
# Function to subtract two numbers  
def subtract(num1, num2): 
    return num1 - num2 
  
# Function to multiply two numbers 
def multiply(num1, num2): 
    return num1 * num2 
  
# Function to divide two numbers 
def divide(num1, num2): 
    return num1 / num2

# Function to find Modulo
def modulo(num1, num2):
    return num1 % num2

# Function to calculate Exponential value
def exponential(num1, num2):
    return num1 ** num2

# Default function
def default(num1, num2):
    return "Invalid"

switcher = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide,
    5: modulo,
    6: exponential
}

def switch(operation, number_1, number_2):
    return switcher.get(operation, default)(number_1, number_2)

print("Please select operation: -\n", 
        "1. Add",
        "2. Subtract", 
        "3. Multiply", 
        "4. Divide",
        "5. Modulo",
        "6. Exponent") 
  
  
# Take input from the user  
select = input("Select operations form 1, 2, 3, 4, 5, 6 :") 
  
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 

print "The result is:",(switch(select, number_1, number_2))
