# Decorator definition that takes a function as argument
def log_function_call(func):
    # Taking 2 arguments (x, y) and prints before and after calling the decorated function
    def wrapper(x, y):
        print(f"Calling {func.__name__} with {x} and {y}")
        result = func(x, y)
        print(f"Result: {result}")
        return result # Returns the result of the decorated function
    return wrapper # Returns decorated function

@log_function_call # decorate a function
def add(x, y):
    return x + y

@log_function_call # decorate a function
def subtract(x, y):
    return x - y

@log_function_call # decorate a function
def multiply(x, y):
    return x * y

@log_function_call # decorate a function
def divide(x, y):
    return x / y

while True:
    list_of_ops = ['add', 'subtract', 'multiply', 'divide']
    operation = input("Enter operation: ")

    if operation == 'quit':
        break

    if operation not in list_of_ops:
        print("Invalid operation! Choose from the list below:")
        for op in list_of_ops:
            print(op)
        continue

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    
    if operation == 'add':
        add(x, y)
    elif operation == 'subtract':
        subtract(x, y)
    elif operation == 'multiply':
        multiply(x, y)
    elif operation == 'divide':
        divide(x, y)
    else:
        print('No')





# result = add(2, 3)
# print(result)

