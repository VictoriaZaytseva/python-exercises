# stacks.py
#
# Introduction
# ------------
# In an unusual shift in business strategy, management has decided
# that a full effort will be made to recreate the greatest handheld
# computer ever created--the HP 35 calculator (only sleeker and with
# BlueTooth).  HP Calculators are somewhat infamous for their use
# of RPN (https://en.wikipedia.org/wiki/Reverse_Polish_notation)
# wherein to perform a calculation such as "3 + 4", you would first
# enter 3, enter 4, and then hit the "+" key last.
#
# Underneath the hood, these calculators are based on a stack
# structure.  The entered values get saved on a stack. Operations
# such as "+" and "*" consume the top two items, carry out the
# calculation, and save the result back on the stack.
# 
# Because stacks seem central to the design, you've been tasked with
# the problem of making stacks. How hard could it be?

# -----------------------------------------------------------------------------
# Exercise 1 - The stack
#
# Define a Stack data structure.  It should support push() and pop() operations
# that work as follows:
#
#    >>> s = Stack()
#    >>> s.push(23)
#    >>> s.push(45)
#    >>> len(s)
#    2
#    >>> a = s.pop()         # Returns the last item pushed
#    >>> a
#    45
#    >>> b = s.pop()
#    >>> b
#    23
#    >>> len(s)
#    0
#    >>> s.push(a + b)      # Push a result onto the stack
#    >>> s.pop()
#    68
#    >>>
# -----------------------------------------------------------------------------

class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, value):
        self._items.append(value)
                 
    def pop(self):
        return self._items.pop()
    
    def __len__(self):
        return len(self._items)



def test_stack(s):     # s is a Stack instance
    s.push(23)
    s.push(45)
    assert len(s) == 2
    assert s.pop() == 45
    assert s.pop() == 23
    assert len(s) == 0
    print("Good stack!")

test_stack(Stack())    # You need to define the Stack class

# -----------------------------------------------------------------------------
# Exercise 2 - A Calculator
#
# Use your stack class to make a simple 4-function calculator.  You
# need to support four operations (add, sub, mul, and div) in addition
# to push/pop.  For example:
#
#     >>> s.push(23)
#     >>> s.push(45)
#     >>> s.add()
#     >>> s.pop()
#     68
#     >>>
#
# All math operations consume the top two items on the stack and
# replace them with the result.  Here's how you would calculate 2 * (3 + 4)
#
#     >>> s.push(2)
#     >>> s.push(3)
#     >>> s.push(4)
#     >>> s.add()
#     >>> s.mul()
#     >>> s.pop()
#     14
#     >>>
#
# Some details have been left intentionally vague. How would you implement this?
# -----------------------------------------------------------------------------

# You define a "Calculator" class here.
class Calculator:
    
    def __init__(self, stack):
        self._stack = stack
    
    def push(self, value):
        self._stack.push(value)
    
    def pop(self):
        return self._stack.pop()
    
    def add(self):
        if(len(self._stack) < 2):
            raise Exception("Not enough values on stack")
        else: 
            first = self._stack.pop()
            second = self._stack.pop()
            self._stack.push(first + second)
    
    def mul(self):
        if(len(self._stack) < 2):
            raise Exception("Not enough values on stack")
        else: 
            first = self._stack.pop()
            second = self._stack.pop()
            self._stack.push(first * second)

    def div(self):
        if(len(self._stack) < 2):
            raise Exception("Not enough values on stack")
        else: 
            first = self._stack.pop()
            second = self._stack.pop()
            self._stack.push(second // first)
    
    def sub(self):
        if(len(self._stack) < 2):
            raise Exception("Not enough values on stack")
        else: 
            first = self._stack.pop()
            second = self._stack.pop()
            self._stack.push(second - first)            
        
def test_calculator(calc):
    calc.push(23)
    calc.push(45)
    calc.add()
    assert calc.pop() == 68

    calc.push(2)
    calc.push(3)
    calc.push(4)
    calc.add()
    calc.mul()
    assert calc.pop() == 14

    calc.push(10)
    calc.push(3)
    calc.sub()
    assert calc.pop() == 7

    calc.push(10)
    calc.push(5)
    calc.div()
    assert calc.pop() == 2.0
    print("Good calculator!")

# For the above test, you need to create the "Calculator" instance calc and pass 
# it to the above test
#
calc = Calculator(Stack())
test_calculator(calc)            # Uncomment

# -----------------------------------------------------------------------------
# Exercise 3 - The Mutable
#
# A central idea of object-oriented programming is that it is often focused
# on behavior and mutation.  You create an object.  You execute methods on the
# object.  Those methods tend to modifiy the state of the object.
#
# However, what happens when a method fails?   Consider the following test
# involving a calculator:

def test_failure(calc):
    calc.push(23)
    try:
        calc.add()              # Should fail.  Not enough values were pushed
    except Exception as err:
        pass
    else:
        raise AssertionError("Why didn't I fail???")

    # What happens if you resume using the calculator after a failure?
    calc.push(45)
    calc.add()                    # Does this work?
    assert calc.pop() == 68       # Does this work?

test_failure(Calculator(Stack()))      # Uncomment

# YOUR TASK: Modify the calculator class so that its methods either
# work entirely or fail entirely.  Methods that fail should leave the
# calculator state unchanged.
#
# DISCUSSION: What are the pros and cons of this design?

# -----------------------------------------------------------------------------
# Exercise 4 - The Debugged and the Defended
#
# Peter is working on some code that involves the calculator class.  However,
# it's broken and he's trying to figure out why.   To help debug it,
# he's written a customized `Stack` class with some print statements
# added to it.  
#
# Similarly, Arjoon has decided that the calculator should do a better job
# of type-checking.  "Why is this allowed?" he asks:
#
#      >>> s = Stack()
#      >>> s.push('hello')
#      >>> s.push(4)
#      >>> s.mul()
#      >>> s.pop()
#      'hellohellohellohello'
#      >>>
#
# To address this, he's created a custom Stack with some type-checking
# added to it.
#
# Although Peter and Arjoon, have created custom Stack classes, they're
# now both perplexed about how to use them with the Calculator class.
# How would you modify the Calculator class to allow alternative
# Stack implementations to be used?
# -----------------------------------------------------------------------------

# An implementation of a Stack with debugging
class DebugStack(Stack):
    def push(self, item):
        print("PUSHING:", item)
        super().push(item)

    def pop(self):
        item = super().pop()
        print("POPPED:", item)
        return item

# An implementation of a "numeric" stack where items must be numbers
class NumericStack(Stack):
    def push(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError("A number is required")
        super().push(item)

# Verify that these Stacks pass the test for Stack by uncommenting these lines.
#
test_stack(DebugStack())
test_stack(NumericStack())
#
# Note: This is a perfectly reasonable use of inheritance--using it to create
# a modified stack. 
    
# Figure out some way to use either one of these stacks with your 
# calculator.  Make sure you can run the test_calculator() test and
# that it works without modification.
#
test_calculator(Calculator(DebugStack()))
test_calculator(Calculator(NumericStack()))


# -----------------------------------------------------------------------------
# Exercise 5 - The Conflict
#
# Both Peter and Arjoon have created alternative Stack implementations.
# However, a debate has now erupted about how to enable the functionality
# of *both* classes at the same time (that is, to have both type-checking
# and debugging turned on all at once).
#
# There seems to be no obviously "great" way to use two stacks at
# once. However, Mary observes that both of these features could be
# implemented as an "add-on" instead.
#
# To illustrate, she's written the following classes below.  Your
# task: figure how theses classes are supposed to be used with either
# the Stack or Calculator class to enable debugging and type checking
# at the same time.

class DebugStackOps:          # There is *NO* inheritance here
    def push(self, item):
        print("PUSHING:", item)
        super().push(item)

    def pop(self):
        item = super().pop()
        print("POPPED:", item)
        return item

class NumericPush:             # There is *NO* inheritance here.
    def push(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError("Must be a number")
        super().push(item)
class MyCalculator(DebugStackOps, NumericPush, Calculator):
    pass
calc = MyCalculator(Stack()) # Create a calculator with both of the above classes in effect
test_calculator(calc)      # Uncomment

# -----------------------------------------------------------------------------
# Exercise 6 - "The Patch"
#
# Instead of defining debugging and type checking features as classes,
# Ben has proposed an approach involving code patching.   The functions below
# have been written.   Show how you could use these functions to add
# debugging and type-checking to the calculator at the same time.
#
# Note: These functions can be used as class decorators, but they don't
# necessarily have to be used exactly in that way.

def add_stack_debugging(cls):
    orig_push = cls.push
    def push(self, item):
        print("PUSHING:", item)
        orig_push(self, item)
    cls.push = push
    
    orig_pop = cls.pop
    def pop(self):
        item = orig_pop(self)
        print("POPPED:", item)
        return item
    cls.pop = pop
    return cls

def add_stack_checking(cls):
    orig_push = cls.push
    def push(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError("Must be a number")
        orig_push(self, item)
    cls.push = push
    return cls

calc = ...     # Create a calculator with both of the above code modifications in effect
# test_calculator(calc)      # Uncomment

# Thought experiment:   What happens if you now run tests using a normal calculator?
# test_calculator(Calculator())    # Uncomment

# -----------------------------------------------------------------------------
# A moment of reflection....
#
# ... are we even solving the right problem?   Proceed to calculator.py.
