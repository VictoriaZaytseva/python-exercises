# -----------------------------------------------------------------------------
# Exercise 4 - The (Code) Generator
#
# Looking at Exercise 3, it all still feels a bit clunky.  Yes,
# there's the more general `parse_matching_predicate()` function, but
# there are now these tiny functions such as `parse_integer()` that
# merely provide some kind of wrapper around it.   
#
# All of this might be simplified if the `parse_matching_predicate()`
# function was re-envisioned.  Instead of directly parsing the
# supplied text, what if it created a parsing function instead?

def matching_predicate(predicate):
    def parse(text, index):
        n = index
        while n < len(text) and predicate(text[n]):
            n += 1
        return (text[index:n], n) if n > index else None
    
    return parse

# Using this code generator, show how you could define `parse_integer`
# and `parse_name` directly without the need for an extra wrapper layer.

parse_integer = matching_predicate(str.isdigit)
parse_name = matching_predicate(str.isalpha)

# Your task: Fill in the missing pieces (...) to make this work.  All
# the tests from exercise 3 should still work.

assert parse_integer('1234 567', 0) == ('1234', 4)
assert parse_integer('1234 567', 5) == ('567', 8)
assert parse_integer('abc', 0) == None              # No match
assert parse_integer('', 0) == None                 # No match (must be at least one digit)

assert parse_name("abc def", 0) == ('abc', 3)
assert parse_name("abc def", 4) == ('def', 7)
assert parse_name("123", 0) == None                # No match
assert parse_name('', 0) == None                   # No match (must be at least one letter)

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

test_parse_setting()      # Uncomment

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
    
test_parse_settings()    # Uncomment

