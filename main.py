from functools import wraps
from time import time

def decorator(func) :

    @wraps(func)
    
    def wrapper(*args , **kwargs) :

        t1 = time()

        result  = func(*args , **kwargs)

        t2 = time()

        print(f"This function took {t2 - t1} seconds to load")

        return result

    
    return wrapper

@decorator
def add(a, b) :

    print(a + b)


add(4,5)

number = 9 
number = 8

print("Ready to rebase")

print("new changes")


print("lets work on the gihub")