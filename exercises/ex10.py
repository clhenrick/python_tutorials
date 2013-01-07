#! usr/bin/env python

tabby_cat="\tI'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat="I'm \\ a \\ cat."

fat_cat='''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#while True:
#	for i in["/","-","|","\\","|"]:
#		print "%s\r" %i,

#extra credit...
number = 100
dope = "dope! " * number
stupid_cat = "I\'m a cat that\'s %r" %"dumb"
stinky_cat = "I\'m a cat that farted %s times and said \"%r\" %s times or\
 once for each time in case you're stupid!" % (number,dope,number)

print stupid_cat
print stinky_cat