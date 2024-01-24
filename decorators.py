def mydecorator(function):

    def wrapper(*args, **kwargs):

        returned_value =  function(*args, **kwargs)
        print("I am Decorating your function")

        return returned_value

    return wrapper

@mydecorator
def hello_world(person):
    return f"Hello {person}"


# print(hello_world("Mike"))

# Practical example #1 - Logging

def logged(function):
    def wrapper(*args, **kwargs):

        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value
    
    return wrapper

@logged
def add(x, y):
    return x + y

# print(add(10,20))
        


# Practical example #2 - Logging
import time 

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__

        print(f"{fname} took {after-before} seconds to execute")

        return value

    return wrapper

@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result

myfunction(1000)