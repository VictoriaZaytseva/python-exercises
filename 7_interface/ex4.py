# -----------------------------------------------------------------------------
# Exercise 4
#

import time
from after import after

# "Oh my, it's full of fail."
#
# In experimenting with the after() function, Mary has noticed some odd
# quirks with respect to error handling.  Consider this function that
# internally uses after().

import math
def f(delay, value):
    try:
        value = after(delay, lambda: math.sqrt(value))
        print("It worked:", value)
    except ValueError as err:
        print("It failed")

# What happens when you try this function with these two inputs?
#
# f(1, -1)        # Uncomment
# f(-1, 1)        # Uncomment
#
# Confused, Mary now tries these operations using after() at the
# interactive REPL.
#
# >>> after(1, lambda: math.sqrt(-1))
# >>> after(-1, lambda: math.sqrt(1))
#
# "Oh, I see!"
#
# Your first task: Try all of the above experiments and contemplate
# the nature of exception handling that's occurring.  Then proceed
# to Part 1 below.

# -----------------------------------------------------------------------------
# Part 1:
#
# Mary has written two versions of the after() function that refine
# the reporting of exceptions. The purpose of this refinement is to
# more clearly separate exceptions originating from the supplied func()
# from exceptions related to bad usage of the after() function.

class AfterError(Exception):
    pass

def after_1(seconds, func):
    if seconds < 0:
        raise AfterError("seconds must be non-negative")
    time.sleep(seconds)
    return func()

def after_2(seconds, func):
    time.sleep(seconds)
    try:
        return func()
    except Exception as err:
        raise AfterError("function failed") from err

# Your task is to try the two examples from earlier with these
# functions and observe the results.   Do you have a preferred
# version?
#after_1(1, lambda: math.sqrt(-1))
#after_1(-1, lambda: math.sqrt(1))
#
#after_2(1, lambda: math.sqrt(-1))
#after_2(-1, lambda: math.sqrt(1))

# -----------------------------------------------------------------------------
# Part 2:
#
# A common programming mistake is to forget the lambda.  Try the
# following examples and observe the behavior
#
#after_1(1, math.sqrt(1))
#after_1(1, math.sqrt(-1))
#
#after_2(1, math.sqrt(1))
after_2(1, math.sqrt(-1))
#
# Do you have a preferred version?

# -----------------------------------------------------------------------------
# Part 3:
#
# Your task is to take everything you've learned above and write your
# preferred version of the after() function below.  If you are inclined,
# you can do something completely different.  However, you should be
# able to explain your reasoning in some way.
#
# I'm not looking for a specific "correct" answer here.  This is a tricky
# edge case and there are many ways one might think about it.

def after(seconds, func):
    # Modify to handle errors in the your most preferred way.
    time.sleep(seconds)
    return func()


# -----------------------------------------------------------------------------
# ASIDE: Unexpected issues with exception handling are a frequent source
# of very surprising program failures--sometimes at great cost.   Clarity
# around error handling is often a good idea in terms of code readability
# and debugging. 
