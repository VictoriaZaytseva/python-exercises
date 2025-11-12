# -----------------------------------------------------------------------------
# Exercise 10 - The Whitespace
#
# One problem with everything that's been written so far is that it
# has no accommodation for whitespace.  For example, what if there
# are spaces around the parts of a setting?  What if there are newlines?
#
#       speed    = 42  ;
#       size     = 9.5 ;
#       maxspeed = 1000;
#
# Whitespace should be ignored--it should have no impact on the final
# result.  However, it's also weird in that it can appear almost
# anywhere.
#
# CHALLENGE:  How would you go about incorporating whitespace into
# all of the machinery that has been created so far? 

from ex4 import matching_predicate, parse_integer, parse_name
from ex5 import parse_equal, parse_semi
from ex6 import sequence
from ex7 import reduce
from ex8 import choice, parse_number, parse_converted_number
from ex9 import zero_or_more

# There are a few subtle complications in solving this problem.
#
# 1. How do you go about matching optional whitespace?  Can it
#    be done using existing functions such as matching_predicate()?

whitespace = ...  # You define

def test_whitespace():
    assert whitespace("   ", 0) == ("   ", 3)
    assert whitespace("abc", 0) == ("", 0)     # Not an error. Just no whitespace.
    assert whitespace("", 0)    == ("", 0)

test_whitespace()

# 2. How do you ignore whitespace that's present? 
#    One way to approach this is to write a function called
#    token() that accepts a parser as input, but wraps it
#    in a way so that it ignores any leading whitespace.
#
#    Can you implement this entirely using functions such as
#    choice(), sequence(), and reduce()?

def token(parser):
    ... # You define

def test_token():
    assert token(parse_integer)("123", 0) == ('123', 3)
    assert token(parse_integer)("    123", 0) == ('123', 7)   # Leading whitespace ignored

# test_token()   # Uncomment.

# 3. Can whitespace handling be merged with an existing function
#    like sequence() in some way?   Can you do this in a way
#    where it's still convenient to define the parse_setting()
#    function?
#
#    One thought is to write a higher-level function tokenize()
#    that works like sequence(), but which wraps each parser
#    with the token operation above.

def tokenize(*parsers):
    ... # You define

parse_setting = ... # You define
parse_settings = ... # You define

def test_parse_settings_final():
    text = """
    speed    = 42 ;
    size     = 9.5 ;
    maxspeed = 1000;
    """
    assert parse_settings(text, 0) == ({'speed':42, 'size':9.5, 'maxspeed':1000}, 62)

# test_parse_settings_final()     # Uncomment
