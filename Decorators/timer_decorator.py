import time

def timer(func):
    # the wrapper takes unlimited number of arguments and key-value arguments
    def wrapper(*args, **kwargs):
        start_time = time.time() # Taking current time
        result = func(*args, **kwargs) # passing all arguments to decorated function
        end_time = time.time() # current time after running the function
        print(f"{func.__name__} ran in: {end_time - start_time} seconds.")
        return result
    return wrapper

@timer
def multiply(x, y):
    # time.sleep(2)
    return x * y

@timer
def sum(x, y):
    # time.sleep(2)
    return x + y

print(multiply(5, 3))
print(sum(5, 3))

#####################################

# FOR WINDOWS TO SHOW THE TIME INSTEAD OF THE 00 SECODS USE THE .PERF_COUNTER()

# import time

# def timer(func):
#     # the wrapper takes unlimited number of arguments and key-value arguments
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter() # Taking current time
#         result = func(*args, **kwargs) # passing all arguments to decorated function
#         end_time = time.perf_counter() # current time after running the function
#         print(f"{func.__name__} ran in: {end_time - start_time} seconds.")
#         return result
#     return wrapper

# @timer
# def multiply(x, y):
#     # time.sleep(2)
#     return x * y

# @timer
# def sum(x, y):
#     # time.sleep(2)
#     return x + y

# print(multiply(5, 3))
# print(sum(5, 3))