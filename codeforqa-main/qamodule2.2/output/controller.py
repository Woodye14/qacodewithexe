from service import *

def runApp():

    print("""
    Welcome to woodys employee reader! 
    Please select an option from below: 
    1. add an employee
    2. read all employees
    3. update an employees name
    4. delete an employee
    """
    )
    running = True

    # Does a thing while a condition is true
    while running:
        choice = int(input("Please select a choice using a number: "))
        if choice == 1:
            insertEmployee()
        elif choice == 2:
            print(readAllEmployees())
        elif choice == 3:
            updateName()
        elif choice == 4:
            deleteName()
        else: 
            print("Incorrect choice.. try again..")

        end_choice = input("Do you want to query more data Y / N: ")
        if end_choice.upper() == "N":
            running = False

runApp()

conn.commit()