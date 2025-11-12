# -----------------------------------------------------------------------------
# Exercise 5 - The Literal
#
# Let's revisit the `parse_setting()` function.  In that function,
# there should be calls to `parse_name()` and `parse_integer()`.
# However, there should also be a check for the literal '=' and ';'
# characters. You may have coded these checks directly, but maybe they
# too could be generalized by a function as well.
#

from ex4 import parse_integer, parse_name

# Write a function `match_literal(literal)` that *creates* a function that
# matches an exact sequence of supplied text:

def match_literal(literal):
    def parse(text, index):
        ... # You define
    return parse

# Examples
parse_equal = match_literal('=')
parse_semi = match_literal(';')

def test_parse_literal():
    assert parse_equal('=123', 0) == ('=', 1)
    assert parse_equal('123=', 0) == None       # Doesn't start with '='
    assert parse_equal('', 0) == None           # Doesn't start with '='
    assert parse_semi(';', 0) == (';', 1)

test_parse_literal()

# After you're done, rewrite your parse_setting() function so that it
# only uses calls to `parse_name()`, `parse_equal()`, `parse_integer`,
# and `parse_semi()` to process the input.  If any of these steps
# fail, the function should return None.

def parse_setting(text, index):
    ... # You define.

    
def test_parse_setting():
    assert parse_setting("name=42;", 0) == (('name', 42), 8)
    assert parse_setting("x", 0) == None
    assert parse_setting("xyz 2", 0) == None         # Missing '='
    assert parse_setting("a=42", 0) == None          # Missing ';' at end
    assert parse_setting("42", 0) == None
    assert parse_setting("name=name",0) == None
    
# test_parse_setting()     # Uncomment

