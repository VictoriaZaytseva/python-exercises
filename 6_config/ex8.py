# -----------------------------------------------------------------------------
# Exercise 8 - The Choice
#
# The sequence() function you wrote works by applying parsers in
# order, requiring all to match.  A different kind of strategy is to
# apply parsers in order, but stopping when a match is found.  This
# allows you to test for alternatives.
#

from ex7 import (parse_name, parse_integer, parse_decimal, parse_equal, parse_semi,
                 sequence, reduce)

# Define the function choice() that allows you to choose between
# different alternatives--picking the first one that matches.

def choice(*parsers):
    def parse(text, index):
        for parser in parsers:
            if m := parser(text, index):
                return m
    return parse

# Here's an example that shows how to use choice() to parse either a
# decimal or an integer number using the previously written
# parse_integer() and parse_decimal() functions.

parse_number = choice(parse_decimal, parse_integer)

def test_parse_number():
    assert parse_number("1234", 0) == ('1234', 4)
    assert parse_number("12.34", 0) == ('12.34', 5)
    assert parse_number("abc", 0) == None

test_parse_number()

# Show how you could use a combination of choice(), reduce(), parse_integer(),
# and parse_decimal() functions to convert numeric values into an appropriate
# Python type while parsing.

parse_converted_number = reduce(parse_number,
                              lambda v: float(v) if '.' in v else int(v))  #

def test_parse_converted_number():
    assert parse_converted_number("1234", 0) == (1234, 4)      # Note: int
    assert parse_converted_number("12.34", 0) == (12.34, 5)    # Note: float
    assert parse_converted_number("abc", 0) == None

test_parse_converted_number()   # Uncomment

# Define a more powerful version of parse_setting() that handles both
# kinds of numbers.

parse_setting = reduce(sequence(parse_name, parse_equal, parse_converted_number, parse_semi),
                       lambda r: (r[0], r[2]))

# New test, with different numeric types and conversion
def test_parse_setting():
    assert parse_setting("x=123;", 0) == (('x',123), 6)
    assert parse_setting("y=1.3;", 0) == (('y',1.3), 6)
    assert parse_setting("x 42", 0) == None   # Missing =
    assert parse_setting("x=42", 0) == None   # Missing ;
    assert parse_setting("x=y;", 0) == None   # y is not a number

test_parse_setting()   # Uncomment
