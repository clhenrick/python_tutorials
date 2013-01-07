#! usr/bin/env python

from sys import argv

script, filename = argv

print "Would you like to now read %r?" % filename

raw_input("yes or no? (RETURN or CTRL-C)")

print "Opening the file..."
target = open(filename)
print "Here are the contents of %r:" % filename
print target.read()
print "Closing the file."
target.close()

