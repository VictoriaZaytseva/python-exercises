# configparse.py
#
# Your task:  Copy the code from config.py here, clean it up,
# and try to make a nicely readable configuration parser.
#
# The code should consist of two parts--general purpose
# functions related to writing parsers, followed by
# specific definitions related to the problem of parsing
# config files.


# -- General purpose "parsing" functions
#
#    matching_predicate()
#    match_literal()
#    sequence()
#    reduce()
#    choice()
#    zero_or_more()
#    whitespace()
#    token()
#    tokenize()

...

# -- Specific definitions related to parsing config files
#
#    parse_integer
#    parse_decimal
#    parse_number
#    parse_setting
#    parse_settings

...

# -- Write a "main" function that just does everything

def parse_config(text):
    ...

# -- Challenge problem
#
# Modify the config parser to allow lists to be defined as a value.  For
# example:
#
#      values = [1, 2, 3.5]
#
# Nested lists should also be ok
#
#      values = [1, 2, [3, 4, [5, 6], 2.5]]
#

# -----------------------------------------------------------------------------
# DISCUSSION:
#
# There's a whole different mindset to programming at work in this
# project.  Instead of directly coding a parsing function built-in on
# low-level Python primitives, the problem of parsing itself is being
# deconstructed into high-level abstractions (sequencing, repetition,
# choice, reduce).   The problem at hand is then elegantly expressed
# in terms of these abstractions.
#
# The general technique being used here involves the concept of "function
# combinators." A combinator is a function that accepts functions as
# inputs and produces a new function as output.  Think of it as a kind
# of code generator.  
#
# To make it all work, it is critically important to make functions
# easily composable.  If you carefully study the solution, you'll
# find that everything is manipulating and creating functions with
# identical a calling signature and return convention (e.g., look at the
# internal parse() functions and notice that they're all the same).
# This uniformity is what makes it possible to compose combinations
# of sequence(), choice(), reduce(), zero_or_more(), and related
# functions in almost any configuration.


