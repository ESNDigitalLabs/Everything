fname    = input("Enter you full name: ")
address   = input("Enter your address: ")
interest = input("Enter your interest: ")
age      =    int(input("Enter your age: "))

"Make"
"To Do: Task 1: Use the code above to ask for user input and then save it to a file called userDetails.txt"

with open('Python/1 Reference File FileHandling/userDetails.txt',"a") as data:

    "method  1"
    data.write("\n"+fname+" "+address+ " "+interest+" "+ str(age))
    
    "method 2"
    fileContent = (f"\n{fname} {address} {interest} {age}")
    data.write(fileContent)
    
    
"Further reading"
# https://www.w3schools.com/python/python_file_handling.asp

file_path = '<your_filepath>.file_userData.txt' # put custom folder/file here
 
class UserData:
    def __init__(self, name, address, interest, age):
        self.name = name
        self.address = address
        self.interest = interest
        self.age = age
 
    def to_string(self):
        return f"Name: {self.name}\nAddress: {self.address}\nInterest: {self.interest}\nAge: {self.age}\n"
 
 
# input
fname = input("Enter your full name: ")
address = input("Enter your address: ")
interest = input("Enter your interest: ")
age = int(input("Enter your age: "))
 
# UserData object
user_data = UserData(fname, address, interest, age)
 
# Write user data to file
with open(file_path, 'w') as file:
    file.write(user_data.to_string())
 
print("written to file successfully.")
 
# did the task, using a Class and creating a new object 