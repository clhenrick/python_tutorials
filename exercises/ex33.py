# usr/bin/env python

# exercise 33: while loops

"""
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
# the initialize function that grabs the variables is a great idea!
def initialize():
    i = int(raw_input("Type a low integer: "))
    j = int(raw_input("Type a high integer: "))
    k = int(raw_input("Type an increment integer: "))
    numbers = []
    return i, j, k, numbers

def number_make():
    i, j, k, numbers = initialize()
    
    while i < j:
        print "At the top i is %d" % i # shows how it works
        numbers.append(i)
        
        i = i + k
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i #also shows how it works  
        
        print "The numbers... "

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
