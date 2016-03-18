"""
File: smoothed_Heaviside.py

Copyright (c) 2016 Grayden Blanchard

License: MIT

Testing to see if the function is running correctly
"""

import math


def H_eps(x, eps = 0.01):
    if x < -eps:
        result = 0
    elif x <= eps:
        x_over_eps = (x/eps)
        result = 0.5 * (1 + x_over_eps + (math.sin(math.pi *x_over_eps))/math.pi)
    else:
        result = 1
    return result

def test_H_eps():
    x = 0.01
    x_over_eps = (x/0.01)
    if H_eps(-2) != 0:
        print "The function is not running properly1."
    if H_eps(-0.01) != 0.5 * (1 + (-0.01/0.01) + (math.sin(math.pi *(-0.01/0.01)))/math.pi):
        print "The function is not running properly2."
    if H_eps(0) != 0.5 * (1 + (0/0.01) + (math.sin(math.pi *(0/0.01)))/math.pi):
        print "The function is not running properly3."
    if H_eps(0.01) != 0.5 * (1 + (0.01/0.01) + (math.sin(math.pi *(0.01/0.01)))/math.pi):
        print "The function is not running properly4."
    if H_eps(1) != 1:
        print "The function is not running properly5."
    else:
        print "The function is fine."

test_H_eps()
