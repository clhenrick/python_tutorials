#! usr/bin/env python

#exercise 30: else and if

people = 30
cars = 30
buses = 5

#if the number of cars are greater than the number of people than print ...
if cars > people:
    print "We should take the cars."
#other wise if the number of cars are less than people print...
elif cars < people:
    print "We should not take the cars."
#other wise print ...
#  *notice the else statement is immediately followed by a colon.
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

#extra credit:
if cars > buses and people < cars:
    print "There's no reason to drive."
elif cars < buses and people > buses:
    print "So maybe driving would be good?"
elif people <= cars and people > buses:
    print "Let's take the bus!"
else:
    print "Driving is a last resort!"