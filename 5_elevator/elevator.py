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
class ElevatorLogic:
      floor_count = 2
      states = ('IDLE', 
                'MOVING_UP', 
                'MOVING_DOWN', 
                'BOARDING_UP', 
                'BOARDING_DOWN', 
                'UNLOADING')
      
      events = ("CALLED_UP_FLOOR_n", "CALLED_DOWN_FLOOR_n",
                "GO_TO_FLOOR_n", "ARRIVED_AT_FLOOR_n",
                "BOARDING_COMPLETE")
      
      state = IDLE

      def __init__(self):
          self.current_floor = 0
          self.direction = 1  # 1 for up, -1 for down
          self.state = 'IDLE'
          self.destination_floors = set()
          # TODO some kind of request queue?
          self.request_queue = []
          
      # Checking for things that should never happen    
      def invariants(self):
          # Elevator should never move with doors open
          if self.state in ['BOARDING_UP', 'BOARDING_DOWN', 'UNLOADING']:
              assert self.direction == 0, "Elevator moving with doors open!"
          # Elevator should never move up when at top floor
          if self.current_floor == self.floor_count - 1:
              assert self.direction != 1, "Elevator moving up at top floor!"
          # Elevator should never move down when at bottom floor
          if self.current_floor == 0:
              assert self.direction != -1, "Elevator moving down at bottom floor!"

      def handle_event(self, event):
          # elevator logic depends on current state and event
          # also need to have a queue of requests somewhere. should be async and have a listener? 
          # actor mailbox. how to implement idk T_T
          # maybe start next request after finishing some of the current ones
          # but what about interruptions, some request should get priority...
          # pull request into queue based on current state...
         if event.startswith('CALLED_UP_FLOOR_'):
            if(self.state == 'IDLE'):
               self.state = 'MOVING_UP'
            else:
               floor = int(event.split('_')[-1])
               self.request_queue.append((floor, 1))  # if elevator is not idle add to request queue
         elif event.startswith('CALLED_DOWN_FLOOR_'):
            if(self.state == 'IDLE'):
               self.state = 'MOVING_DOWN'
            else:
               floor = int(event.split('_')[-1])
               self.request_queue.append((floor, -1))  # -1 for down
         elif event.startswith('GO_TO_FLOOR_'):
             # elevator should be in boarding state and the button that is pressed should match the direction
             # this is hell
             # so many combinations of states and events
            if(self.state in ['BOARDING_UP', 'BOARDING_DOWN', 'UNLOADING']):
                 floor = int(event.split('_')[-1])
                 self.destination_floors.add(floor)
            else:
              # if not boarding and button pushed add to destination floors 
              # move to floors that are matching the directions first, after all complete, switch directions   
               floor = int(event.split('_')[-1])
               self.destination_floors.add(floor)
         self.invariants      


      # Handlers for specific events for clarity
      def handleMoveUp(self, event):
          pass
      
      def handleMoveDown(self, event):
          pass     


# TODO: split elevator class into several classes similar to actor with different behaviors.
# to do add more behaviors for each state.
class IDLE:
      def handle_destination_button(self, floor):
         pass
      def handle_up_call_button(self, floor):
         pass
      def handle_down_call_button(self, floor):
         pass
      def handle_door_close(self):
         pass
      def handle_arrival(self, floor):
         pass
class MOVING_UP:
      def handle_destination_button(self, floor):
         pass
      def handle_up_call_button(self, floor):
         pass
      def handle_down_call_button(self, floor):
         pass
      def handle_door_close(self):
         pass
      def handle_arrival(self, floor):
         pass
class MOVING_DOWN:
      def handle_destination_button(self, floor):
         pass
      def handle_up_call_button(self, floor):
         pass
      def handle_down_call_button(self, floor):
         pass
      def handle_door_close(self):
         pass
      def handle_arrival(self, floor):
         pass
class BOARDING_UP:
      def handle_destination_button(self, floor):
         pass
      def handle_up_call_button(self, floor):
         pass
      def handle_down_call_button(self, floor):
         pass
      def handle_door_close(self):
         pass
      def handle_arrival(self, floor):
         pass
class BOARDING_DOWN:
      def handle_destination_button(self, floor):
         pass
      def handle_up_call_button(self, floor):
         pass
      def handle_down_call_button(self, floor):
         pass
      def handle_door_close(self):
         pass
      def handle_arrival(self, floor):
         pass
class UNLOADING:
      def handle_destination_button(self, floor):
         pass
      def handle_up_call_button(self, floor):
         pass
      def handle_down_call_button(self, floor):
         pass
      def handle_door_close(self):
         pass
      def handle_arrival(self, floor):
         pass

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
      events = [
          'CALLED_UP_FLOOR_0',
          'CALLED_DOWN_FLOOR_1',
          'GO_TO_FLOOR_0',
          'GO_TO_FLOOR_1',
          'ARRIVED_AT_FLOOR_0',
          'ARRIVED_AT_FLOOR_1',
          'BOARDING_COMPLETE'
      ]
      for _ in range(100):
          event = random.choice(events)
          elevator.handle_event(event)
          elevator.invariants()      