# Interfaces

Functions are the primary unit of code that you find in most programs.
Functions also form the basis of programming interfaces and libraries.
In thinking about interfaces, one must often think about how functions
interact with each other. This project explores some of these ideas.

Look at the file `after.py` to start and then proceed through
`ex1.py` - `ex8.py`. 

## Advanced Function Idioms

Suppose you have a function like this:

```
def func(x, y, z):
    print(x, y, z)
```

Normally, you'd call the function by giving it three arguments like `func(1,2,3)`.  However,
Python supports a range of other calling conventions:

```
func(1, 2, 3)           # Positional arguments
func(x=1, y=2, z=3)     # Keyword arguments
func(1, z=3, y=2)       # Mix of positional and keyword arguments

args = (1,2,3)
func(*args)             # Passing an iterable as positional args

kwargs = { 'x': 1, 'y': 2, 'z': 3}
func(**kwargs)          # Passing a dictionary as keyword args

args = (1,2)
kwargs = { 'z': 3 }
func(*args, **kwargs)   # Passing both positional and keyword args
```

Function definitions also support a variety of advanced features.
For example:

```
# Default arguments
def func(x, y, z=42):
    ... 

func(1, 2)           # Can omit the z

# Keyword-only arguments
def func(x, y, *, z):
    ...

func(1, 2, z=3)     # z must be provided by keyword

# Positional-only arguments
def func(x, /, y, z):
    ...

func(1, 2, 3)         # x must be given by position
func(1, y=2, z=3)     # Ok
func(x=1, y=2, z=3)   # Error

# Any number of positional arguments
def func(*args):
    ...

func()        # args -> ()
func(1,2)     # args -> (1,2)
func(1,2,3,4) # args -> (1,2,3,4)

# Any number of keyword arguments
def func(**kwargs):
    ...

func(x=2, color='red')  # kwargs -> {'x':2, 'color': 'red'}

# Any arguments whatsoever
def func(*args, **kwargs):
    ...

func(1,2, x=3, y=4)    # args=(1, 2), kwargs={'x':3, 'y':4}
```

## Exceptions

Python uses exceptions to signal errors.  For example:

```
>>> import math
>>> math.sqrt(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>>
```

Exceptions can be caught using `try-except`.  For example:

```
try:
    y = sqrt(x)
except ValueError as err:
    print("It didn't work. Reason:", err)
```

## Chained Exceptions

Python functions signal errors via exceptions.  It is possible for
exceptions to be nested and to be chained together.  Try this example
and see what happens:

```
def fail():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError("It failed") from e

fail()
```

Here, the result will be a "chained exception".  You should get a
traceback that includes information about both of the exceptions that
occurred.  If you want to unwind the exception, you can access the
`__cause__` attribute.  For example:

```
try:
    fail()
except RuntimeError as err:
    print("It failed. The reason why was", err.__cause__)
```

## Runtime Type Checking

To prevent errors, Python allows runtime inspection of objects.  Functions
such as `isinstance(obj, type)` can check an object to see if it's an
expected type.  Functions such as `callable(obj)` can check to see if an
object can be called like a function. For example:

```python
>>> def f(x):
...     return x + 10
...
>>> a = 2
>>> isinstance(a, int)
True
>>> isinstance(f, int)
False
>>> callable(a)
False
>>> callable(f)
True
>>>
```

## Type-based pattern matching

Python 3.10 an onward introduced a feature for structural pattern matching.
It can be used to check a value against a variety of types.  For example,
consider this code:

```python
def f(x):
    if isinstance(x, int):
        print("integer")
    elif isinstance(x, float):
        print("float")
    elif isinstance(x, str):
        print("string")
```

Instead of writing that, you can now write the following:

```python
def f(x):
    match x:
	    case int():
            print("integer")
        case float():
            print("float")
        case str():
            print("string")
```

Structural pattern matching can be extended to perform variable
unpacking if you define classes with a special `__match_args__`
attribute.  For example:

```python
class Name:
    __match_args__ = ('text',)
    def __init__(self, text):
        self.text = text
        
class Address:
    __match_args__ = ('hostname', 'port')
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        
def f(x):
    match x:
        case Name(v):
             print("Name is", v)
        case Address(host, port):
             print("Address is:", host, port)
```

		
