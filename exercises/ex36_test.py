#! usr/bin/env python

"""
testing new stuff for ex36.py
"""

#Ask user which job they'd like to take
print "\nYour dispatcher calls out three jobs, which one do you call on?"
print "\n\t 1. job heading south to the Navy Yard \n\t 2. job heading east to Olde City \n\t 3. job staying local to 1735 Market St."

choice_made = False

while True:

    next = [raw_input(">")]

    first_choice = ("1", "south", "Navy", "Yard")
    second_choice = ("2", "east", "Olde", "City")
    third_choice = ("3", "local", "1735", "Market", "St.", "St")
    
    for k in next:
        if any(s in k for s in first_choice) and not choice_made:
            print "You're heading south!"
            choice_made = True
            exit(0)
    
    for i in next:
        if any(s in i for s in second_choice) and not choice_made:
            print "You're heading east!"
            choice_made = True
            exit(0)
            
    for j in next:
        if any(s in j for s in third_choice) and not choice_made:
            print "You're staying local!"
            choice_made = True
            exit(0)
            
    else:
        print "I don't understand! Enter your choice again."
            
            
        
    