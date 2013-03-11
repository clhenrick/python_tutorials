#! usr/bin/env python

"""
exercise 36 from LPTHW
Build your own game!
****** Philly Bike Messenger v1.0 *****
"""

from sys import exit

cash=0
health=100
jobs=0

def start_game():
    #Tells user objective of the game
    print "\nYou are a bicycle messenger cycling into downtown Philly.\nYou must make as many deliveries as possible without dying!"
    print "\t Your health is %r\n\t Your cash is %r\n\t Your number of jobs is %r" % (health, cash, jobs)
    
    #Ask user which job to take
    print "\nYour dispatcher calls out three jobs, which one do you call on?"
    print "\n\t 1. job heading south to the Navy Yard \n\t 2. job heading east to Olde City \n\t 3. job staying local to 1735 Market St."
    
    next = 	raw_input("> ")
    
    if "1" in next:
        job_south()
    elif "2" in next:
        job_east()
    elif "3" in next:
        job_local()
    else:
        print "your dispatcher said; 'call on a job knuckle head!'"


def end_game(why):
    """ends the game and tells the user why."""
    print why, "It sure is rough out there!"
    exit(0)

def job_south():
    jobs = + 1
    print "You're heading south with %r job(s)." % jobs


def job_east():
    jobs = + 1
    print "You're heading east with %r job(s)." % jobs

def job_local():    
    jobs = + 1
    print "You're staying local. \nYou have %r job(s) in your bag." % jobs
    
start_game()