
"To Do: Task 2:Modify the code below to:"
# Read the contents of your file (yourName.txt) by replacing the:
# 1. "w" mode after the file path with the "r"
# 2. the write() method with the read method()
# 3. Unlike the write mode, no argument is required within the parenthesis of the read mode.
# 4. use print to display the contentsfrom the file you are reading 

# "Syntax :  varName = openMethod('pathtofolder/parthtofile//fileName.txt', 'w')"
# filePath1 = open('pathtofolder/parthtofile/fileName.txt', 'w') # folder/folder/filename
# filePath1.write("Python Programming")
# filePath1.close()

"method 1"
filePath1 = open('Python/1 Reference File FileHandling/erica.txt', 'r') # folder/folder/filename
# filePath1.read()
print(filePath1.read())
filePath1.close()

"method 2"
readContents = filePath1.read()
print(readContents)
filePath1.close()


"Further reading"
# https://www.w3docs.com/snippets/python/how-to-read-a-text-file-into-a-list-or-an-array-with-python.html