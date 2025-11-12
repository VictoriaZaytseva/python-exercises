# Functional Programming

Up to this point, a lot of our discussion has focused on objects and
the way in which objects can be put together (inheritance,
composition, etc.).  However, a similar kind of focus can
also be applied to functions.  For example, functions can be passed
around and interact with other functions in unusual ways.  Studying
this interaction is often at the foundation of a lot of techniques
from "functional programming."

This project explores some common and novel uses of functions.

Look at the file `config.py` to start.

## Overview of Functions

One of the most common things we do as programmers is write functions.
For example:

```
def square(x):
    return x * x

print(square(10))
```

A function takes inputs and returns a result. It all seems simple
enough. Well, until it's not.

## Higher Order Functions

Functions can be passed around as data, just like numbers or strings.
So, a function can be passed as an argument to another function.
A common example is the definition of a `map()` function:

```
def map(func, items):
    result = [ ]
    for x in items:
        result.append(func(x))
    return result

def square(x):
    return x*x

map(square, [1,2,3,4])   # -> [1, 4, 9, 16]
```

Sometimes `lambda` is used to define a short function instead:

```
map(lambda x: x*x, [1,2,3,4])  # -> [1, 4, 9, 16]
```

Functions can also be created and returned as results.  For example:

```
def make_mapper(func):
    def map(items):
        result = [ ]
	for x in items:
	    result.append(func(x))
        return result
    return map

def square(x):
    return x*x

square_items = make_mapper(square)
square_items([1,2,3,4]) # -> [1, 4, 9, 16]
```

In this case, the `make_mapper()` function is more of a code generator.
It doesn't actually perform any kind of operation--it merely creates a
function to carry out the operation later.

When returning a function, the returned function remembers values from
its definition environment.  So the inner `map()` function above
remembers the value of `func` that was provided to `make_mapper()`.
This is sometimes known as a "closure."

## Composition of Functions

Suppose that you have two functions like this:

```
def square(x):
    return x * x

def tenx(x):
    return x * 10
```

These functions can be composed together by defining a new function like this:

```
# Compute 10 times the square of x
def f(x):
    return tenx(square(x))
```

This is effectively defining a chain of computation.  The input `x` is
first fed to `square(x)`. The result of that is then fed to the
function `tenx()`.  It's often ill-advised to write code that combines
too many things all at once, but you often see it with various forms
of data processing.  For example, this example involving string processing.

```
t = s.lower().replace('.', ' . ').replace(',', ' , ').split()
```

## Variadic Arguments

Sometimes you want to write a function that takes any number of inputs.
The `*args` syntax can be used to do this:

```
def many(*args):
    print(args)

>>> many(1,2,3)
(1,2,3)
>>> many()
()
>>> many(1,2,3,4,5)
(1,2,3,4,5)
>>>
```

When used, all of the supplied arguments are put into a tuple and assigned
to the `args` variable.

The `*` syntax can also be used to pass arguments to a function:

```
def func(x, y, z):
    print(x, y, y)
    
args = (1,2,3)
func(*args)      # Same as func(1,2,3)
```

