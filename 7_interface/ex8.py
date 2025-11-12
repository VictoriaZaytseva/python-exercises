# -----------------------------------------------------------------------------
# Exercise 8 - Changing The Future
#
# In reality, Mary wants the after() function to return immediately,
# but run the supplied function in the background using a thread. To
# coordinate this, she has implemented a programming device known as a
# "Future."  A future represents the outcome of a computation that has
# yet to be performed.  The final result gets set at a later time.
#
# In many ways, a Future is almost identical to the Result object
# we created in earlier exercises except for the fact that we don't
# know its final value at the time of creation.  That only becomes
# known later.
#
# Here is code that implements a Future.

import threading
import time

class Future:
    def __init__(self):
        self._value = None
        self._exc = None
        self._evt = threading.Event()

    def set_value(self, value):
        assert not self._evt.is_set()
        self._value = value
        self._evt.set()

    def set_exception(self, exc):
        assert not self._evt.is_set()        
        self._exc = exc
        self._evt.set()

    def result(self):
        self._evt.wait()
        if self._exc is None:
            return self._value
        else:
            raise self._exc

# And here is Mary's modified after() function that uses a Future
def after(seconds, func) -> Future:
    fut = Future()
    def run():
        time.sleep(seconds)
        try:
            fut.set_value(func())
        except Exception as exc:
            fut.set_exception(exc)
    threading.Thread(target=run).start()
    return fut
        
# -----------------------------------------------------------------------------
# Part 1
#
# Your first task is to make sure you understand what's happening by
# trying an example. A critical feature of after() is that allows
# multiple functions to be launched at once.   Another critical feature
# is that if result() is called before a result is known, the code
# waits (blocks) until the result is set (this is the purpose of the
# threading.Event used in the implementation).
#
# Try this example and study the result:

def add(x, y):
    print(f"Adding: {x} + {y}")
    return x + y

def example():
    print("Launching functions")
    f1 = after(20, lambda: add(2, 3))
    f2 = after(10, lambda: add(100, 200))
    f3 = after(5, lambda: add("two", 3))
    print("Now waiting for results")
    print("f1->", f1.result())
    print("f2->", f2.result())
    try:
        f3.result()
    except TypeError as err:
        print("f3->", err)

# example()   Uncomment

# -----------------------------------------------------------------------------
# Part 2
#
# In the last few exercises, we spent a lot of time thinking about the Result
# class and how we might refactor it to support things such as type checking
# and structural pattern matching.    Can we do something similar for the
# above Future class and if so, what would it look like?
#
# This is a very open-ended question and I'm not sure there is a right answer.
# However, the gist of the code below is what to think about:

class ModernFuture:
    ...
    # ????

class Success:
    ...
    # ????

class Fail:
    ...
    # ????
    
def after(seconds, func) -> ModernFuture:
    fut = ModernFuture()
    def run():
        time.sleep(seconds)
        ...
        # Run func() and set the result of fut
        # func()

    threading.Thread(target=run).start()
    return fut

def modern_example():
    # This code is incomplete.  You need to modify/fix as you see fit.
    fut = after(10, lambda: add(2, 3))
    match ...:  # ???? 
        case Success(value):
            print("It worked:", value)
        case Fail(err):
            print("It failed:", err)

# modern_example()




