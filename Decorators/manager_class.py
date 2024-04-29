
import sys
# Define a class called manager that will manage different actions

class Manager:
    # Initialize and empty dictonary to store acion names and their functions
    def __init__(self):
        self.actions = {}

    # A method to assigne afunction to a spesific action name
    def assign(self, name):
        # This method returns a decorator which will be used to decorate a function
        def decorate(cb): # CallBack (cb)
            # Store the call back function in the dictionary with given name
            self.actions[name] = cb
        return decorate
    
    # A method to execute a function associtated wuth a given action name
    def execute(self, name):
        # Chec if the action name exists in the dictionary
        if name not in self.actions:
            print("Action not defined!")
        else:
            # If the action is defined, execute the associated function, passing 'self' (the manager instance)
            self.actions[name](self)

# Create an instance of Manager
manager = Manager()

# @manager.assign("print_yes")
# def printer(manager):
#     print("Yes")

# # Execute the action associated with the name "print_yes"
# manager.execute("print_yes")


# Function to handle adding two numbers

@manager.assign("add")
def add(manager):
    a = float(input("Enter first number: "))
    b = float(input("Enter first number: "))
    print(f"The sum of {a} and {b} is {a + b}")

# Function to handle subtraction two numbers

@manager.assign("subtract")
def add(manager):
    a = float(input("Enter first number: "))
    b = float(input("Enter first number: "))
    print(f"The sum of {a} and {b} is {a - b}")

# Function to exit the program
@manager.assign("exit")
def exit_program(manager):
    print("Exiting the program")
    sys.exit(0)


def main_menu():
    print("\n Welocme to the simple calculator!")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. exit")
    choice = input("Enter your choice (1, 2, 3): ")
    return choice

while True:
    choice = main_menu()
    if choice == "1":
        manager.execute("add")
    elif choice == "2":
        manager.execute("subtract")
    elif choice == "3":
        manager.execute("exit")
    else:
        print("Wrong inputs!")
        sys.exit(1)

