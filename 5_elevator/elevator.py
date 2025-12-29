'''
elevator.py

You are tasked with the job designing and writing the decision making
logic for an elevator in a 5-floor building.  The software receives
inputs from the following sources:

1. A panel of five push buttons inside the elevator car to select a
   destination floor.

2. Two push buttons (up/down) on each floor to request the elevator.
   (Remark: the top and bottom floors obviously only have one button).

3. A sensor on each floor to indicate that the elevator is arriving
   at that floor (triggered when the elevator is in motion).  If 
   instructed to stop right at this moment, assume that the elevator
   can safely do so.

4. A "boarding complete" event that occurs to indicate that the
   doors have closed after passenger loading.

The elevator operates according to the "Elevator Algorithm" as
described at https://en.wikipedia.org/wiki/Elevator_algorithm.  In a
nutshell, elevators work by alternating between upward and downward
motion.  When moving up, the elevator keeps moving up until there are
no more requests to service.  It then reverses direction and moves down
until there are no more requests to service.  A key aspect of this
approach is that it avoids starvation.  For example, suppose the
elevator is on floor 1 and Bob presses "down" on floor 3.  The
elevator will start moving up.  However, now suppose that Alice
now presses "down" on floor 5.  Instead of going to floor 3
and servicing Bob first, the elevator will *pass* floor 3 and go
all the way up to floor 5 to pick up Alice first.  It will then
stop to pick up Bob on the return trip.

YOUR TASK:

Design and implement code for the decision making logic of the
elevator. More importantly, come up with a strategy for testing it.

A CHALLENGE:

To write this code you might ask to know more about how the elevator
hardware control actually works.  For example, an elevator obviously
has a motor that moves the car up and down.  There is a door that
opens and closes.  Perhaps there is some kind of timer related to
holding the door open during loading.  Are these devices that receive
commands?  If so, how does that work?  Are we somehow responsible?
Unfortunately, we just don't have any information about that aspect of
the elevator--that's a different corporate division.

Thus, one tricky part of the project is to think about what
aspects of the elevator system are truly essential to the problem at
hand.  We'll also need to consider the way in which the logic will be
used by other software (not shown/provided).  It also means that our
understanding of the problem might be incomplete and that we should
try to write the code in a way that allows it to be extended to handle
new "requirements."

HINTS:

At first, this problem is likely to seem overwhelming. There are
many moving parts.  Where to even begin?

When presented with a problem like this, it might help to spend a bit
of time thinking about the problem before coding.  What is the
fundamental problem being solved?  What is the least amount of
information you need to solve that problem?  What is the simplest
thing that you can actually code?  What can you actually test?

With that in mind, here are some specific things to focus on:

1. Operation. What does an elevator actually do when it operates?
2. State. What information minimally needs to be stored?
3. Inputs. What inputs does the elevator software receive?
4. Outputs. What outputs are going to be produced?
5. Invariants. What is never supposed to happen?

Use your intuition and your experience as a user of an elevator.
Also, try to build your initial understanding of the problem at a high
level without immediately jumping into code.  Code can come later.
'''
  
# TODO: split elevator class into several classes similar to actor with different behaviors.
# to do add more behaviors for each state.
class IDLE:
      def handle_destination_button(elev, floor):
         pass
      def handle_up_call_button(elev, floor):
         if floor > elev.current_floor: 
            elev.state = MOVING_DOWN
            elev.destination_floors.add(floor)
         else:   
            elev.state = MOVING_UP
            elev.destination_floors.add(floor)         
      def handle_down_call_button(elev, floor):
         if floor < elev.current_floor: 
            elev.state = MOVING_DOWN
            elev.destination_floors.add(floor)
         else:   
            elev.state = MOVING_UP
            elev.destination_floors.add(floor) 
      def handle_door_close(elev):
         #door close can move to destination floor or stay idle if no requests
         pass # nothing happen? idle elevator closes the doors and stays idle
      def handle_arrival(elev, floor):
         # switch to unloading state if arrived at destination floor
         if floor in elev.destination_floors:
            elev.state = UNLOADING
            elev.current_floor = floor
            elev.destination_floors.remove(floor)
         # else stay idle
class MOVING_UP:
      def handle_destination_button(elev, floor):
            if(floor > elev.current_floor):
               elev.destination_floors.add(floor) # todo if the destination is in opposite direction, queue it for later
            else:
               pass # ignore   
      def handle_up_call_button(elev, floor):
         if(floor > elev.current_floor):
            elev.destination_floors.add(floor) # todo if the destination is in opposite direction, queue it for later
         else:
            pass # ignore

      def handle_down_call_button(elev, floor):
         # todo: queue destination for later if in opposite direction
         pass

      def handle_door_close(elev):
         pass # already moving up, should not happen

      def handle_arrival(elev, floor):
         elev.current_floor = floor
         if floor in elev.destination_floors:
            elev.state = UNLOADING
            elev.destination_floors.remove(floor)
         else:
            pass # continue moving up

class MOVING_DOWN:
      def handle_destination_button(elev, floor):
         if(floor < elev.current_floor):
            elev.destination_floors.add(floor) # todo if the destination is in opposite direction, queue it for later
         else:
            pass # ignore
      def handle_up_call_button(elev, floor):
         if(floor < elev.current_floor):
            elev.destination_floors.add(floor) # todo if the destination is in opposite direction, queue it for later
         else:
            pass # ignore
      def handle_down_call_button(elev, floor):
         if(floor < elev.current_floor):
            elev.destination_floors.add(floor) # todo if the destination is in opposite direction, queue it for later
         else:
            pass # ignore
      def handle_door_close(elev):
         pass # already moving down, should not happen
      def handle_arrival(elev, floor):
         if floor in elev.destination_floors:
            elev.state = UNLOADING
            elev.current_floor = floor
            elev.destination_floors.remove(floor)
         else:
            pass # continue moving down
class BOARDING_UP:
      def handle_destination_button(elev, floor):
         if(floor > elev.current_floor):
            elev.destination_floors.add(floor) # todo if the destination is in opposite direction do nothing?
      def handle_up_call_button(elev, floor):
         if(floor > elev.current_floor):
            elev.destination_floors.add(floor) # todo if the destination is in opposite direction do nothing? 
      def handle_down_call_button(elev, floor):
         if(floor > elev.current_floor):
            elev.destination_floors.add(floor) # todo if the destination is in opposite direction do nothing?
      def handle_door_close(elev):
         if elev.destination_floors:
            elev.state = MOVING_UP
         else:
            elev.state = IDLE
      def handle_arrival(elev, floor):
         pass # should not happen, already boarding

class BOARDING_DOWN:
      def handle_destination_button(elev, floor):
         if(floor < elev.current_floor):
            elev.destination_floors.add(floor) # todo if the destination is in opposite direction do nothing?
      def handle_up_call_button(elev, floor):
         if(floor < elev.current_floor):
            elev.destination_floors.add(floor) # todo if the destination is in opposite direction do nothing?
      def handle_down_call_button(elev, floor):
         if(floor < elev.current_floor):
            elev.destination_floors.add(floor) # todo if the destination is in opposite direction do nothing?
      def handle_door_close(elev):
         if elev.destination_floors:
            elev.state = MOVING_DOWN
         else:
            elev.state = IDLE
      def handle_arrival(elev, floor):
         pass # should not happen, already boarding

class UNLOADING:
      def handle_destination_button(elev, floor):
         # do nothing I guess only idle elevators can accept new requests
         pass
      def handle_up_call_button(elev, floor):
         if floor > elev.current_floor: 
            elev.state = MOVING_DOWN
            elev.destination_floors.add(floor)
         else:   
            elev.state = MOVING_UP
            elev.destination_floors.add(floor)

      def handle_down_call_button(elev, floor):
         if floor < elev.current_floor: 
            elev.state = MOVING_DOWN
            elev.destination_floors.add(floor)
         else:   
            elev.state = MOVING_UP
            elev.destination_floors.add(floor)
      def handle_door_close(elev):
         if elev.destination_floors:
            if max(elev.destination_floors) > elev.current_floor:
               elev.state = MOVING_UP
            else:
               elev.state = MOVING_DOWN
         else:
            elev.state = IDLE

      def handle_arrival(elev, floor):
         pass # should not happen, already unloading
class ElevatorLogic:
      states = (IDLE, MOVING_UP, MOVING_DOWN, BOARDING_UP, BOARDING_DOWN, UNLOADING)

      def __init__(self,
                   current_floor=1,
                   destinations=(),
                   up_requests=(),
                   down_requests=()):
          self.current_floor = 1
          self.state = IDLE
          self.destination_floors = set()
          # buttons pressed inside the elevator
          self.request_queue = set(destinations)
          #up and down buttons pressed in the building
          self.up_requests = set(up_requests)
          self.down_requests = set(down_requests)
          
      # Checking for things that should never happen    
      def invariants(self):
         # TODO: new invariants to check
         assert 1 <= self.current_floor <= 5, "Current floor out of range"
         assert self.state in self.states, "Invalid elevator state"
         assert all(1 <= floor <= 5 for floor in self.destination_floors), "Destination floor out of range"
         assert all(1 <= floor <= 5 for floor in self.up_requests), "Up request floor out of range"
         assert all(1 <= floor <= 5 for floor in self.down_requests), "Down request floor out of range"
          

      def handle_event(self, *args):
          # elevator logic depends on current state and event
          # also need to have a queue of requests somewhere. should be async and have a listener? 
          # actor mailbox. how to implement idk T_T
          # maybe start next request after finishing some of the current ones
          # but what about interruptions, some request should get priority...
          # pull request into queue based on current state...
         match args:
             case('down', floor):
               self.state.handle_down_call_button(self, floor) 
             case('up', floor):
               self.state.handle_up_call_button(self, floor)          
         self.invariants    

_all_buttons = ([('destination', floor) for floor in range(1, 6)]
                + [('up', floor) for floor in range(1, 5)]
                + [('down', floor) for floor in range(2, 6)])

def all_possinle_input(elev: ElevatorLogic):
   if(elev.state == MOVING_UP):
      return _all_buttons + [('floor', elev.current_floor + 1)]
   elif(elev.state == MOVING_DOWN):
      return _all_buttons + [('floor', elev.current_floor - 1)]
   elif(elev.state in {IDLE, UNLOADING, BOARDING_UP, BOARDING_DOWN}):
      return _all_buttons + [('close')]
   else:
      return _all_buttons

def test_elevator_logic():
      
      elevator = ElevatorLogic()
      # Test going to floor 2 starting from idle floor 1
      elevator.handle_event('GO_TO_FLOOR_2')
      assert elevator.current_floor == 2
      assert elevator.state == 'UNLOADING'

# can try every possible event sequence breadth-first search
def test_random_events():
      import random
      elevator = ElevatorLogic()
      for _ in range(100):
         possible_events = all_possinle_input(elevator)
         event = random.choice(possible_events)
         elevator.handle_event(*event)
         elevator.invariants()

test_random_events()
