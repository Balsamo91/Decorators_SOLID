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
