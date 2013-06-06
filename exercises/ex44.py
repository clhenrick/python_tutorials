#! usr/bin/env python

# exercise 44: Inheritance vs. Composition
# are concepts practiced when reusing code
# important code: super() which is often used with __init__ functions in base classes but 
#    is not used in this example.
# it's good practice to avoid "multiple inheritance" but of course okay to break the rules

# create a class called Parent that has methods override(), implicit(), altered()
class Parent(object):
    
    def override(self):
        print "PARENT override()"
    
    def implicit(self):
        print "PARENT implicit()"
    
    def altered(self):
        print "PARENT altered()"

# create a class called Other that has methods override(), implicit(), altered()
class Other(object):
    
    def override(self):
        print "OTHER override()"
    
    def implicit(self):
        print "OTHER implicit()"
    
    def altered(self):
        print "OTHER altered()"

# create a class called Child that has methods override(), implicit(), altered(), composition()
# in Child create a __init__() function that points to Other() which allows for Child() to utilize the altered() method from Other()
class Child(Parent):
    
    def __init__(self):
        self.other = Other()
    
    def override(self):
        print "CHILD override()"
    
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
    
    def composition(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

print "\n"

dad.override()
son.override()

print "\n"

dad.altered()
son.altered()

print "\n"

son.composition()

