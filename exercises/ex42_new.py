#! /usr/bin/env python

# exercise 42: Is-A, Has-A, Objects and Classes

# from Zed;
# "In Python classes act as templates that "mint" new objects,
# similar to how coins were minted using a die (template)."

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    
    def __init__(self, name):
        print "I'm a new Animal that's named %s!" % name 
        self.name = name
    
    def poops(self, size):
        self.size = size
        print "That's a %s poop!" % size

# Dog is-a Animal
class Dog(Animal):

    def __init__(self, type, name):
        # call the ancestor/parent __init__
        Animal.__init__(self, name)
        
        self.type = type
        print "I'm a %s type of dawg." % type
    
        # self has-a name
        self.name = name
    
    def say_name(self, name):
        self.name = name
        print name
    
    def barks(self, wolf=None):
        self.wolf = wolf
        print wolf

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## ??
        ## self has-a name
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None
        
    def meows(self, meow):
        self.meow = meow
        print meow

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## ??
        ## self has-a name
        self.name = name
        print "Hi, my name is %s" % name
        
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

#########################
# rover tests here:
## rover is-a Dog
rover = Dog("German Shepard","Rover")
rover.say_name("Rover")
rover.poops("HUGE")
rover.barks("Arff!")


## satan is-a Cat
satan = Cat("Satan")
satan.poops("small")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet that is-a Cat named "Satan"
mary.pet = satan

## frank is-a Employe named "Frank" with salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet rover that is-a Dog
frank.pet = rover

## frank has a pet has a name Rover
print frank.pet.name
## mary has a pet has a name Satan
print mary.pet.name

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

human_pets = [satan, rover]

print human_pets[1].name
human_pets[1].poops("small")

puppies = {
    "Abe" : Dog("German Shepard", "Ableton"),
    "Blue" : Dog("German Shepard", "Blueberry"),
    "Apple" : Dog("German Shepard", "Them Apples")    
}

print puppies.items()
puppies.get("Abe")