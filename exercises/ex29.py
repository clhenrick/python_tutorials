#! usr/bin/env python

#exercise 29: what if

people = 20
cats = 10
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

#I added the following if-statement to test and
if people > dogs and (people > cats):
    print "People have nothing to worry about :)"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."
    

if people != dogs:
    print "People are not dogs."

"""Extra Credit:
1. code under the if statement runs when the if-statement is true.
2. code under the if statement needs to be indented 4 spaces
   so that the interpreter knows to run it when the if-statement is true.
3. if not indented the interpreter returns the following error message:
   IndentationError: expected an indented block
4. other boolean expressions can be used such as !=, and, or, not
5. when changing the variables' values the if-statements result will change.
"""