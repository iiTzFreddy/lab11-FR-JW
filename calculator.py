"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
import math
def add(a, b): a + b

def sub(a, b): a - b

def mul(a, b): a * b

def div(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        return None

def log(a, b):
    try:
        return math.log(b,a)
    except ValueError:
        return None# use math library + raise ValueError

def exp(a, b): return a ** b
