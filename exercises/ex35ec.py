#! usr/bin/env python

""" exercise 35: branches and functions
extra credit 4 & 5: expand upon, simplify, and improve game
"""

from sys import exit

def gold_room():
    """simplified gold room stage / fixed checking next for a number.
    if a number is not entered then user is prompted to enter one.
    """
    print "This room is full of gold. How much do you take?"
    try:
        next = int(raw_input("> "))
    except:
        print "Give me a whole number."
        gold_room()
        
    if next < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    """ left door option from start()
    Asks the user how to interact with the bear.
    Based on input the user either goes on to the gold room or loses the game.
    """
    
    #simplified print
    print "There is a bear here.\nThe bear has a bunch of honey.\nThe fat bear is in front of another door.\nHow are you going to move the bear?"
    
    #added for extra credit:
    print "Your options are: \n \t take honey \n \t taunt bear"
    
    bear_moved = False #still unsure of how this works / what it does...
    
    while True:
        next = raw_input("> ")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
            
            #extra credit, added options:
            print "Your options are: \n \t kick bear \n \t shoot bear \n \t open door"
            
            choice2 = raw_input(">> ")
            
            if choice2 == "kick bear":
                dead("Bear gets mad and eats you.")
            elif choice2 == "shoot bear":
                dead("You missed. The bear chews you up.")
            elif choice2 == "open door":
                gold_room()                
            else:
                print "I don't understand."
        
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    """right door option from start()
    user either goes back to start or loses game.
    """
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    """the user has lost the game
    tells user why and then 'Good job!'
    """
    print why, "Good job!"
    exit(0)

def start():
    """start of game, gives user an option for a left or right door
    if neither is chosen user loses and game ends.
    """
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()