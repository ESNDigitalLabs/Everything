
"As your programs become larger and more complex, they need to be broken down into smaller, self-contained sections"
"In python function is a type of subroutine, asubroutine is sequence of instructions to perform a specific task with an identifiable name."

"A subroutine(function) definition is used to define the steps within the subroutine(function)"

"A subroutine(function) may or may not have a return statement"

"A subroutine(function) may or may not have parameters"

"def just defines the subroutine(function)"

"A subroutine(function) is not executed unless the subroutine is called."

"A subroutine(function) call tells the program to branch to the function, execute it and come back to the next statement in the main program"

"Custom built function"  '' # A function that you have created yourself and imported into other programs that you have created.

# Syntax
"""
def subroutine/functionName():
    subroutine/functionBody(code)
    subroutine/functionBody(code)
    subroutine/functionBody(code)
    subroutine/functionBody(code)

#call/invoke the subroutine/function
subroutineName/function()


"""

"To Do: Predict, then Run, and then Investigate"
# name is a global variable 
name = "Emjay"
print("Your name is: ", name)

name= input(("What is your name? "))
print("Your name is: ", name)


 # def define the subroutine/function user

# name is a now a local variable 
name = ""

# def define the subroutine userName
def userName():
    print(f'Welcome {name}')

# print("Welcome")
# userName()

"To Do: Task 1: Call the subroutine inside a print function with or without f-strings and explain your result"

def greet(name):
    return f"Hello, {name}!"

print(f"{greet('Bob')}")

#the greet function is called with the argument "Bob", and its return value 
# "Hello, Bob!" is interpolated into the f-string within the print function.

"To Do: Predict, then Run, and then Investigate"
def addition():
    # name is a global variable 
    # answer, num1 and num2 are local variables 
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 + num2
    print(f"The answer to {num1} + {num2} = {answer}")

"Make"
"To Do:Task1: Modify the code above to use either subtraction or multiplication or division and change the subroutine name respectively"

def multiply():
    num1 = int(input("enter your first number: "))
    num2 = int(input("enter your second number: "))
    answer = num1 * num2
    print(f"The answer to {num1} * {num2} = {answer}")
    
multiply()

"To Do:Task2: Add comments to the explain your lines of code"
# def multiply():: This line defines a function named multiply without any parameters.

# num1 = int(input("enter your first number: ")): This line prompts the user to input the 
# first number, converts the input to an integer using the int() function, and assigns 
# the result to the variable num1.

# num2 = int(input("enter your second number: ")): This line prompts the user to input the 
# second number, converts the input to an integer using the int() function, and assigns 
# the result to the variable num2.

# answer = num1 * num2: This line calculates the product of num1 and num2 and assigns 
# the result to the variable answer.

# print(f"The answer to {num1} * {num2} = {answer}"): This line uses an f-string to format 
# and print the multiplication operation and its result. It substitutes {num1}, {num2}, 
# and {answer} with the values of num1, num2, and answer respectively.

# multiply(): This line calls the multiply() function, causing the function's code to execute. 
# When the function is called, the user is prompted to enter two numbers, and their product 
# is computed and printed.

# prevents the automatic running of the subroutine when it is imported
# in to another python file/application
"If this file is run directly it will automatically call and run the respective subroutines"
if __name__ == "__main__":
    addition()

"Further reading on python functions"












"Modify/Make"
"To Do: Task 2: Modify the subroutine to ask for address and interest"

'Task 2: Investigate  if __name__ == "__main__":'
'Copy and paste the code block above if __name__ == "__main__":  in the browser to investigate it use'
# if __name__ == "__main__":
# Add comment to explain why it can be used in your program in your own words"

# call/invoke the subroutine
# call/invoke the subroutine
  
"Knowledge Check"
"Task 4: Linking existing knowledge with new knowledge"
# What do you think is the equivalent of the python 'def' keyword in JavaScript

"Further reading on python functions"
# 


