"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""



# import the datetime library/class/module
import datetime


"To Do: Predict, then Run, and then Investigate"


print("None while Loop output")
dateTime = datetime.datetime.now()
print(dateTime.strftime("%H:%M:%S"))


"To Do: Task 1" 
" study the output of the code above and the output in in the while loop below, and use the links provide to answer"

" What is the while loop doing?"

#This is a while loop with the condition True, which means it will run indefinitely until explicitly stopped.

" add comment to explain what you understand the 'datetime.datetime.now().strftime('%H:%M:%S')'"

# Within the loop, it retrieves the current time using datetime.datetime.now() and formats it as hours, minutes, and seconds 
# using strftime("%H:%M:%S"). Then, it prints this formatted time to the console. 


" add comment to explain what you understand the 'end='"

# 'end' is used to specify what character or string to append at the end of the printed output. 
# By default, the end parameter is set to "\n", which means a newline character is added after the printed content. 
# However, you can change this behavior by passing a different value to the end parameter.

" add comment to explain what you understand the '\r' "

# "\r" is a special escape sequence representing a carriage return character. A carriage return character (\r) moves the cursor 
# or printing position to the beginning of the current line without advancing to the next line. This allows you to overwrite the 
# existing content on the current line in the console or terminal.

# When used in a string within a print() function, "\r" instructs Python to move the cursor to the 
# beginning of the current line after printing the content. This can be useful for creating dynamic or 
# updating displays, such as progress bars, live counters, or in this case, a continuously updating clock.

# https://www.w3schools.com/python/gloss_python_escape_characters.asp

" add comment to explain what you understand the 'end=' is used for"
" add comment to explain what you understand the '\r' is used for "
" What will output if you remove  , end='\r'  from the while loop"

# The end="\r" parameter ensures that each new print statement overwrites the previous one on the same line in the console, 
# creating the appearance of a continuously updating clock.


print("while Loop output")
while True:
    print(datetime.datetime.now().strftime("%H:%M:%S"), end=" ")

    time.sleep(1)

# The time.sleep(1) function call means that the program will pause execution for 1 second 
# (1, representing one second) before continuing to execute the next line of code.

# In Python, time.sleep() is a function from the time module that allows you to pause the execution 
# of your program for a specified amount of time. The argument you provide to time.sleep() 
# specifies the duration of the pause in seconds. In this case, time.sleep(1) pauses the program for one second.

# This function is commonly used when you need to introduce a delay in your code, 
# such as when you want to control the rate of execution, simulate real-time processes, or synchronize actions 
# with external events.

"Further reading on python while statements"
# https://www.w3schools.com/python/ref_keyword_while.asp
# https://www.w3schools.com/python/python_ref_keywords.asp
# https://www.w3schools.com/python/python_reference.asp