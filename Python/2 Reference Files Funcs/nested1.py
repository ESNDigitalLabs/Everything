"""Nested selection/nesting is when a selection block(if/else)
is placed within another if,  else selection block"""

"Modify"
"To Do: Task 1: Using if elif and else"
# Exercise: Use the notes/comments after the variable initialisation to create a nested if statement that will:

# 1. Check 'userAge' against the 'ageLimit

# Initialize variables
userAge = 25  # The age of the user
ageLimit = 18  # The minimum age required


# 1.1 When the 'userAge' is not greater that the 'ageLimit then display a suitable message
userAge = int(input(" how old are you?:"))
if userAge < ageLimit:
    print("You are just a baby, too young for this.")
elif userAge == ageLimit:
    print("You are exactly the minimum age required.")
else:
    print("Congratulations Old One!")

# 2. When the 'userAge' is greater than the 'ageLimit' then execute another code block( that asks user to provide a code, see 2.1 below)

userAge = int(input(" how old are you?:"))
if userAge > ageLimit:
        user_code = input("Please provide the code: ")
        print("Thank you for providing the code.")
        if userAge < ageLimit:
            print("You are just a baby, too young for this.")
        elif userAge == ageLimit:
             print("You are exactly the minimum age required.")
else:
    print("You are not old enough to proceed.")    


# 2.1 create a variable called 'userCode' to ask for user input and compare the value provided(userCode) with the value held in passCode

# 3. When the 'userCode' is not the same as 'passCode' display a suitable message

# 3.1 When the 'userCode' is the same as 'passCode' display a suitable message



userAge = int(input("Enter your age: "))

ageLimit = 16

passCode = "Bootcamp"

# compare if the value held in userAge is greater than the value held in ageLimit


# execute the code block below if the comparison returns true


# nested if will execute if the codition above is true (if userAge > ageLimit:)

 # This else will execute if nested if condition above is false (userCode is not equal to passCode:)

# This else will execute if the if condition above is false ( userAge is less than the ageLimit:)

"To Do: Q&A"
"What do you think is the equivalent of JS nested if in python?"



name = "Erica Samba-Ngoie"
for letter in name:
    print(letter)

