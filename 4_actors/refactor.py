# refactor.py
#
# Throughout this project, we've experimented with different
# implementation issues and made various code modifications to address
# those issues.  Your final task is to take everything you've learned
# so far and to create a final implementation of the Actor system
# that incorporates everything all at once.
#
# Just to recall, this includes:
#
# 1. A way to have message variants can be processed quickly
#    and reliably.
#
# 2. No direct instantiation of actors. Actors can only be
#    referenced by their address.
#
# 3. Actors must be able to send messages and spawn new actors
#    in response to receiving a message.
#
# 4. Actors must be able to self cancel.  Cancellation requests
#    from the outside must also be honored.

from dataclasses import dataclass

@dataclass
class Message:
    source : str
    dest : str
    # You define
    ...

class Actor:
    # You define
    ...

class Manager:
    # You define
    ...
    
# You may define additional classes if you think it makes sense to do so.

