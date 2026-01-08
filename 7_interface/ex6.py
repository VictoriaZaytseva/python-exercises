# -----------------------------------------------------------------------------
# Exercise 6 - "The Split"
#
# After some discussion, Mary realizes that the approach taken in exercise 5
# is a bit weird and muddled.   Part of the problem is the Result instance is
# being used to represent two completely different things--a normal
# result and an error result.  Perhaps it would be better to split these
# into two different classes--each representing a different outcome.
# For example:

class Result:
    __match_args__ = ('_value',)
    def __init__(self, value):
        self._value = value

    def unwrap(self):
        raise NotImplementedError()

class Ok(Result):
    def unwrap(self):
        return self._value

class Error(Result):
    def unwrap(self):
        raise self._value

# -----------------------------------------------------------------------------
# Part 1:
#
# Fill in the missing details of the following after() function.  It
# returns a Result as before, but it should refine the outcome so
# that either Ok() or Error() is returned.  An attached test illustrates.

import time

def after(seconds:float, func) -> Result:
    if(seconds < 0):
        return Error(ValueError("seconds must be non-negative"))
    else:
        time.sleep(seconds)
        # You implement this 
        try:
            result = func()
            return Ok(result)
        except Exception as e:
            return Error(e)

def test_after():
    def add(x, y):
        return x + y

    r = after(1, lambda: add(2, 3))
    assert isinstance(r, Ok), "Should have returned Ok"
    r = after(1, lambda: add(2, "three"))
    assert isinstance(r, Error), "Should have returned Error"

test_after()     # Uncomment

# -----------------------------------------------------------------------------
# Part 2:
#
# Splitting the result into two classes refines the result, but also
# opens up the possibility of case-analysis.  Consider the following
# revised version of a function from Exercise 4.

import math
def f(delay, value):
    r = after(delay, lambda: math.sqrt(value))
    if isinstance(r, Ok):
        print("It worked:", r.unwrap())
    elif isinstance(r, Error):
        print("It failed!")

# Try these examples:
#
f(1, 1)
f(1, -1)
f(-1, 1)
#

# -----------------------------------------------------------------------------
# Part 3:
#
# Upon seeing the code in part 2, Mary's mind wanders to structural
# pattern matching--a feature added to Python 3.10.   Could the function
# in Part 2 be rewritten like this instead?

def g(delay, value):
    match after(delay, lambda: math.sqrt(value)):
        case Ok(value):
            print("It worked:", value)
        case Error(exc):
            print("It failed:", exc)

# Try the above function to see what happens
#
g(1, 1)
g(1, -1)
#
# Okay, it doesn't quite work.  However, it can be made to work if
# you add a `__match_args__` attribute to the `Result` class like this:
#
# class Result:
#     __match_args__ = ('_value',)
#    def __init__(self, value):
#        self._value = value
#
# Make this change and retry the above test.

# -----------------------------------------------------------------------------
# Part 4:
#
# The refinement.  Can pattern matching further refine exceptions?  For
# example, as shown in this code?

def h(delay, value):
    match after(delay, lambda: math.sqrt(value)):
        case Ok(value):
            print("It worked:", value)
        case Error(TypeError()):
            print("It failed: type error")
        case Error(ValueError()):
            print("It failed: bad value")
        case Error(e):
            raise e

# Try the above code with these examples:
#
h(1, 1)
h(1, -1)
h(1, "one")
h(-1, 1)
del math
h(1, 1)
#

# -----------------------------------------------------------------------------
# Challenge:
#
# In the above code for h(), the `case Error(e)` binds the exception to the
# variable `e`.  Is there any way to similarily bind the exception to a
# variable in the `case Error(TypeError()` and `case Error(ValueError())`
# cases?  For example:

def k(delay, value):
    match after(delay, lambda: math.sqrt(value)):
        case Ok(value):
            print("It worked:", value)
        case Error(TypeError()):
            print("It failed:", e)   # ??? where to get e? (the exception)
        case Error(ValueError()):
            print("It failed:", e)   # ??? where to get e? (the exception)
        case Error(e):
            raise e

        # Hint: How do you get the exception value with try-except?

# -----------------------------------------------------------------------------
# Discussion:
#
# Are we even coding in Python?   For most of Python's existence, exception
# handling has been the preferred mechanism for error handling.   In this
# example, we have converted almost everything into structural pattern
# matching? Is this even a good idea?  It's hard to say.
#
# Maybe the ultimate test is whether or not you could read the above code
# and explain what's happening to a coworker.

