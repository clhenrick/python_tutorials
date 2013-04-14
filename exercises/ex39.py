#! usr/bin/env python

#exercise 39

# assign the variable ten_things to a string
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# print "..."
print "Wait there's not 10 things in that list, let's fix that."

# assign the variable stuff to call the function split() with parameters ten_things and ' '
stuff = ten_things.split(' ') # ten_things.split(' ') is saying; split(ten_things, ' ')

# create a list called more stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# create a while loop that wont' stop until stuff contains 10 items
while len(stuff) != 10: 
    next_one = more_stuff.pop() # more_stuff.pop() is saying; pop(more_stuff)
    print "Adding: ", next_one
    stuff.append(next_one) # 
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!
