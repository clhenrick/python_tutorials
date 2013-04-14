#! /usr/bin/env python

from sys import exit
from random import randint

def death():
    quips = ["You died. You kinda suck at this.",
             "Nice job, you died ... jackass.",
             "Such a luser.",
             "I have a small puppy that's better at this."]
    
    print quips[randint(0,len(quips)-1)]
    exit(1)

def central_corridor():
    """
    The Gothons of Planet Percal #25 have invaded your ship and destroyed
    your entire crew. You are the last surviving member and your last
    mission is to get the neutron destruct bomb from the Weapons Armory,
    put it in the bridge, and blow the ship up after getting into an
    escape pod.
    \n
    You're running down the central corridor to the Weapons Armory when 
    a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume 
    flowing around his hate filled body. He's blocking the door to the
    Armory and about to pull a weapon to blast you!
    """       
           action = raw_input("> ")
           
           if action=="shoot!":
               print "Quick on the draw you yank out your blaster and fire it at

print central_corridor.__doc__