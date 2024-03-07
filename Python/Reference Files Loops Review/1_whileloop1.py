"""
Use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program

You will need a while statement:
When your program needs to repeat actions, while a condition is satisfied
"""

"To Do: Predict, then Run, and then Investigate"

number = 4
print("Guess a number between 1 and 10")
numGuess = int(input("Guess a number between 1 and 10: "))
while numGuess != number:
   numGuess = int(input("Incorrect\nGuess a number between 1 and 10"))
print(f"You guessed {numGuess} is correct")




"To Do: Task1: Add comments to the code to explain what the while loop is doing"
number = 4 #initialises the variable number and gives it the value of 4
print("Guess a number between 1 and 10: ") #prints the message to prompt a guess
numGuess = int(input("Guess a number between 1 and 10: ")) #takes input from user between 1 and 10 and converts to integer and stores it as variable 'numGuess'
while numGuess != number: #starts while loop that continues until user's guess equals 'number'
   numGuess = int(input("Incorrect\nGuess a number between 1 and 10:")) #inside while loop, if user guess is wrong, it prompts the user to guess again
print(f"You guessed {numGuess} is correct") #prints message saying user has guessed correct.

"Further reading on python while statements"
# https://www.w3schools.com/python/ref_keyword_while.asp