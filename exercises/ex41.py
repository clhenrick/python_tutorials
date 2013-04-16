#! /usr/bin/env python

"""
Exercise 41 from LPTHW
building on dict
"""

from sys import exit
from random import randint

# ends the game.
def death(action):
    """
    DEAD.
    """
    quips = ["You died. You kinda suck at this.",
             "Nice job, you died ... jackass.",
             "Such a luser.",
             "I have a small puppy that's better at this."]
    
    print quips[randint(0,len(quips)-1)]
    exit(1)

# start of game.
def central_corridor(action):
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
    #action = raw_input("> ")
           
    if action=="shoot!":
        print(
            "\n\t Quick on the draw you yank out your blaster and fire it at the Gothon."
            "\n\t His clown costume is flowing and moving around his body, which throws "
            "\n\t off your aim.  Your laser hits his costume but misses him entirely. This "
            "\n\t completely ruins his brand new costume his mother bought him, which"
            "\n\t makes him fly into an insane rage and blast you repeatedly in the face until "
            "\n\t you are dead. Then he eats you."
            )
        return 'death'
            
    elif action == "dodge!":
        print(
            "\n\t Like a world class boxer you dodge, weave, slip and slide right"
            "\n\t as the Gothon's blaster cranks a laser past your head."
            "\n\t In the middle of your artful dodge your foot slips and you"
            "\n\t bang your head on the metal wall and pass out."
            "\n\t You wake up shortly after only to die as the Gothon stomps on"
            "\n\t your head and eats you."
            )
        return 'death'
           
    elif action == "tell a joke":
        print(
            "\n\t Lucky for you they made you learn Gothon insults in the academy."
            "\n\t You tell the one Gothon joke you know:"
            "\n\t 'Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr'"
            "\n\t The Gothon stops, tries not to laugh, then busts out laughing and can't move."
            "\n\t While he's laughing you run up and shoot him square in the head"
            "\n\t putting him down, then jump through the Weapon Armory door.")
        return 'laser_weapon_armory'
           
    else:
        print("DOES NOT COMPUTE!")
        return 'central_corridor'

def laser_weapon_armory(action):
    """
    You do a dive roll into the Weapon Armory, crouch and scan the room
    for more Gothons that might be hiding. It's dead quiet, too quiet.
    You stand up and run to the far side of the room and find the
    neutron bomb in its container.  There's a keypad lock on the box
    and you need the code to get the bomb out.  If you get the code
    wrong 10 times then the lock closes forever and you can't
    get the bomb.  The code is 3 digits.
    """
    #code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
    code = "123" # for debugging
    #guess = raw_input("[keypad]> ")
    guess = action # rename the functions parameter to match existing variable ``guess``
    guesses = 0
    
    while guess != code and guesses < 10:
        print("BZZZZEDDD!")
        guesses += 1
        guess = raw_input("[keypad]> ")
    
    if guess == code:
        print(
            "\n\tThe container clicks open and the seal breaks, leting gas out."
            "\n\tYou grab the neutron bomb and run as fast as you can to the"
            "\n\tbridge where you must place it in the right spot."
            )
        return 'the_bridge'
    
    else:
        print(
            "\n\tThe lock buzzes one last time and then you hear a sickening"
            "\n\tmelting sound as the mechanism is fused together."
            "\n\tYou decide to sit there, and finally the Gothons blow up the"
            "\n\tship from their ship and you die."
            )
        return 'death'

def the_bridge(action):
    """
    You burst onto the Bridge with the netron destruct bomb
    under your arm and surprise 5 Gothons who are trying to
    take control of the ship.  Each of them has an even uglier
    clown costume then the last.  They haven't pulled their
    weapons out yet, as they see the active bomb under your
    arm and don't want to set it off.
    """
          
    #action = raw_input("> ")
          
    if action == "throw the bomb":
        print(
            "\n\t In a panic you throw the bomb at the group of Gothons"
            "\n\t and make a leap for the door.  Right as you drop it a"
            "\n\t Gothon shoots you right in the back killing you."
            "\n\t As you die you see another Gothon frantically try to disarm"
            "\n\t the bomb.  You die knowing they will probably blow up when"
            "\n\t it goes off."
            )
        return 'death'
          
    elif action == "slowly place the bomb":
        print(
            "\n\t You point your blaster at the bomb under your arm"
            "\n\t and the Gothons put their hands up and start to sweat."
            "\n\t You inch backward to the door, open it, and then carefully"
            "\n\t place the bomb on the floor, pointing your blaster at it."
            "\n\t You then jump back through the door, punch the close button"
            "\n\t and blast the lock so the Gothons can't get out."
            "\n\t Now that the bomb is placed you run to the escape pod to"
            "\n\t get off this tin can!"
            )
        return 'escape_pod'
    else:
        print("DOES NOT COMPUTE!")
        return 'the_bridge'

def escape_pod(action):
    """
    You rush through the ship desperately trying to make it to
    the escape pod before the whole ship explodes.  It seems like
    hardly any Gothons are on the ship, so your run is clear of
    interference.  You get to the chamber with the escape pods, and
    now need to pick one to take.  Some of them could be damaged
    but you don't have time to look.  There's 5 pods, which one
    do you take?
    """
    
    good_pod = randint(1,5)
   # guess = raw_input("[pod #]> ")
    guess = action
    
    if int(guess) != good_pod:
        print(
            "\n\t You jump into the pod %s and hit the eject button." 
            "\n\t The pod escapes out into the void of space, then"
            "\n\t implodes as the hull ruptures, crushing your body"
            "\n\t into jam jelly." % guess)
        return 'death'
    else:
        print(
            "\n\t You jump into pod %s and hit the eject button." 
            "\n\t The pod easily slides out into space heading to"
            "\n\t the planet below.  As it flies to the planet, you look"
            "\n\t back and see your ship implode then explode like a"
            "\n\t bright star, taking out the Gothon ship at the same"
            "\n\t time.  You won!" % guess)
        exit(0)

ROOMS = {
    'death' : death,
    'central_corridor': central_corridor,
    'laser_weapon_armory': laser_weapon_armory,
    'the_bridge': the_bridge,
    'escape_pod': escape_pod
    }

# extra credit:
    """
    Zed says;
       "Once you have doc comments as the room description, do you need to
        have the function prompt even? Have the runner prompt the user, and
        pass that in to each function. Your functions should just be
        if-statements printing the result and returning the next room."
        
    Adding the prompt as a parameter to room() works, but we don't need
    a prompt for death(). So how do we not pass to this one function in the
    ROOMS dict?
    """

def runner(map, start):
    next = start
    
    while True:
        room = map[next]
        print "\n----------"
        print room.__doc__ # prints the description (doc string) of each function
        next = room(action = raw_input("> "))


if __name__ == "__main__":
    """
    start game!
    """
    runner(ROOMS, 'central_corridor')
