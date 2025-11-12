"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        return None

def hypotenuse(a,b):
    math.hypot(a,b)

def add(a, b): 
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    try:
        return b/a
    except ZeroDivisionError:
        return None

def log(a, b):
    try:
        return math.log(b,a)
    except ValueError:
        return None

def exp(a, b):
    return pow(a,b)

