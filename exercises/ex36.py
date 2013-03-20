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


#set variables for start of game to default values
cash = 5.00 #amount of money as $
health = 100 #health as %
jobs = 0 #number of deliveries in messenger's bag as an integer.

def start_game(health, jobs, cash):
    """
    start the game with the start_game() function.
    function takes variable values for health, jobs, and 	cash.
    """
    print("\n**************** PHILLY BIKE MESSENGER v0.1 ****************\n"
      "\nYou are a bicycle messenger cycling towards downtown Philly."
      "\nYou must make as many deliveries as possible without dying!"
      "\nYour current stats are:"
      "\n\t health: +%r"
      "\n\t jobs: %r"
      "\n\t cash: $%r" % (health, jobs, cash))

    dispatcher(health, jobs, cash)

def dispatcher(health_count, jobs_count, cash_count):    
    health_new = health_count
    jobs_new = jobs_count
    cash_new = cash_count
    
    print("\nYour dispatcher calls out three jobs, which one do you call on?"
      "\n\t 1. a job heading south to the Navy Yard"
      "\n\t 2. a job heading east to Olde City"
      "\n\t 3. a job staying local to 1735 Market St.")
    
    first_pattern = "1$|south|Navy|Yard"
    second_pattern = "^2|east|Olde|City"
    third_pattern = "^3|local|1735|Market|St|St."
    
    choice = raw_input("> ")
    
    if re.search(first_pattern, choice, re.I):
        print("You said %r, so you're calling on the south job?"
              "\nY/N?" % choice)
              
        yes_no = raw_input("> ")
        
        if "Y" in yes_no or "y" in yes_no:
           job_south(health_new, jobs_new +1, cash_new)
        else:
           dispatcher(health_new, jobs_new, cash_new)
        
    elif re.search(second_pattern, choice, re.I):
        print("You said %r, so you're calling on the east job?" 
              "\nY/N?" % choice)
              
        yes_no = raw_input("> ")
        
        if "Y" in yes_no or "y" in yes_no:
           job_east(health_new, jobs_new +1, cash_new)
        else:
           dispatcher(health_new, jobs_new, cash_new)
           
    elif re.search(third_pattern, choice, re.I):
        print("You said %r, so you're calling on the local job?"
              "\nY/N?" % choice)
              
        yes_no = raw_input("> ")
        
        if "Y" in yes_no or "y" in yes_no:
           job_local(health_new, jobs_new +1, cash_new)
        else:
           dispatcher(health_new, jobs_new, cash_new)
    else:
        print("I didn't get that, tell me again.")
        dispatcher(health_new, jobs_new, cash_new)    
 
def end_game(why):
    """
    ends the game and tells the user why.
    """
    health_final = health
    jobs_final = jobs #change this so that a variable is made to store the number of jobs a user completed
    cash_final = cash
    
    print("%s" 
          "\nIt sure is rough out there!"
          "\n\n\tFINAL STATS:"
          "\n\t*health: %r"
          "\n\t*jobs: %r"
          "\n\t*cash: $%r" % (why, health_final, jobs_final, cash_final))
    exit(0)


#first three choices from start_game() are here:
################################################

def job_local(health_count, jobs_count, cash_count):  
    """
    third choice from dispatcher()
    all choices take health, jobs, and cash 
    """  
    print("You're staying local."
        "\nYou have %r job(s) in your bag." 
        "\nDo you make your delivery or wait?" % jobs_count)
    
    health_new = health_count
    jobs_new = jobs_count
    cash_new = cash_count
    
    choice_made = False
    
    while True:
        next = raw_input("> ")

        if "make" in next and not choice_made:
            health_new = health_new -100
            end_game('You were just run over by a bus!')
            
        elif "wait" in next and not choice_made:
            print ("How many minutes do you wait?")
            time = int(raw_input("> "))
            
            if time < 30:
                print("\nYour dispatcher just offered you a super rush going to the same address!"
                      "\nThis job pays $30 should you complete it."
                      "\nDo you take it?")
                
                input = raw_input("y/n ")
                
                if input == "y":
                    jobs_new = jobs_new + 1
                    super_local(health_new, jobs_new, cash_new)
                    
                else:
                    end_game("That was a dumb choice!")
            
            else:
               end_game("Man you're lazy and just got fired!")
                    
        else:
            print("Didn't get that, learn to use your radio!")

def job_east(health_count, jobs_count, cash_count): 
    print("You made your pick up and have %r job(s) in your bag."
          "\nDo you head east or wait for another job heading that way?" % jobs_count)
    
    health_new = health_count
    jobs_new = jobs_count
    cash_new = cash_count
    
    choice_made = False
    
    while True:
    
        next = raw_input(">")
    
        if "east" in next or "head" in next and not choice_made:
            head_east_no_rush(health_new, jobs_new, cash_new)
        
        elif "wait" in next and not choice_made:
            print("You wait 15 minutes. Your dispatcher informs you she has another job heading east, a rush! Way to be patient."
                  "\nDo you call on the rush?")
        
            choice = raw_input(">")
        
            if choice == "yes":
                head_east(health, jobs_new +1, cash)
            else:
                end_game("Your boss said you're too lazy and fired you.")
        else:
            print "Not sure what you're saying."
 
def job_south(health_count, jobs_count, cash_count):
    print("You have %r jobs."
          "\nDo you wait for another job going south or do you roll out?" % jobs_count)
    
    next = raw_input("?")


#second set of job choices here:
######################################################    

def super_local(health_count, jobs_count, cash_count):
    print("\nOkay you have 15 minutes to complete the super rush."
          "\nDo you deliver it or your other job?")
    health_new = health_count
    jobs_new = jobs_count
    cash_new = cash_count
    next = raw_input("> ")
    
    if "deliver" in next:
        print("\nWay to go!"
              "\nYou just made $30!")
        cash_new = cash_new + 30
        jobs_new = jobs_new - 1
    
    else:
        print("Okay you delivered your other job, but now you're late with the super rush!")
        end_game('Learning are we?')

def head_east(health_count, jobs_count, cash_count):
    print "You are heading east with %r job(s)" % jobs_count
    print "Which job do you deliver first? The rush or the regular one?"
    
    next = raw_input("> ")
    
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


#third set of job choices:
######################################################    

def finished_east(health_count, jobs_count, cash_count):
    print "Now, do you hang east for a minute or go back to downtown?"
    next = raw_input("> ")
    

######################################################    
if __name__ == "__main__":
    """
    start the game here!
    """
    start_game(health, jobs, cash)