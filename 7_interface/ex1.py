# ------------------------------------------------------------------------------
# Exercise 1
#
# You first exercise is to make sure you know how to use the function with
# a simple "Hello World" example.
# -----------------------------------------------------------------------------

from after import after

def greeting():
    print('Hello World')

# How do you use the greeting() function with the after() function?
# That is, have the after() function call greeting() after 10 seconds.
after(10, greeting)