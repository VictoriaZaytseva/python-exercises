# -----------------------------------------------------------------------------
# Exercise 5
#
# The function make_frac() is used to construct fractions. One feature
# of make_frac() is that it puts a fraction number into lowest terms and
# normalizes the sign to always appear in the numerator.  For example:
#
#    >>> a = make_frac(4, -6)
#    >>> a.numerator
#    -2
#    >>> a.denominator
#    3
#    >>>
#
# How would you modify the Fraction namedtuple class to have the same
# behavior if you used its normal constructor?
#
#    >>> a = Fraction(4, -6)
#    >>> a.numerator
#    -2
#    >>> a.denominator
#    3
#    >>>
#
# Disclaimer:  This is hard and not obvious.  But, it points to deeper
# problems. Maybe NamedTuple is not the solution we seek.
# -----------------------------------------------------------------------------

from typing import NamedTuple

def gcd(a, b):
    # Greatest common divisor
    while b:
        a, b = b, a % b
    return a

class Fraction(NamedTuple):
    numerator : int
    denominator : int
    # You'll need to make modifications to pass the test below.  Logically,
    # you'll want to make it so the numerator/denominator are reduced to
    # lowest terms as you might have done in an __init__() method.  Sadly,
    # doing that does NOT work (can you figure out why?)

    # DOES NOT WORK!  Can you think of an alternative that achieves the same
    # effect?
    def __init__(self, numerator, denominator):
        d = gcd(numerator, denominator)
        self.numerator = numerator // d
        self.denominator = denominator // d

# You are not allowed to change any part of this test.
def test_frac():
    a = Fraction(4, 6)
    assert a.numerator == 2
    assert a.denominator == 3
    assert isinstance(a, Fraction)

    b = Fraction(-3, -4)
    assert b.numerator == 3
    assert b.denominator == 4

    c = Fraction(3, -4)
    assert c.numerator == -3
    assert c.denominator == 4

    print("Good fractions")

test_frac()

# ----------------------------------------------------------------------
# Even if you could get this work, there are other issues.
#
# Just as integers "accidentally" work as Fractions. A Fraction
# defined as a NamedTuple accidentally works as a tuple.  That means
# that it supports various "tuple" operations like this:
#
#     >>> a = Fraction(2, 3)
#     >>> len(a)
#     2
#     >>> a[0]
#     2
#     >>> a + Fraction(4, 5)
#     (2, 3, 4, 5)
#     >>>
#
# Is this a good thing or not?




