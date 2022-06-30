import numpy as np

# fahrenheit to celsius
def fToC(f):
    c = (f - 32) * 5/9
    return c

# celsius to fahrenheit 
def cToF(c):
    return c * 9/5 + 32


# Abritrary A to B replacement
def AToB(A):
    return A * 9/5 + 32
