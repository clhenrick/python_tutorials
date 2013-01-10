# usr/bin/env python

# exercise 33: while loops
# extra credit 1-5

""" the original exercise is just a while loop:

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = i+ 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
    
"""

# found this cool answer here: http://codepad.org/gGRRi2qW
# the initialize function prompts the user for the variables and stores them; great idea!
def initialize():
    i = int(raw_input("Type a low integer: "))
    j = int(raw_input("Type a high integer: "))
    k = int(raw_input("Type an increment integer: "))
    numbers = []
    return i, j, k, numbers

def number_make():
    i, j, k, numbers = initialize()
    
    #extra credit #5; use a for loop and range instead of while loop and increment.
    #what happens when you ditch the increment? - it just gives you the range.
    #how to insert the increment in the for loop?
    numbers = range(i,j)
    for i in numbers:
        print "Numbers are: %d" % i
       
    """
    while i < j:
        print "At the top i is %d" % i # shows how it works
        numbers.append(i)
        
        i = i + k
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i #also shows how it works  
        
        print "The numbers... "
    """

    # print each item in the list on a new line
    for num in numbers:
        print num
    # run another function to repeat this one
    repeat_it()

def repeat_it():
    again = raw_input("One more time? (y/n) ")
    if again != "n":
        number_make()

number_make()
