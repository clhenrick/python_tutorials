#! usr/bin/env python

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
    # read function as: split(' ', things)
    # separates each part of the string using a space as a delimiter.
    # Creates a new list with the separate strings.

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
    # another list containing multiple strings

while len(stuff) != 10:
    # do the following to the list 'stuff' while it does not contain 10 items
    
    next_one = more_stuff.pop() # creates a new string by removing the last item from the list more_stuff 
        # pop(more_stuff)
    
    print "Adding: ", next_one # prints "Adding " and the current string of 'next_one'
    
    stuff.append(next_one) # append the string in 'next_one' to 'stuff'
        # append(stuff, next_one)
    
    print "There's %d items now." % len(stuff) # prints how many items are in the list 'stuff'

print "There we go: ", stuff
    # prints the items now in stuff after the while loop added new items.

print "Let's do some things with stuff."


print stuff[1] # prints the second item in the list 'stuff'

print stuff[-1] # prints the last item in the list 'stuff'

print stuff.pop() # removes the last item in 'stuff' and prints it
    # pop(stuff)

print ', '.join(stuff) # calls the function join on 'stuff'
    # which makes the list a single string but when printed separates each word with ', '
    # join(', ', stuff)
    
print '#'.join(stuff[3:5]) # same as above but on elements 3-4 in 'stuff' and uses a '#' as a delimiter
    # join('#', stuff[3:5])