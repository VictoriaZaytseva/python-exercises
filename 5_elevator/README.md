# Event Driving Programming

In this project, you're tasked with writing software for an
event-driven system (an elevator).  This is a lot different than
sequential programs like scripts in that the software is passive--only
running in reaction to events that occur.  Testing, debugging, and
code organization is much more challenging.

The other challenge with this project is figuring out how to
manage complexity.   At first glance, the problem is going to
look daunting---maybe even impossible.   When faced with a
problem like that, it often helps to "think small."  What is
the absolute most minimal thing that you could code?  What
parts of the problem can be simplified?  What parts of the
problem can be ignored entirely?

## Stateful Objects

Part of this project involves the design and implementation of a
"stateful object."  In this context, a "stateful object" refers to the
idea that an object might have different operational modes based on a
"state" setting.  Here is an example:

```
class Connection:
    def __init__(self):
        self.state = 'CLOSED'

    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('Connection already open')
        elif self.state == 'CLOSED':
            self.state = 'OPEN'

    def close(self):
        if self.state == 'OPEN':
            self.state = 'CLOSED'
        elif self.state == 'CLOSED':
            raise RuntimeError('Connection already closed')

    def receive(self):
        if self.state == 'OPEN':
            print('Receiving')
        elif self.state == 'CLOSED':
            raise RuntimeError('Connection closed')

    def send(self, data):
        if self.state == 'OPEN':
            print('Sending')
        elif self.state == 'CLOSED':
            raise RuntimeError('Connection closed')
```

In this class, the behavior of each method varies according to an
internal operational state (`'CLOSED'` or `'OPEN'`).  Certain methods
might change the internal state.

If there are many states, each method can quickly turn into a tangled
mess of `if`-statements and conditionals.  Is there any way to NOT
code it in that way?

## Disclaimer

This project is quite challenging--elevators are a lot harder than
they seem at first glance.  The code you write will probably be quite
messy and likely quite broken at the end.   However, our goal
is not so much to have a fully working elevator, but a framework
of code where we could eventually arrive at one.

Proceed to the file `elevator.py` to start.

