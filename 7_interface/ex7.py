# -----------------------------------------------------------------------------
# Exercise 7 - "The Chain"
#
# Although it's maybe a bit unusual in terms of Python style, one
# possibly nice thing about the last few exercises is that the after()
# function is fairly easy to reason about.  You give it a function as
# input, and it always returns a Result regardless of what the supplied
# function does.
#
# However, in programming, it's also common to perform step-by-step
# sequencing of operations. For example, consider these three
# functions (type hints added to emphasize the kind of data expected):

def A(x: int) -> int:
    return x + 10

def B(x: int) -> int:
    return x * 2

def C(x:int) -> int:
    return x * x

# Now, suppose you had some code that called each function, one after the other,
# feeding the output of one function into the input of the next function.
# Such chaining is common in a lot of data processing applications.

def chained(x:int) -> int:
    a = A(x)
    b = B(a)
    c = C(b)
    return c

assert chained(2) == 576

# How would this kind of chaining work if you also incorporated the
# use of the after() function?  For example, if you wanted to do the
# same calculation, but with time delays. Note: This is expressed as
# pseudocode--it doesn't work as shown. You'll need to modify it to
# work with the after() function in Exercise 6.

def chained_after(x:int) -> int:
    from ex6 import after, Result, Ok, Error
    a = after(1, A(x))     # Call a = A(x) after 1 second   (must modify)
    b = after(2, B(a.unwrap()))     # Call b = B(a), 2 seconds after that (must modify)
    c = after(3, C(b.unwrap()))     # Call c = C(b), 3 seconds after that (must modify)
    return c
print("Starting chained after...")
print("Result:", chained_after(2).unwrap())  # Uncomment
assert chained_after(2).unwrap() == 576        # Uncomment

# One problem with the chaining is that everything gets very messy
# once `Result` objects enter the mix.  For example, the result of
# calling `after()` can't be immediately given to the next function.
# Instead, you have to either `unwrap()` the result or destructure
# it with pattern matching.   Frankly it's a big mess.
#
# However, the idea of a chained calculation is really one of
# data flow.  For example, in the above code, we're performing
# a calculation like this:
#
#     x -> A -> B -> C -> result
#
# (The output of each function serves as the input to the next).
#
# Idea: Can we abuse Python's syntax to make it possible to
# express a computation chain in an elegant way like this?
# For example:
#
#    r = Ok(x) >> A >> B >> C
#    print(r.unwrap())           # Prints
#
# Or alternatively:
#
#    match Ok(x) >> A >> B >> C:
#       case Ok(value):
#            print("It worked:", value)
#       case Error(e):
#            print("It failed:", e)
#
# To do this, you're going to need to add an operator (>>) to
# the Result/Ok/Error classes.  

class Result:
    __match_args__ = ('_value',)
    def __init__(self, value):
        self._value = value

    def unwrap(self):
        raise NotImplemented()

    def __rshift__(self, func) -> 'Result':
        # self >> func
        raise NotImplemented()

class Ok(Result):
    def unwrap(self):
        return self._value
    
    def __rshift__(self, func) -> Result:
        # self >> func
        ...
        # You implement

class Error(Result):
    def unwrap(self):
        raise self._value

    def __rshift__(self, func) -> Result:
        # self >> func
        ...
        # You implement


def test_chained_operator(x):
    r = Ok(x) >> A >> B >> C
    assert r.unwrap() == 576

    match Ok(x) >> A >> B >> C:
        case Ok(value):
            assert value == 576
        case _:
            raise AssertionError("Why am I here?")

    match Ok("two") >> A >> B >> C:
        case Ok(value):
            raise AssertionError("Why am I here?")
        case Error(e):
            assert isinstance(e, TypeError)

# Uncomment            
# test_chained_operator(2)

# -----------------------------------------------------------------------------
# Challenge:
#
# How would you write the after() function to allow it to be injected into
# the processing chain in some way?  For example:
#
#   r = Ok(2) >> after(1, A) >> B >> after(3, C)
#
# Note: The above code does NOT work as written.  Why?  Can it be fixed?

