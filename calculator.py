'''
The start up method determines what operation the user wants to perform!
+ - x /

This method utilizes conditional statements and recursion
'''
def startup():
    rerun = "bababa" #filler
    print("Calculator boot:\nWhich operation? (+ , -, x, /)") #tells the user to enter an operator
    selected_operation = input() #gets that info
    if selected_operation is '+':
        addition() #calls addition method
    elif selected_operation is '-':
        subtraction() #calls subtraction method
    elif selected_operation is 'x':
        multiplication() #calls multiplication method
    elif selected_operation is '/':
        division() #calls divison method
    else:
        print("Invalid operator, try again")
        startup() #recurses back instead of continuing to the conditional
    #condtional sequence for if the user wants to run the calculator again
    rerrun = input("Would you like to run again?\nEnter: 'Yes' or 'Y'")
    if rerrun == "Yes":
        startup()
    elif rerrun == 'Y':
        startup()
    else:
        print("Exiting")

#adds two numbers together
def addition():
    val1 = float(input("Enter in value 1\n"))
    val2 = float(input("Enter in value 2\n"))
    print(val1 + val2)

#subtracts two numbers
def subtraction():
    val1 = float(input("Enter in value 1\n"))
    val2 = float(input("Enter in value 2\n"))
    print(val1 - val2)

#multiplies two numbers
def multiplication():
    val1 = float(input("Enter in value 1\n"))
    val2 = float(input("Enter in value 2\n"))
    print(val1 * val2)

#divides two numbers
#contains condiitonal logic that that detects if the user is trying to divide by 0
#recalls itself if this is the case
def division():
    val1 = float(input("Enter in value 1\n"))
    val2 = float(input("Enter in value 2\n"))
    if val2 == 0:
        print("You can't divide by 0\n")
        division() #recurse recurse recurse
    else:
        print(val1 / val2)




