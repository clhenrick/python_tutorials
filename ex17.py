#! usr/bin/env python

#exercise 17 More Files, from Learn Python the Hard Way v 2.0

from sys import argv; from os.path import exists; script, from_file, to_file = argv

#you could also do it on one line like this apparently:
#from sys import argv; open(argv[2], 'w').write(open(argv[1]).read())

print "Copying from %s to %s" % (from_file, to_file)

#question from Zed; "we could do these (next) two (lines of code) on one line too, how?"
#answer: by removing the second variable (see exercise) and instead chaining two method calls.
#input = open(from_file)
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
#remove the features below to simplify script...
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

#simplified the following as above by removing the second variable and calling two methods.
#output = open(to_file, 'w')
open(to_file, 'w').write(indata)

print "Alright, all done."

#no more variables means you don't need to close them!
#output.close()
#input.close()