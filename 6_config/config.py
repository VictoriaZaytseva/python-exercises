# config.py
#
# Objective: Explore an application of higher-order functions and
# composition of functions.
# -----------------------------------------------------------------------------
#
# Ben has been lamenting the complex state of packaging,
# configuration, and software deployment. "I just can't take it
# anymore!!!!" he wails as he runs out of the office.
#
# Clearly, the solution to all of Ben's problem, is for Ben to create
# a new packaging tool based on a new simplified configuration file format
# (see https://xkcd.com/927/).
#
# Thus, Ben has been hard at work coding a tool to read his new
# configuration file format. Part of it involves text parsing.  He
# needs to write code that recognizes various elements from a text
# string such as numbers and names:
#
#      integers   - Example: 123
#      names      - Example: abcdef
#
# To do this, he's written the following functions.  Each of these
# functions accept an input string and integer starting index as
# input.  They produce a tuple of the matching text and an ending
# index as output or None if there is no match. 
#
# Note: This interface may look a little weird, but Ben is thinking
# about the problem of efficiently reading through a text file
# without having to make a lot of string copies.  Keeping the
# original unmodified text and a numeric index seemed like one way
# to do it.

def parse_integer(text, index):
    n = index
    while n < len(text) and text[n].isdigit():
        n += 1
    return (text[index:n], n) if n > index else None

assert parse_integer('1234 567', 0) == ('1234', 4)
assert parse_integer('1234 567', 5) == ('567', 8)
assert parse_integer('abc', 0) == None              # No match
assert parse_integer('', 0) == None                 # No match (must be at least one digit)

def parse_name(text, index):
    n = index
    while n < len(text) and text[n].isalpha():
        n += 1
    return (text[index:n], n) if n > index else None

assert parse_name("abc def", 0) == ('abc', 3)
assert parse_name("abc def", 4) == ('def', 7)
assert parse_name("123", 0) == None                # No match
assert parse_name('', 0) == None                   # No match (must be at least one letter)

# -----------------------------------------------------------------------------
# Exercise 1 - The Parser
#
# As part of Ben's configuration file format, configuration settings are
# written in the following form:
#
#      name=value;
#
# For example:
#
#      x=42;
#      
# Your task, use the functions above to write a `parse_setting()`
# function that converts text such as 'x=42;' into a tuple ('x', 42).
# Integer values should be converted to a Python integer.  Like the
# `parse_integer()` and `parse_name()` functions, the ending index
# will also be returned.  If there is any error in the format (such as
# a missing semicolon), the function should return None.

def parse_setting(text, index):
    ... # You define using the parse_integer() and parse_name() functions above

def test_parse_setting():
    assert parse_setting("name=42;", 0) == (('name', 42), 8)
    assert parse_setting("x", 0) == None
    assert parse_setting("xyz 2", 0) == None         # Missing '='
    assert parse_setting("a=42", 0) == None          # Missing ';' at end

# test_parse_setting()             # Uncomment

# -----------------------------------------------------------------------------
# Exercise 2 - The Repetitive
#
# The parse_setting() function in exercise 1 is only a small part of a
# larger parser.   Ben actually wants to parse multiple settings into
# a Python dictionary.  For example, input like this:
#
#     a=123;b=42;size=99;
#
# Should turn into the following:
#
#     { 'a': 123, 'b': 42, 'size': 99 }
#
# Like the other functions, the ending index will also be returned.
# If no settings can be parsed, an empty dictionary is returned.
#
# You task: implement a `parse_settings()` function that repeatedly
# calls parse_setting() to parse each setting one at a time and
# returns a dictionary when no more settings can be found.
#
# Note: You can turn a list of tuples [('a',123), ('b', 42), ('size', 99)]
# into a dict using the dict([('a',123), (b', 42), ...]).

def parse_settings(text, index):
    ... # You define

def test_parse_settings():
    assert parse_settings("a=123;b=42;size=99;", 0) == ( {'a': 123, 'b': 42, 'size': 99}, 19)
    assert parse_settings("", 0) == ({ }, 0)
    assert parse_settings("a=123;b 42;", 0) == ({ 'a': 123 }, 6)

# test_parse_settings()       # Uncomment

# Proceed to ex3.py when finished.






    
