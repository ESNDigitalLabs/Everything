# There are four modes for opening a file:​

# r for only reading files​

# w for only writing to files​ and creating the file if it does not exists but overwrites existing file contents

# a for adding to an existing file​

# r+ for reading and writing files

import os

filePath = 'Python/1 Reference File FileHandling/'

if os.path.exists(filePath):

# with open('Python/1 Reference File FileHandling/file4.txt',"r+") as filePath1:# folder/folder/filename
#     print(filePath1.read()) #read from fiile
#     readContents = filePath1.read()
#     print(readContents)
#     contents ="\nHas this updated - All this works"
#     filePath1.write(contents) #write to file 

# try this code to open the file, read and display its contents in the terminal
    try:
        with open(filePath +'/file4.txt',"r+") as filePath1: # folder/folder/filename
        
            readContents = filePath1.read()
            print(readContents)
            contents ="\nHas this updated?"
            filePath1.write(contents) #write to file 
    

# handle (FileNotFoundError) what is not found
    except IOError as e:
        print(f"Error occured because: {e}")

else:
    print("File not found. Please check the file path")



"To Do: Task 1: Modify the code above to"
# Read the contents from your file (yourName.txt) and write to your file  
# use the with the correct mode and ensure you use both the read and the write() methods to perform their respective 
# operations


# [11:28] Abdul Jalloh
# import os
 
# filepath = 'Pt7_FilesDictsCodeBase2024/1 Reference File FileHandlings'
 
# if os.path.exists(filepath):
#     # try this code to open the file, read and display it contents in the terminal
#     try:
#         with open(filepath +'/file4.txt',"r+") as filePath1:# folder/folder/filename
#             # print(filePath1.read()) #read from fiile
#             readContents = filePath1.read()
#             print(readContents)
#             contents ="\nGoodbye"
#             filePath1.write(contents) #write to file
   
#     # handle (FileNotFoundError) : this error occurs if the file is not found
#     except IOError as e:
#         print(f"Error occured because: {e}")
 
# else:
#     print("File not found. Please check the file path")
 