# -----------------------------------------------------------------------------
# Exercise 7 - The Reduction
#
# In exercise 6, the match_setting() function *almost* does what you need
# to replace the functionality of parse_setting().  However, the returned
# result includes unwanted information.  For example, instead of getting
# just the name and the value, you also get the '=' and ';' characters.
# How would you discard them?

from ex6 import parse_integer, parse_name, parse_equal, parse_semi, sequence, match_setting
from ex5 import match_literal

#
# One way to fix it would be to apply some kind of extra operation to
# the final output. For example, you could wrap the `match_setting()`
# function with some other function that extracted the interesting parts.
#
#      def parse_setting(text, index):
#          if not (mat := match_setting):
#              return None
#          parts, n = mat
#          return ((parts[0], int(parts[2])), n)
#
# Yes, this works, but it feels a bit clumsy.  Maybe it could also be
# generalized in some way.  Perhaps a `reduce()` function can be
# defined that takes a parser and a function as input.  As output,
# it returns the result of applying the function to the raw parsing
# data.

def reduce(parser, func):
    def parse(text, index):
        ... # You define
    return parse

# Here's an example showing how reduce() might work with integers.

assert parse_integer('123', 0) == ('123', 3)             
assert reduce(parse_integer, int)('123',0) == (123, 3)

# Show how you could define `parse_setting()` in terms of `reduce()` and
# `sequence()`.  Show that it passes all of the earlier tests.
# Hint: Use of a lambda function might be useful here.

parse_setting = reduce(sequence(...), ...)  # You define

def test_parse_setting():
    assert parse_setting("name=42;", 0) == (('name', 42), 8)
    assert parse_setting("x", 0) == None
    assert parse_setting("xyz 2", 0) == None         # Missing '='
    assert parse_setting("a=42", 0) == None          # Missing ';' at end

# test_parse_setting()       # Uncomment

# Challenge: Show how you can use a combination of reduce,
# parse_integer(), and sequence to parse a decimal number.  A decimal
# number consists of a series of digits, decimal point (.) and more
# digits.

parse_decimal = ... # You define

def test_parse_decimal():
    assert parse_decimal("123.45", 0) == ("123.45", 6)
    assert parse_decimal("123", 0) == None

# test_parse_decimal()     # Uncomment
