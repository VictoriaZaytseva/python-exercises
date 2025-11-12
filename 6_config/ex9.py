# -----------------------------------------------------------------------------
# Exercise 9 - Repetition
#
# Ben wants to parse a sequence of settings.  For example:
#
#    speed=42;
#    size=9.5;
#    maxspeed=1000;
#
# Perhaps this can be generalized as well.  Write a function zero_or_more()
# that repeatedly invokes a parser and collects the results into a list.

from ex8 import parse_setting, reduce

def zero_or_more(parser):
    def parse(text, index):
        ... # You define
    return parse

parse_settings = zero_or_more(parse_setting)

def test_parse_settings():
    assert parse_settings("speed=42;size=9.5;maxspeed=1000;", 0) == \
                ([('speed',42), ('size',9.5),('maxspeed',1000)], 32)
    assert parse_settings("", 0) == ([], 0)

# test_parse_settings()    # Uncomment

# Show how you could use reduce() to convert the settings into a dictionary instead
parse_settings_dict = ...

def test_parse_settings_dict():
    assert parse_settings_dict("speed=42;size=9.5;maxspeed=1000;", 0) == ({'speed':42, 'size':9.5, 'maxspeed':1000}, 32)
    assert parse_settings_dict("", 0) == ({}, 0)

# test_parse_settings_dict()   # Uncomment
