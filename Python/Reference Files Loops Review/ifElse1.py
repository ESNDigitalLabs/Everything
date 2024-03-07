# Selection is used to control the flow of the program

pStudy = input("Enter your program of study: ").title()
curProgram = "Bootcamp"

pStudy = input("Enter your program of study: ").title()
curProgram = "Bootcamp"
if pStudy == curProgram:
    print(f"Welcome to our Bootcamp:")
else:
    print(f"Sorry Course is now full")

"Predict, then Run, and then Investigate"

# check the condition that pStudy value is same as the value held in curProgram

# do something/execute the line of code if the condition is checked above true/met - welcome

# The block(else) of code will be executed if the codition in the if block is not true/not met


"Modify"
#ToDo: Exercise
# Modify the code above to use the "!=" operator, or the "not" operator


"Your Turn to: Apply and Build"

"Task 1: Using if and else"
# 1. Create a program that finds the minimum value between two numbers using if else


    
num1 = int(input( "enter your first number:"))
num2 = int(input( "enter your second number"))
    
if num1 < num2:
    return num1
else:
    return num2

    minimum = minimum_number(num1, num2)
print("The minimum value between", num1, "and", num2, "is:", minimum)


"Task 2"
# 2.Create a python program to check user's password and print "Logged In" if successful
# else "Not Logged In“ when unsuccessful.

def check_password(password):
    # Define the correct password
    correct_password = "password123"

    # Check if the entered password matches the correct password
    if password == correct_password:
        print("Logged In")
    else:
        print("Not Logged In")

# Prompt the user to enter their password
user_password = input("Enter your password: ")

# Check the password
check_password(user_password)
