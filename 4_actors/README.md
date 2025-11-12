# Coordinated Objects

When defining objects, it is common to focus primarily on issues
related to the object itself.  For example, what data does it contain
and what methods does it provide?  Does it contain other objects?  Does
it inherit from another object?

However, there is completely different dimension to objects related to
their overall management and interaction within a greater environment.
How are objects created?  How are they referenced by other objects?
How long do they live? How are they destroyed?

In this project, we're going to build a system of objects involving
messaging and coordination.  It's going to appear different than
normal Python programming so we'll have to pay attention to some
subtle details and think about how the pieces fit together.

This document provides a bit of background on some Python features
that may be useful in the solution.

The starting point for the project is the file `actors.py`.  Go
there to start.

## Object Lifecycle

Most programmers know about classes and the `__init__()` method which
initializes an object:

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)         #  Triggers Point.__init__(self, 2, 3)
```

However, this is only part of the story.  Objects are actually
created in two steps like this:

```
self = Point.__new__(Point, 2, 3)        # Create the instance itself
self.__init__(2, 3)                      # Execute the __init__() method
```    

This is something you could try on your own.  Try it in the
interactive terminal:

```
>>> p = Point.__new__(Point, 2, 3)
>>> p
<__main__.Point object at 0x10f35da90>
>>> p.x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Point' object has no attribute 'x'
>>> p.__init__(2, 3)
>>> p.x
2
>>>
```

Most programmers never see the `__new__()` method.  That's something
that's usually predefined and hidden behind the scenes.  A class
normally only implements `__init__()`.   However, a class can
implement `__new__()` if it wants to alter some aspect of instance
creation.   For example:

```
class Point:
    def __new__(cls, x, y):
        print("Creating Point")
        return super().__new__(cls)   # Note: x and y are *NOT* passed
    
    def __init__(self, x, y):
        print("Initializing Point")
        self.x = x
        self.y = y
```

Once the instance is alive, it carries an internal reference
count. Assignment operations increase the reference count.

```
a = Point(2, 3)     # a: refcount = 1
b = a               # b: refcount = 2     (refers to a)
c = [10, 20, b]     # c[2]: refcount = 3  (refers to a)
```

You can view the reference count using `sys.getrefcount(x)`.  Any operations
that destroy a reference decrease the reference count. These include
the `del` operator, reassignment of a value, etc.  When the reference
count reaches 0, the `__del__()` method is triggered.  Normally this
isn't defined on a class.  However, if you define it, you can see when
an object is destroyed and perform other actions. For example:

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __del__(self):
        print('Destroying Point')

>>> p = Point(2, 3)
>>> del p
Destroying Point
>>>
```

## Alternate Constructors and Class Methods

Sometimes a class needs to define an alternate constructor that
bypasses the usual `__init__()` method or does some other special
processing for some reason.  A common approach is to define a class
method like this:

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_complex(cls, c):
        self = cls.__new__(cls)
        self.x = c.real
        self.y = c.imag
        return self

# Example
p = Point.from_complex(3 + 4j)
```

Class methods are sometimes used for other purposes related to the
management of objects.  The key thing is that a class method
is usually associated with the class itself and not an single
object instance.






