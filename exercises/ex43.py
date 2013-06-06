#! usr/bin/env python

# exercise 43: Basic Object Oriented Analysis and Design

from sys import exit
from random import randint

class Scene(object):
    """Creates each level or scene of the game"""
    def enter(self):
        print("This is a base class for the game's scenes."
              "Subclass it and implement enter().")
        exit(1)

class Engine(object):
    """Runs the game"""

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print "\n---------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    """
       The Death scene, where the player has died.
       Ends the game.
    """
    
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luuuuzer!",
        "I have a small puppy that's better at this."
    ]
    def enter(self): 
        """cycle through the quips list and print a random
           list value by using the randint method and passing
           the values for the first list item and last list item
        """
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):
    """
       The Central Corridor Scene,
       First Scene of game,
       player must navigate to the armory
    """

    def enter(self):
        print("You're the remaining survivor on a spaceship that"
              "\nhas had its entire crew wiped out by invading space"
              "\naliens called Gothons. You're mission is to get to the"
              "\nweapons armory, grab a nuke, place it in the ships's bridge,"
              "\nand then make off in an escape pod before it blows up"
              "\nthe Gothons and your ship."
              "\n"
              "\nFirst you are face to face with a Gothon. Do you:"
                  "\n\tshoot"
                  "\n\tdodge"
                  "\n\ttell a joke")
        
        action = raw_input("? ")
        
        if action == "shoot":
            print "You missed and the Gothon eats you!"
            return 'death'
        elif action == "dodge":
            print "You slipped and fell. The Gothon gobbles you up!"
            return 'death'
        elif action == "tell a joke":
            print "The Gothon cracks up laughing which gives you an"
            print "oppurtune moment to split his head open with your"
            print "light saber!"
            return 'laser_weapon_armory'
        else:
            print "Does not Compute!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    """The Laser Weapon Armory Scene,
       player must defeat the Gothon and
       grab the bomb"""
    
    def enter(self):
        print("You enter the laser Armory, and must"
              "\nunlock the bomb by entering the secret code."
              "\nYou have 10 chances to enter the correct 3 digit code."
              "\nIf you fail the bomb will lock and become useless.")
        #code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        code = "123" # for debugging rest of game
        guess = raw_input("[keypad]> ")
        guesses = 1
        
        while guess != code and guesses < 10:
            print "BZZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
            
        if guess == code:
            print("The container clicks open and you grab the bomb."
                  "\nNice work!")
            return 'the_bridge'
        else:
            print ("The lock buzzes one last time and fuzes together..."
                   "\nFAIL!")
            return 'death'

class TheBridge(Scene):
    """The Bridge Scene,
        player must successfully place bomb
        and run away"""

    def enter(self):
        print ("You burst onto the Bridge with the bomb."
               "\nDo you:"
               "\n\tThrow the bomb"
               "\n\tslowly place the bomb")
    
        action = raw_input("? ")
        
        if action == "throw bomb":
            print("You toss the bomb and run for the door"
                  "\nbut you get shot in the back.")
        
        elif action == "slowly place the bomb":
            print("You point your gun at the bomb while slowly laying it down."
                  "\nYou back away slowly out the door, close it, and blast the lock."
                  "\nNow you head to the escape pod to get off this ship before it blows-up!")
            return 'escape_pod'
        else:
            print "Does not compute!"
            return 'the_bridge'

class EscapePod(Scene):
    """The Escape Pod Scene,
       player must choose the correct escape pod"""
     
    def enter(self):
        print ("You rush through the ship to the escape pods before everything explodes."
                "\nYou now have to pick a pod. There are 5 to choose from."
                "\nHowever some may be damaged. Which pod do you pick?"
                "\n...enter a single digit 1-5")
        
        #good_pod = randint(1,5)
        good_pod = 1 # for debugging rest of game
        guess = raw_input("? ")
        
        if int(guess) != good_pod:
            print("You jump into pod %s and eject it from the ship." 
                  "\nUnfortunately the pod implodes and crushes you into jelly." % guess)
            return 'death'
        else:
            print("You jump into the pod %s and eject it from the ship."
                  "\nThe pod sends you away from the ship towards the planet below."
                  "\nYou watch as the ship explodes while taking out the Gothon ship"
                  "\nat the same time. Congrats, you won!" % guess)
        
        return 'finished'
    
class Finished(Scene):
    """The end of the game, exits python"""
    
    def enter(self):
        exit(0)

class Map(object):
    
    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory' : LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'death' : Death(),
        'finished' : Finished()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()