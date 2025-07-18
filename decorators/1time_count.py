import time # Imports the time module to measure execution time

def timer_decorator(orginal_func):  # Defines the decorator that takes a function as input
    def wrapper():      # Defines a wrapper function to add extra behavior around original function
        start_time = time.time()
        orginal_func()  
        end_time = time.time()
        print(f"Time required is {end_time - start_time :.4f}s")      #:.4f Is used to denote decimal extension
    return wrapper  # Return is given to the time decorator so that it can be used later on


@timer_decorator    # Applies the decorator to my_function
def my_func():
    print("Wait for some time")
    time.sleep(2)

my_func()   # Calls the decorated function (wrapper runs here)