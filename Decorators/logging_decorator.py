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

result = add(2, 3)
