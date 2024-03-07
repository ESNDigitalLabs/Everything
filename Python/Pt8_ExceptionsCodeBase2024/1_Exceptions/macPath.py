import logging
import os
"To Do: Predict, then Run, and then Investigate"
#different logging methods and severity
 
#  Python/Pt8_ExceptionsCodeBase2024/1_Exceptions
filepath = os.path.join(r"Python", "Pt8_ExceptionsCodeBase2024","1_Exceptions","file3.log" )
logging.basicConfig(filename=filepath, level=logging.DEBUG)
 
try:  # attempt to run the indented code block
    num1 = int(input(("Enter your first number: ")))
    num2 = int(input(("Enter your second number: ")))
    answer = num1 / num2
    #Output for developer/what the developer see
    logging.info(f"Divided {num1} / {num2} = {answer}")
       
except ZeroDivisionError:  # handles exception if code in try block fails
    #Output for user/what the user see
    print("You can't divide a number by zero")
    logging.warning("User attempted to divide by zero")
   
finally:
    print("Closing....")