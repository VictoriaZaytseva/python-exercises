# Owning Your Abstractions

As a programmer, it's common to define data structures--typically in
the form of a class.  In this exercise, we explore the interplay
between the use of classes and built-in data structures such as lists
and dicts.  The starting point for the project is `report.py`.  Go
there first to read about the project and follow the instructions found.

## Classes

Classes are often used to represent data. For example:
```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
	self.height = height
```

or, if you prefer, you could write it using a dataclass:

```
from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int
```

With classes, you have the option of adding methods.  For example, you
could add a method to compute the area:

```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
	self.height = height

    def area(self):
        return self.width * self.height
```

Here's a usage example:

```
>>> r = Rectangle(4, 5)
>>> r.width
4
>>> r.height
5
>>> r.area()
20
>>>
```

## Properties

For methods that take no arguments and return values, it sometimes common to define a property
like this:

```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
	self.height = height

    @property
    def area(self):
        return self.width * self.height
```

The main benefit of a property is that you don't need to add the extra parentheses.
For example:

```
>>> r = Rectangle(4, 5)
>>> r.width
4
>>> r.height
5
>>> r.area
20
>>>
```

This often gives a more consistent interface

## Containers

Programs also have to work with collections of objects.  For this,
you can use built-in objects such as lists and dictionaries.

```
rectangles = [ Rectangle(10, 20), Rectangle(4, 5), Rectangle(2, 3) ]
```

You're not limited to the containers that Python provides.  If you
want, you can make a custom class that holds data. For example:

```
class Shapes:
    def __init__(self):
        self._shapelist = [ ]

    def add_shape(self, shape):
        self._shapelist.append(shape)

    def __len__(self):
        return len(self._shapelist)

    def __iter__(self):
        return iter(self._shapelist)
```

If you're going to make a custom container, there are a few extra
methods that usually get defined.  First the `__len__()` method is
added to indicate how many items are part of the container.  Python
also uses this to determine truth-value testing. It is a common
convention for empty containers to evaluate as "false" in logic
checks.  This would be indicated by returning a length of 0 from
`__len__()`.  Second, the `__iter__()` method is used to create an
iterator for use with the for-loop.  Typically, you don't need to do
much in these extra methods.  It is common to forward the operation to
the corresponding operation on an internal data structure such as a
list or dict.

There are additional container methods that might get defined
depending on how fancy you want your container to be:

```
a[index]            # a.__getitem__(index)
a[index] = value    # a.__setitem__(index, value)
del a[index]        # a.__delitem__(index)
x in a              # a.__contains__(x)
```

