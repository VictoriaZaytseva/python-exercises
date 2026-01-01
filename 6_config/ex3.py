# -----------------------------------------------------------------------------
# Exercise 3 - The Repetitive (Code)
#
# Ben shows his code to Arjoon who notices that the `parse_integer()` and
# `parse_name()` functions are basically identical.
#
# "There's just one tiny difference in both of the functions", he remarks.
#
# Perhaps the core functionality could be implemented in a single
# function that accepts some kind of extra predicate function for
# testing characters.  For example:

def parse_matching_predicate(text, index, predicate):
    n = index
    while n < len(text) and predicate(text[n]):
        n += 1
    return (text[index:n], n) if n > index else None

def test_parse_matching_predicate():
    assert parse_matching_predicate("123 456", 0, str.isdigit) == ('123', 3)
    assert parse_matching_predicate("123 456", 4, str.isdigit) == ('456', 7)
    assert parse_matching_predicate("abc", 0, str.isdigit) == None
    assert parse_matching_predicate("", 0, str.isdigit) == None

test_parse_matching_predicate()

# Show how you could rewrite the `parse_integer()` and `parse_name()`
# functions in terms of `parse_matching_predicate()`.  

def parse_integer(text, index):
    return parse_matching_predicate(text, index, str.isdigit)    # You define

assert parse_integer('1234 567', 0) == ('1234', 4)
assert parse_integer('1234 567', 5) == ('567', 8)
assert parse_integer('abc', 0) == None              # No match
assert parse_integer('', 0) == None                 # No match (must be at least one digit)

def parse_name(text, index):
    return parse_matching_predicate(text, index, str.isalpha)    # You define

assert parse_name("abc def", 0) == ('abc', 3)
assert parse_name("abc def", 4) == ('def', 7)
assert parse_name("123", 0) == None                # No match
assert parse_name('', 0) == None                   # No match (must be at least one letter)

# Your `parse_setting()` and `parse_settings()` functions should work without
# modification using these functions.  Please copy that code here and verify
# that it still works.

def parse_setting(text, index):
    value = text.strip().rstrip(';').split('=')
    if(len(value) !=2 or not text.strip().endswith(';')):
        return None
    else:
        if(value[1].isdigit()):
            parsed_int = parse_integer(value[1], index)
            return (value[0], int(parsed_int[0])), index + len(text)
        else:
            parsed_str = parse_name(value[1], index)
            return (value[0], parsed_str[0]), index + len(text)  

def test_parse_setting():
    assert parse_setting("name=42;", 0) == (('name', 42), 8)
    assert parse_setting("x", 0) == None
    assert parse_setting("xyz 2", 0) == None         # Missing '='
    assert parse_setting("a=42", 0) == None          # Missing ';' at end

test_parse_setting()             # Uncomment

def parse_settings(text, index):
    result = [x+';' for x in text.split(';')]
    result.pop()
    settings = {}
    curr_index = index
    for item in result:
        parsed = parse_setting(item, 0)
        if parsed is not None:
            key, value = parsed[0]
            settings[key] = value
            curr_index += parsed[1]
        else:
            break
    return settings, curr_index

def test_parse_settings():
    assert parse_settings("a=123;b=42;size=99;", 0) == ( {'a': 123, 'b': 42, 'size': 99}, 19)
    assert parse_settings("", 0) == ({ }, 0)
    assert parse_settings("a=123;b 42;", 0) == ({ 'a': 123 }, 6)

test_parse_settings()       # Uncomment
