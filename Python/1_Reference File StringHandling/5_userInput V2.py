fname    = input("Enter you full name: ")
address   = input("Enter your address: ")
interest = input("Enter your interest: ")
age      =    int(input("Enter your age: "))

"Make"
"To Do: Task 1: Use the code above to ask for user input and then save it to a file called userDetails.txt"


# create a dictionary
userData =  {
    "Fullname":fname,
    "Address":address,
    "Interest":interest,
    "Age":age
}
print(userData["Fullname"])
 
with open('Python/1_Reference File StringHandling/userDictionary.txt',"a") as dictData:
    for aKey,aValue in userData.items():
        dictData.write(f"{aKey}, {aValue}")    
     
    
"Further reading"
# https://www.w3schools.com/python/python_file_handling.asp

