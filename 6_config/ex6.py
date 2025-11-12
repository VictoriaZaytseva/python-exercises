# -----------------------------------------------------------------------------
# Exercise 6 - The Sequence
#
# If you look more closely at Exercise 5, you'll find that the
# parse_setting() function is stepping through a sequence of
# individual parsing steps, but the code looks almost identical at
# each step.  Maybe this sequencing is something that could be
# generalized in some way.

from ex5 import parse_name, parse_integer, parse_equal, parse_semi

# Create a function `sequence(*parsers)` that accepts any number of
# parser functions and combines them into a single function that
# invokes each parser in order.  If any parser fails, return None.  If
# all parsers work, return a list of the matching parts and an ending
# index.

def sequence(*parsers):
    def parse(text, index):
        ...
    return parse

# Try combining the earlier rules into a sequence
match_setting = sequence(parse_name, parse_equal, parse_integer, parse_semi)

def test_match_setting():
    assert match_setting("x=42;",0) == (['x','=','42',';'], 5)
    assert match_setting("x=42", 0) == None     # Missing ;
    assert match_setting("x 42", 0) == None     # Missing =

# test_match_setting()     # Uncomment

# Commentary: The `match_setting()` function is not quite the same
# as the previous `parse_setting()` function.   For one, it doesn't
# return the answer in the right form.  It also includes extra
# information such as the `=` and `;` characters.  Finally, it
# doesn't properly convert the string value '42' into a Python
# integer.   We will fix this in the next exercise. Proceed to ex7.
