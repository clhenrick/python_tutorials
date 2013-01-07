#!/usr/bin/env python

#set the value for x to a string that contains a format character
x = "There are %d types of people." % 10
#set the value for the variable "binary" to a string
binary = "binary"
#set the value for do_not
do_not = "don't"
#set the value for y which contains two string variables within a string ***2
y = "Those who know %s and those who %s." % (binary, do_not)

#print to the console x
print x
#print to the console y
print y

#print to the console a string that contains the value x which also has a string value ***3
print "I said: %r." %x
#print to the console a string the contains the value y which has a string value that contains 2 string values ***4
print "I also said: '%s'." %y

#set the value for hilarious to a boolean False
hilarious = False
#set the value for joke_evaluation to the string "..."
joke_evaluation = "Isn't that joke so funny?! %r"

#print to the console the values for joke_evaluation % hilarious
print joke_evaluation % hilarious

#set the value of w
w = "This is the left side of..."
#set the value of e
e = "a string with a right side."

#print to the console w+e which combines the string values for variables w and e
print w+e