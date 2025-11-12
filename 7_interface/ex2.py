# -----------------------------------------------------------------------------
# Exercise 2
#
# It seems that the after() function only works if you give it a
# function taking no arguments.  Is there any way to make it work with
# a function that takes any set of arguments?  Can you do this without
# making any code changes to the after() function or the function
# that's be supplied as input?

# You are NOT allowed to change any part of the after() function
from after import after

# You are NOT allowed to change any part of this function
def add(x, y):
    print(f'Adding {x} + {y} -> {x + y}')
    return x + y

# This doesn't work. Why?  Can you modify it to make it work?
result = after(10, add(2, 3))

# -----------------------------------------------------------------------------
# Thought Experiment:
#
# How would you use the after() function to carry out the following
# operation after 5 seconds?
#
#       add(add(1,2), add(3,4))
#
# Before you begin, what is this operation even doing?  What
# behavior do you expect to see?

# result = after(5, add(add(1,2), add(3,4)))    # Must modify!
