#! usr/bin/env python

#get user input
from sys import argv

#user input needs to be 2 separate things: the name of the script and another file name
script, filename=argv

#set the variable txt to the command open with the parameter file name
txt=open(filename)

#print to the console "Here's your file "filename".
print "Here's your file %r." %filename
#print to the console and call the function "read" with no parameters on txt
print txt.read()
print txt.close()

#print to the console "Type the filename again:"
#print "Type the filename again:"
#set the variable file_name to raw_input with some parameter that ">" stands for.
#file_again=raw_input(">")

#set the variable txt_again to the commmand open with the parameter set to the variable file_again
#txt_again=open(file_again)

#print to the console the variable txt_again which calls the function read with no parameters
#print txt_again.read()

