# https://github.com/iiTzFreddy/lab11-FR-JW
# Partner 1: Freddy Rives
# Partner 2: John Watson
# First example
import math
def add(a, b): return a + b

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)


def subtract(a, b): return a - b

def mul(a, b): return  a * b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    return b/a

def logarithm(a, b):
    if a < 0:
        raise ValueError
    return math.log(b,a)

def exp(a, b): return a ** b

