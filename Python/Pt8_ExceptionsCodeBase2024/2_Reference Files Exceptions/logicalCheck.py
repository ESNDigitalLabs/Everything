
#  while not valid_age or not valid_student_status:
 
# age = int(input("Enter your age: "))
# validStudent = input("Are you enrolled on Dev bootcamp (Y/N): ")
# print(f"Your age is {age} and enrolled {validStudent}")
 
def student_input():
    age = int(input("Enter your age: "))
    validStudent = input("Are you enrolled on Dev bootcamp (Y/N): ")
    return age, validStudent
 
 
studentData = True# boalean variable (toggle on/off)
while studentData:
    # assign the age and validStudent local variable to the student_input() function
    age , validStudent = student_input()
   
    # check if the age is valid
    getValidAge = 18 <= age <=25 #(18 and 25)
 
    # check for valid student status
    getValidStatus = validStudent == "Y" or validStudent == "N"
 
    if not getValidAge or not getValidStatus:
        print("Enter valid data")
    else:
        print("Valid data entered....")
        studentData = False # setting the studentData to false ensure we break out of the while loop







# [09:57] James Vethamony
# I made a simple little test of it as well, not sure if it's syntactically correct, though:
 
# valid_age = False
# valid_student_status = False
 
 
# while not valid_age or not valid_student_status:
 
#     age = int(input("Enter your age: "))
 
#     if age >= 19:
#         valid_age = True
#         print("Age is valid")
#     else:
#             print("Invalid age. You need to be 19 or older to enrol")
 
#     student_status = input("Are you a student? (y/n): ").lower()
 
#     if student_status == "y" or student_status == "n":
#         valid_student_status = True
 
#     else:
#         print("Invalid input! Please enter y or n.")
 
# print("End")
 
 