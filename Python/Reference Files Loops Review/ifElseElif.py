# Selection is used to control the flow of the program

# elif == else if

score = int(input("Enter a number: "))
"Predict, then Run, and then Investigate"
# check the condition that score is greater than 100
score = int(input("Enter a number: "))

if score > 100:
    print("Score is greater than 100")
elif score == 100:
    print("Score is equal to 100")
else:
    print("Score is less than 100")


# create a variable and assign it the value Invalid Entry
invalid_entry_message = "Invalid Entry"


# check the condition that score is between 75 and 100
score = int(input("Enter a number: "))

if score > 100:
    print("Score is greater than 100")
elif score >= 75:
    print("Score is between 75 and 100")
else:
    print("Score is less than 75")

# create a variable and assign it the value A
a_variable = "A"


# check the condition that score is between 60 and 74
score = int(input("Enter a number: "))

if score > 100:
    print("Score is greater than 100")
elif score >= 75:
    print("Score is between 75 and 100")
elif score >= 60:
    print("Score is between 60 and 74")
else:
    print("Score is less than 60")


# reassign the grade variable the value B
grade = "B"

# check the condition that score is between 50 and 59
score = int(input("Enter a number: "))

if score > 100:
    print("Score is greater than 100")
elif score >= 75:
    print("Score is between 75 and 100")
elif score >= 60:
    print("Score is between 60 and 74")
elif score >= 50:
    print("Score is between 50 and 59")
else:
    print("Score is less than 50")


# reassign the grade variable the value C
grade = "C"

# reassign the grade variable the value F
grade = "F"

# full code 
score = int(input("Enter a number: "))

# check the condition that score is greater than 100
if score > 100:
    print("Score is greater than 100")
    grade = "Invalid Entry"
# check the condition that score is between 75 and 100
elif score >= 75:
    print("Score is between 75 and 100")
    grade = "A"
# check the condition that score is between 60 and 74
elif score >= 60:
    print("Score is between 60 and 74")
    grade = "B"
# check the condition that score is between 50 and 59
elif score >= 50:
    print("Score is between 50 and 59")
    grade = "C"
else:
    print("Score is less than 50")
    grade = "F"

# Output the grade
print("Grade:", grade)


#ToDo: Q&A
"What do you think is the equivalent of JS else if in python?"


"Make"
#ToDo: Task 1: Using if elif and else
# Create a Menu program that allows users to select between three subject choices
# User must be presented with the value assoiciated with each choice
# for example 1. Music, 2. Maths ....
# A choice must also be available for the user to exit the program
# A message using the print function must be display as per the user choice

# Display the menu
print("Menu:")
print("1. Music")
print("2. Maths")
print("3. Science")
print("4. Exit")

# Get user input for choice
choice = input("Enter your choice: ")

# Convert choice to integer
choice = int(choice)

# Check user's choice
if choice == 1:
    print("You chose Music.")
elif choice == 2:
    print("You chose Maths.")
elif choice == 3:
    print("You chose Science.")
elif choice == 4:
    print("Exiting the program.")
else:
    print("Invalid choice. Please choose a valid option.")


#ToDo: Task 2
# Use if else to find item(a specific number) from a list
numList = [56, 78, 100, 45, 88, 71]

numList = [56, 78, 100, 45, 88, 71]
specific_number = 100  # Change this to the number you want to find

if specific_number in numList:
    print(f"{specific_number} exists in the list.")
else:
    print(f"{specific_number} does not exist in the list.")
