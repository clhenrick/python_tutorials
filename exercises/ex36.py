#! usr/bin/env python

"""
exercise 36 from Learn Python the Hard Way
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
jobs = 0 #number of deliveries in messenger's bag as an integer
jobs_completed = 0 #total number of jobs delivered

def start_game(health, jobs, cash):
    """
    start the game with the start_game() function.
    function takes variable values for health, jobs, and 	cash.
    """
    print("\n**************** PHILLY BIKE MESSENGER v0.1 ****************\n"
      "\nYou are a bicycle messenger cycling towards downtown Philly."
      "\nYou must make as many deliveries as possible without dying!"
      "\nYour current stats are:"
      "\n\t *health: +%r"
      "\n\t *jobs: %r"
      "\n\t *cash: $%r" % (health, jobs, cash))

    dispatcher(health, jobs, cash)

def dispatcher(health_count, jobs_count, cash_count):
    """
    follows start_game()
    """
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
 
def end_game(why, health, jobs_completed, cash):
    """
    ends the game and tells the user why.
    gives user final stats, including the total number of jobs completed.
    """
    health_final = health
    jobs_final = jobs_completed 
    cash_final = cash
    
    print("%s" 
          "\nIt sure is rough out there!"
          "\n\n\tFINAL STATS:"
          "\n\t*health: %r"
          "\n\t*total jobs delivered: %r"
          "\n\t*cash: $%r" % (why, health_final, jobs_final, cash_final))
    exit(0)


# first three choices from start_game() are here:
# this set of choices take health, jobs, cash
################################################

def job_south(health_count, jobs_count, cash_count):
    """
    follows first choice from dispatcher()
    """
    print("You made your pick up and have %r jobs in your bag."
          "\nDo you wait for another job going south or do you roll out?" % jobs_count)
    
    health_new = health_count
    jobs_new = jobs_count
    cash_new = cash_count
    
    choice_made = False
    
    while True:
        next = raw_input("?")
        
        if "south" in next or "roll" in next and not choice_made:
           end_game("All of a sudden you're in outer space?",health_new-100,jobs_completed,cash_new)
           
        elif "wait" in next and not choice_made:
            choice_made=True
            print("How many minutes do you want to wait?")
            time = int(raw_input("> "))
            
            if time < 30:
               print("\nYour dispatcher says she's got nothin! You better roll out..."
                     "\nSo do you roll?")
                     
               decision = raw_input("Y?N")
                     
               if decision == "y" or decision == "Y":
                   print("Sweet, you're heading south")
                   gone_south(health_new, jobs_new, cash_new)
                     
            else:
                end_game("You're fired for being lazy. Are we learning yet young grasshopper?",health_new,jobs_completed,cash_new)
                
        else:
            print("I didn't get that brah!")
            job_south(health_new,jobs_new,cash_new)

def job_east(health_count, jobs_count, cash_count):
    """
    follows second choice from dispatcher()
    """
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
                end_game("Your boss said you're too lazy and fired you.",health_new,jobs_completed,cash_new)
        else:
            print("Not sure what you're saying.")

def job_local(health_count, jobs_count, cash_count):  
    """
    follows third choice from dispatcher()
    """  
    print("\nYou're staying local."
          "\nYou made your pick up and have %r job(s) in your bag." 
          "\nDo you make your delivery or wait?" % jobs_count)
    
    health_new = health_count
    jobs_new = jobs_count
    cash_new = cash_count
    
    choice_made = False
    
    while True:
        next = raw_input("> ")

        if "make" in next and not choice_made:
            health_new = health_new -100
            end_game('You were just run over by a bus!',health_new, jobs_completed, cash_new)
            
        elif "wait" in next and not choice_made:
            print ("How many minutes do you wait?")
            time = int(raw_input("> "))
            
            if time < 30:
                print("\nYour dispatcher just offered you a super rush going to the same address!"
                      "\nWay to get lucky!"
                      "\nThis job pays $30 should you complete it."
                      "\nDo you take it?")
                
                decision = False
                
                while True:
                    input = raw_input("y/n ")
                    
                    if input == "y" or input == "Y" and not decision:
                        jobs_new = jobs_new + 1
                        decision = True
                        super_local(health_new, jobs_new, cash_new)
                    
                    elif input == "N" or input == "n":
                        end_game("That was a dumb choice!",health_new,jobs_completed,cash_new)
                        
                    else:
                        print("What did you say?")
            
            else:
               end_game("Man you waited too long and just got fired!",health_new,jobs_completed,cash_new)
                    
        else:
            print("Didn't get that, learn to use your radio!")

# second set of job choices here
# if user successfully navigates one then jobs_completed +1
######################################################

def gone_south(health_count, jobs_count, cash_count):
    """
    follows job_south() if user doesn't die
    """
    health_new = health_count
    jobs_new = jobs_count
    jobs_completed=0
    cash_new = cash_count
    
    print("\nOh man some guy is behind you blaring his horn."
          "\nDo you FTB (Flip him The Bird), throw your u-lock at him, or brush it off?")
          
    choice = raw_input("? ")  
    
    first_pattern="flip|bird|ftb|throw|u-lock"
    second_pattern="brush|off|ignore"
    
    if re.search(first_pattern, choice, re.I):
        end_game("He just ran you over!",health_new-100,jobs_completed,cash_new)
        
    elif re.search(second_pattern, choice, re.I):
        jobs_new=jobs_new-1
        jobs_completed=1
        cash_new=cash_new+15
        
        print("\nWise choice, these South Philly drivers are crazy!"
              "\nYou managed to avoid the crazies and make your delivery. Good job!"
              "\nYour current stats are:"
              "\n\t *jobs completed: %r"
              "\n\t *cash: %r"
              "\n\t *health: %r" % (jobs_completed,cash_new,health_new))
    
    else:
        print("I didn't get that, tell me again.")
        gone_south(health_new,jobs_new,cash_new)
       
    exit(0) #temporary exits until this part of game is finished.
              
def super_local(health_count, jobs_count, cash_count):
    """
    Follows successful navigation of job_east()
    """
    print("\nOkay you have 15 minutes to complete the super rush."
          "\nDo you deliver it first or your other job?")
    health_new = health_count
    jobs_new = jobs_count
    cash_new = cash_count
    next = raw_input("> ")
    
    if "deliver" in next:
        print("\nWay to go!"
              "\nYou just made $30!")
         
        cash_new = cash_new + 30
        jobs_new = jobs_new - 1
        jobs_completed = 1
        
        print("\nYour current stats are:"
              "\n\t *jobs completed: %r"
              "\n\t *jobs in your bag: %r"
              "\n\t *cash: %r"
              "\n\t *health: %r" % (jobs_completed,jobs_new,cash_new,health_new))
        
        local_regular(health_count, jobs_completed, jobs_new, cash_new)
    
    elif "other" in next:
        print("Okay you delivered your other job, but now you're late with the super rush and are fired!")
        cash_new = cash_new + 7.50
        jobs_new = jobs_new -1
        jobs_completed = 1
        end_game('Learning are we?',health_new,jobs_completed,cash_new)
    
    else:
        print("I didn't understand that.")
        super_local(health_new, jobs_new, cash_new)

def local_regular(health_count, jobs_completed, jobs_count, cash_count):
    print("\nYou still have that other local job, and it's in the same building you're currently in." 
          "\nDo you deliver it or wait?")
    
    next = raw_input("> ")
    
    exit(0) # end game. temporary until finish this part.

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
    

# start the game if script is not being imported.
######################################################
    
if __name__ == "__main__":
    """
    start the game here!
    """
    start_game(health, jobs, cash)