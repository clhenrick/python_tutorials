#! usr/bin/env python

"""
exercise 36 from LPTHW
Build your own game!
****** Philly Bike Messenger v1.0 *****
to do:
   finish choice 3. and create functions for choice 1.
   how to best organize functions?
      or is there a more efficient way to do this?
   how to make game non-linear?
"""

from sys import exit
import re

"""
set variables for start of game to default values
"""

cash = 5
health = 100
jobs = 0

"""
start the game with the start_game() function.
function takes variable values for health, jobs, and cash.
"""

def start_game(health_count, jobs_count, cash_count):
    #Tells user objective of the game
    print "\nYou are a bicycle messenger cycling towards downtown Philly.\nYou must make as many deliveries as possible without dying!"
    print "Your current stats are:\n\t health: +%r\n\t jobs: %r\n\t cash: $%r" % (health_count, jobs_count, cash_count)
    dispatcher(health_count, jobs_count, cash_count)
    
def dispatcher(health_count, jobs_count, cash_count)
    
    #Ask user which job they'd like to take
    print "\nYour dispatcher calls out three jobs, which one do you call on?"
    print "\n\t 1. job heading south to the Navy Yard \n\t 2. job heading east to Olde City \n\t 3. job staying local to 1735 Market St."
    
    health_new = health_count
    jobs_new = jobs_count
    cash_new = cash_count
    
    choice_made = False
    
    while True:
    
        next = 	raw_input("> ")
    
        if "1" in next and not choice_made:
            job_south(health_new, jobs_new +1, cash_new)
            
        elif "2" in next and not choice_made:
            job_east(health_new, jobs_new +1, cash_new)
            
        elif "3" in next and not choice_made:
            job_local(health_new, jobs_new +1, cash_new)
            
        else:
            # tell user to call on a job and go back to top of loop
            print "your dispatcher said; 'call on a job knuckle head!'"
            #start_game(health, jobs, cash)

"""
function to end the game here.
takes one argument <why> which states reason why game ended
"""
 
def end_game(why):
    """
    ends the game and tells the user why.
    	"""
    print why, "It sure is rough out there!"
    exit(0)


"""
first three choices from start_game() are here:
"""

def job_local(health_count, jobs_count, cash_count):    
    print "You're staying local. \nYou have %r job(s) in your bag." % jobs_count
    print "Do you make your delivery or wait?"
    
    health_new = health_count
    jobs_new = jobs_count
    cash_new = cash_count
    
    choice_made = False
    
    while True:
        next = raw_input("?")

        if "make" in next:
            health_new = health_new -100
            end_game("You were just run over by a bus!")
            
        if "wait" in next:
            print "How many minutes do you wait?"
            time = int(raw_input("?"))
            
            if time < 30:
                print "\nYour dispatcher just offered you a super rush going to the same address!\nThis job pays $30 should you complete it."
                print "\nDo you take it?"
                
                input = raw_input("y/n ")
                
                if input == "y":
                    jobs_new = jobs_new + 1
                    super_local(health_new, jobs_new, cash_new)
                    
                else:
                    end_game("That was a dumb choice!")
            
            else:
               end_game("Man you're lazy and are fired!")
                    
def job_east(health_count, jobs_count, cash_count): 
    print "You made your pick up and have %r job(s) in your bag." % jobs_count
    print "Do you head east or wait for another job heading that way?"
    
    health_new = health_count
    jobs_new = jobs_count
    cash_new = cash_count
    
    choice_made = False
    
    while True:
    
        next = raw_input(">")
    
        if "east" in next or "head" in next and not choice_made:
            head_east_no_rush(health_new, jobs_new, cash_new)
        
        elif "wait" in next and not choice_made:
            print "You wait 15 minutes. Your dispatcher informs you she has another job heading east, a rush! Way to be patient."
            print "Do you call on the rush?"
        
            choice = raw_input(">")
        
            if choice == "yes":
                head_east(health, jobs +1, cash)
            else:
                end_game("Your boss said you're too lazy and fired you.")
        else:
            print "Not sure what you're saying."
 
def job_south(health_count, jobs_count, cash_count):
    print "You have %r jobs. Do you wait for another job going south or do you roll out?" % jobs_count
    
    next = raw_input("?")

"""
second set of job choices here:
"""    

def super_local(health_count, jobs_count, cash_count):
    print "\nOkay you have 15 minutes to complete the super rush.\nDo you deliver it or your other job?"

def head_east(health_count, jobs_count, cash_count):
    print "You are heading east with %r job(s)" % jobs_count
    print "Which job do you deliver first? The rush or the regular one?"
    
    next = raw_input(">")
    
    if "rush" in next:
        print "Awesome, you just made $15!"
        cash_new = cash_count + 15
        jobs_new = jobs_count - 1
        health_new = health_count
        print "You now have $%d in your pocket and %d jobs in your bag." % (cash_new, jobs_new)
        print "Do you make your second delivery now or get some coffee first?"
            
        next2 = raw_input("?")
        choice_made = False
        
        #new if-then-else statement for 2nd choice:
        
        if "coffee" in next2 and not choice_made:
            print "awesome, you can kick it for a minute. \n hit return when you're ready."
                
            kick_it = raw_input(">")
                   
            print "You are now caffienated and you made your delivery. Score!"
            cash_new = cash_new + 7
            jobs_new = jobs_new - 1
            print "You now have $%d in your pocket and %d job(s) in your bag." % (cash_new, jobs_new)
            finished_east(health_new, jobs_new, cash_new)
            
        elif "make" in next2 and not choice_made:
            print "ouch you just got doored!"
                
            health_new = health_new - 20
            cash_new = cash_new + 7
            jobs_new = jobs_new - 1
                
            print "your health is now +%d" % health_new
            print "You now have $%d in your pocket and %d jobs in your bag." % (cash_new, jobs_new)
                
            finished_east(health_new, jobs_new, cash_new)
            
        else:
            print "I didn't get that..."
    
    else:
        end_game("You're late with the rush! You're fired!")

def head_east_no_rush(health_count, jobs_count, cash_count):
    print "You're heading east with %r job." % jobs_count
    exit(0) #tempoary exit function, remove after finishing this branch of the game.

"""
third set of job choices:
"""

def finished_east(health_count, jobs_count, cash_count):
    print "Now, do you hang east for a minute or go back to downtown?"
    next = raw_input("?")

"""
start the game here!
"""

start_game(health, jobs, cash)