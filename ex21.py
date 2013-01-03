#! usr/bin/env python

#exercise 21: Functions can return something

def add(a,b):
    print "ADDING %d + %d" % (a,b)
    return a + b
    
def subtract(a,b):
    print "SUBTRACTING %d - %d" % (a,b)
    return a - b

def multiply(a,b):
    print "MULTIPLYING %d * %d" % (a,b)
    return a * b

def divide(a,b):
    print "DIVIDING %d / %d" % (a,b)
    return a / b

print "Let's do some math with just functions!"

age = add(30,5)
height = subtract(78, 4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

#extra credit:

print "Dividing IQ: %d by 2, multiplying the result by weight: %d, subtracting that result from \
height: %d, and then adding the result to age: %d" % (iq, weight, height, age)
puzzle = (height - ((iq / 2) * weight)) + age

print "Which equals: %d" % puzzle

#the inverse of the above puzzle?
inverse = divide(iq, multiply(weight, subtract(height, add(age, 2))))

print "So the inverse is:",inverse, "right?"