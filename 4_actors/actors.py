# actor.py
#
# Introduction
# ------------
# Arjoon is working on a distributed system involving message passing.
# The system is to be built around something known as the "actor
# model."  In the actor model, a system is composed of independent
# objects called "actors." 
#
# Actors coordinate by sending messages to each other.  Each actor has
# an associated address and this address is embedded in each message.
# There is no other mechanism for communication nor is there any
# shared state.  Think of each actor as a completely independent
# entity that is isolated from all other actors except for the ability
# to receive a message.
#
# In response to a message, an actor can perform local processing,
# send messages to other actors that it knows about, or create new
# actors. It can also ignore the message if it doesn't understand it.
#
# To implement the actor model, Arjoon has started to write the
# following code.  It consists of a `Message` class that is used to
# encode messages.  The `Actor` class is an abstract class that
# specifies the required interface for `Actor` instances--actors must
# be defined by inheriting from this class.  Finally, there is a
# `Manager` class that has runtime functionality related to sending
# messages and creating (spawning) new actors.
#
# Most of this project is going to involve thinking about these
# classes, their overall design, and their interaction with each other.

from dataclasses import dataclass

@dataclass
class Message:
    source : str
    dest : str
    content : str

class Actor:
    def __del__(self):
        print(f'{self} is going away')
        
    def handle_message(self, msg: Message):
        raise NotImplementedError('Actors must implement handle_message()')
    
class Manager:
    def __init__(self):
        self._actors = { }
        
    def send(self, msg: Message):
        if msg.dest in self._actors:
            self._actors[msg.dest].handle_message(msg)

    def spawn(self, address: str, actor: Actor) -> str:
        self._actors[address] = actor
        return address
        
# -----------------------------------------------------------------------------
# Exercise 1 : Hello World
#
# Your first task is to try an example involving the above code.  Here
# is an implementation of an actor that receives messages and simply
# prints them out.

class Printer(Actor):
    def handle_message(self, msg: Message):
        print(f'{msg.dest}: {msg.source} said : {msg.content}')
        
def printer_example():
    import time
    m = Manager()
    m.spawn('printer', Printer())
    m.send(Message(source='example',
                   dest='printer',
                   content='Hello World'))
    time.sleep(5)
    m.send(Message(source='example',
                   dest='printer',
                   content='Are you still there world?'))

# Uncomment this line and watch the code run.  You should see
# two messages displayed along with a notification about the
# Printer actor "going away."

printer_example()

# Question: Actors are always referenced by an address which
# is a string such as 'printer' in this example.  Is there
# a mechanism for an actor to obtain it's own address?

# -----------------------------------------------------------------------------
# Exercise 2 : Understanding the Manager
#
# The purpose of the `Manager` class is to create a managed
# environment for the `Actor` instances and to handle all of the
# associated messaging.  Actors are always associated with an
# enclosing Manager.  When the Manager goes away, the Actors contained
# within it should also go away.  Verify that this seems to happen by
# trying this example:

def manager_example():
    m = Manager()
    # Create a few actors
    m.spawn('alice', Printer())
    m.spawn('bob', Printer())
    # Send a few messages
    m.send(Message(source='example', dest='alice', content='Hi Alice'))
    m.send(Message(source='example', dest='bob', content='Hi Bob'))
    # Delete the manager.
    # This should produce two messages about the Printer actor going away
    print('About to delete the manager')
    del m
    print('Manager deleted')
    print('You should have seen two "going away" messages above')

# Uncomment
manager_example()

# -----------------------------------------------------------------------------
# Discussion:
#
# These two opening exercises set the stage for the rest of the project.
# Key ideas:
#
#  - Actors are objects that receive and respond to messages.
#  - The Manager provides a runtime environment for actors.
#  - Everything goes away when the Manager goes away.
#
# To continue, go to the file 'messages.py'



