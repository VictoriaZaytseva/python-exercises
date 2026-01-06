# -----------------------------------------------------------------------------
# Exercise 3
#
# Mary has been further pondering the usage of the after() function.  Should
# she make it easier for users to supply arguments to the provided function?
# For example, to simplify the problem addressed in Exercise 2.
#
# This is a surprisingly nuanced problem because Python functions can
# be called in many different ways.  For example:
#
#     def func(x, y z):
#         ...
#
#     func(1, 2, 3)          # Positional arguments
#     func(x=1, y=2, z=3)    # Keyword arguments
#     func(1, z=3, y=2)      # Position/keyword argument mix
#
#     args = (1,2,3)
#     func(*args)            # Passing a tuple as positional arguments
#
#     kwargs = { 'x': 1, 'y':2, 'z': 3 }
#     func(**kwargs)         # Passing a dict as keyword arguments
#
# To make matters even more complicated, a function can force the
# use of keyword arguments:
#
#     def func(x, *, y):
#         ...
#
#     func(1, 2)                # Error. y not supplied by keyword
#     func(1, y=2)              # Ok!
#
# Plus, there are functions that accept any number of positional
# or keyword arguments:
#
#     def func(*args, **kwargs):
#         ...
#
# And in more recent versions of Python, positional-only functions:
#
#     def func(x, y, /, z):
#         ...
#
#     func(1, 2, 3)     # OK
#     func(1, 2, z=3)   # OK
#     func(1, y=2, z=3) # ERROR.
#
# -----------------------------------------------------------------------------

import time

# To explore all of the above options, Mary has written 3 variants of
# the after() function.

# Option 1: Original implementation. No arguments. 
def after_1(seconds, func):
    time.sleep(seconds)
    return func()

# Option 2: Extra arguments are passed as explicit tuple/dict
def after_2(seconds, func, args=(), kwargs={}):
    time.sleep(seconds)
    return func(*args, **kwargs)

# Option 3: Extra arguments provided via *args and **kwargs
def after_3(seconds, func, *args, **kwargs):
    time.sleep(seconds)
    return func(*args, **kwargs)

# -----------------------------------------------------------------------------
# Part 1:
#
# You first task is to show how you would go about using the above
# functions with the add() function from before--using both positional
# and keyword arguments.

def add(x, y):    # You are NOT allowed to change this function 
    print(f'Adding {x} + {y} -> {x + y}')
    return x + y


# You must fix each of these to work correctly.  Uncomment each line.
after_1(1, lambda: add(2,3))        # FIX
after_1(1, lambda:add(x=2, y=3))   # FIX. Must keep kwargs

after_2(1, add, args=(2,3))        # FIX
after_2(1, add, kwargs={'x':2, 'y':3})   # FIX. Must keep kwargs

after_3(1, add, 2, 3)        # FIX
after_3(1, add, x=2, y=3)   # FIX. Must keep kwargs

# -----------------------------------------------------------------------------
# Part 2: 
#
# Ben looks at the code and perversely asks what happens if you try to
# use `after()` to call itself?
#
# "What kind of question is that?!?", exclaims Mary.
#
# "Well, if your goal is to make the function general purpose, then
# surely it should be capable of calling itself", explained Ben.
# "For example, something like this."

#    after_1(1, lambda: after_1(1, lambda: add(2,3)))
#    after_1(1, lambda: after_1(seconds=1, func=lambda: add(2, 3)))

# Make these work.  Note: Our focus here is on the "after_" function,
# not on the add() function.

#after_2(1, after_2, args=(1, lambda: add(2,3)))                 # FIX

#after_2(1, after_2, kwargs={'seconds':1, 'func':lambda: add(2, 3)})

after_3(1, after_3, 1, add, 2, 3)                # FIX.
        #after_3(1, add(2, 3)))                # FIX.
# after_3(1, after_3(seconds=1, func=add(2,3)))    # FIX. Must use kwargs for seconds/func


# -----------------------------------------------------------------------------
# Part 3:
#
# Your task is as follows. Decide which approach Mary should use going
# forward and code it into a final after() function below.  If you
# think Mary should do something different than any of the proposed
# solutions, code that instead.  In all cases, be prepared to explain
# your reasoning when you unleash this code on your coworkers...
# number 1 is the best
def after(seconds, func):
    # Final implementation.  You decide what it is.
    time.sleep(seconds)
    return func()


