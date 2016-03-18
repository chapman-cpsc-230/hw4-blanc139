"""
File: Heavyside.py
Copyright (c) 2016 Grayden Blanchard
License: MIT
Write a function to test the value of a number, and then test the function.
"""

def H(x):
    if x < 0:
        value  = 0
    if x >= 0:
        value = 1
    return value

def test_H():
    if H(-10) != 0:
        print "The function is not running correctly."
    elif H(-10 ** -15) != 0:
        print "The function is not running correctly."
    elif H(0) != 1:
        print "The function is not running correctly."
    elif H(10 ** 15) != 1:
        print "The function is not running correctly."
    elif H(10) != 1:
        print "The function is not running correctly."
    else:
        print "The function is running correctly."



test_H()
