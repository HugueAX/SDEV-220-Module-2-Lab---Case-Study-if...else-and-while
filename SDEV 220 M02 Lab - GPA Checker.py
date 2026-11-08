# Raven Chason
# SDEV 220 M02 Lab - GPA Checker
# This app intends to accept Student names and GPAs to test whether the student qualifies
# for the Dean's List and Honor Roll

# Constants
deans_list_gpa = 3.5
honors_list_gpa = 3.25

# variables
student_first = ""
student_last = ""
student_gpa = ""

while True:
    # get student last name
    student_last = input("Please enter student's last name: ")

    # ZZZ ends program
    if student_last == "ZZZ":
        print("Goodbye.")
        break

    # get student first name
    student_first = input("Please enter student's first name: ")
    # get gpa and change to a float
    student_gpa = float(input("Please enter student's GPA: "))
    # dean's list comparison
    if student_gpa >= deans_list_gpa:
        print("Congratulations! You've made the Dean's List and the Honor Roll!\n")    
    # honor's roll comparison
    elif student_gpa >= honors_list_gpa:
        print("Congratulations! You've made the Honor Roll!\n")      
    else:
        print("Better luck next time!\n")
