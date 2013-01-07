#! usr/bin/env python

#get input from the user
from sys import argv

#assign the variables script and filename to argv
script, filename = argv

#print to the console "We are going to erase <filename>"
print "We're going to erase %r." %filename
#print to the console "If you don't..."
print "If you don't want that, hit CTRL-C (^C)."
#print to the console "If you want..."
print "If you want to do that, hit RETURN."

#use the method raw_input() to get input from the user.
raw_input("?")

#print to the console "Opening the file..."
print "Opening the file..."
#assign the method open() with the parameters filename and 'w' to the variable target
target = open(filename, 'w')

#print "Truncating the file. Goodbye!"
print "Truncating the file. Goodbye!"
#use the method truncate() on the variable target to erase the file's contents.
target.truncate()

#print to the console "Now I'm going to ask you for three lines."
print "Now I'm going to ask you for three lines."

#assign user input to the following variables: line1, line2, and line3.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

#print to the console; "I'm going to write these to the file."
print "I'm going to write %r %r %r to the file." % (line1, line2, line3)

#use the method write() on the variable target while passing the parameters line1, "\n" (newline character), etc.
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#extra credit: take the above six lines of code and make them one line (hint: use strings, formats, and escapes):

#new = (line1, "\n", line2, "\n", line3, "\n") #not correct.
#target.write(new) #not correct.

#the next line is correct!
target.write("%r\n%r\n%r\n" % (line1,line2,line3))

#print to the console "And finally, we close it."
print "And finally, we close it."
#pass the method close() to the variable target
target.close()