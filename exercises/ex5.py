#!/usr/bin/env python

name='Chris L. Henrick'
age= 30 #not a lie
height= 74 #inches
height_metric = height * 2.54 #centimeters
weight= 150 #lbs
weight_metric = weight * .453592
eyes='Brown'
teeth='Yellow'
hair='Blue'

print "Let's talk about %s." %name
print "He's %d inches or %d centimeters tall."%(height, height_metric)
print "He's %d pounds or %d kilos heavy."%(weight, weight_metric)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, %d, %d, and %d I get %d."%(
	age, height, height_metric, weight, weight_metric, age+height+weight+height_metric+weight_metric)
	