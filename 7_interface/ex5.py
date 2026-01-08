# -----------------------------------------------------------------------------
# Exercise 5
#
# One challenge in returning results is that there are actually two
# kinds of results from any Python function--a value returned by the
# "return" statement or an exception raised by the "raise" statement.
# One possible design for code that wants to communicate the "result" of
# a computation is to place both possible outcomes inside a combined
# Result object like this:

class Result:
    def __init__(self, value=None, exc=None):
        # Use value for a result produced by "return"
        # Use exc for an exception produced by "raise"
        assert (value is None) or (exc is None)
        self._value = value
        self._exc = exc

    def unwrap(self):
        # Produce the enclosed result
        if self._exc:
            raise self._exc
        else:
            return self._value

# The Result object might be used like this:
#
#     result = after(10, func)     # Always returns a Result
# 
# To see the actual result, you call "unwrap" like this:
#
#   try:
#       value = result.unwrap()
#   except Exception as e:
#       print("An error occurred")
#

# -----------------------------------------------------------------------------
# Part 1:
#
# Fill in the missing details of the following after() function so
# that it uses Result.  Then, verify that the supplied test works.

import time

def after(seconds:float, func) -> Result:
    if seconds < 0:
        return Result(exc=ValueError("seconds must be non-negative"))
    time.sleep(seconds)
    # You implement this 
    try:
        result = func()
        return Result(value=result)
    except Exception as e:
        return Result(exc=e)

# Example
def add(x, y):
    print(f'Adding {x} + {y} -> {x + y}')
    return x + y

# The following test shows the desired behavior
def test():
    r = after(5, lambda: add(2, 3))
    assert r.unwrap() == 5

    r = after(5, lambda: add('2', 3))
    try:
        a = r.unwrap()
        print('Bad! Why did this work?')
    except TypeError as err:
        print('Good!')

# Uncomment to test
test()

# -----------------------------------------------------------------------------
# Part 2
#
# In the previous exercise, we were concerned with the behavior of various
# error cases.  Your job here is to revisit some of those tests.

import math

# Try the following failure scenarios with your new after() function
#
r = after(1, lambda: math.sqrt(-1))   
r = after(-1, lambda: math.sqrt(1))
r = after(1, math.sqrt(-1))
#
# Ponder: Is the implementation clearly separating all of these
# failure cases?

# -----------------------------------------------------------------------------
# Part 3
#
# A coding style debate has erupted in the office.  Ben argues that
# the following is an appropriate and convenient way to use the
# after() function:
#
#    try:
#        value = after(delay, func).unwrap()
#        print("It worked:", value)
#    except ValueError:
#        print("It didn't work")
#
# Mary counters that it would be much better to structure such code
# like this:
#
#    r = after(delay, func)
#    try:
#        value = r.unwrap()
#        print("It worked:", value)
#    except ValueError:
#        print("It didn't work")
#
# What is your opinion on this debate?



