# after.py
#
# Mary has been pondering the mysteries of the universe, time, and
# function evaluation. In this project, we're going to sneak in and
# join her.  Let's peek inside her mind...
#
# ... ah, we see that Mary is currently pondering the problem of
# submitting work to cloud services.  The focus of her thinking is not
# so much on the low-level mechanics, but on the top-level programming
# interface for it.  To explore this, she has written the following
# small function that accepts a time delay and a function callback.
# The evaluation of the supplied function is delayed and its final
# returned. Very exciting!  Although it's not quite the same as
# actually executing a function in the cloud, it at least mimics the
# performance of doing so.

import time

def after(seconds, func):
    time.sleep(seconds)   # Emulate the "cloud"
    return func()

# Proceed to exercise 1 in ex1.py







