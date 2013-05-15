#! /usr/bin/env python

# exercise 42: Is-A, Has-A, Objects and Classes

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    
    def __init__(self):
        print "I'm a new Animal!"
    
    def poops(self, size):
        self.size = size
        return size

## ??
# Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## ??
        # self has-a name
        self.name = name
    
    def say_name(self, name):
        self.name = name
        print name

## ??
## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## ??
        ## self has-a name
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## ??
        ## self has-a name
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None

## ??
## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        ## super has-a Employee is-a self? **not sure...
        super(Employee, self).__init__(name)
        ## ??
        ## self has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")
rover.say_name("Rover")
rover.poops("HUGE")


## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet that is-a Cat named "Satan"
mary.pet = satan

## frank is-a Employe named "Frank" with salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet rover that is-a Dog
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
