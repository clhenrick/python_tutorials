#! usr/bin/env python

"""
<<<<<<< HEAD
testing new stuff and debugging for ex36.py from LPTHW
=======
testing new stuff for ex36.py
>>>>>>> 84e80ec29d29da6fdd2846a2ecf48027d654253b
"""

#Ask user which job they'd like to take
print "\nYour dispatcher calls out three jobs, which one do you call on?"
<<<<<<< HEAD
print "\n\t 1. a job heading south to the Navy Yard \n\t 2. a job heading east to Olde City \n\t 3. a job staying local to 1735 Market St."
=======
print "\n\t 1. job heading south to the Navy Yard \n\t 2. job heading east to Olde City \n\t 3. job staying local to 1735 Market St."
>>>>>>> 84e80ec29d29da6fdd2846a2ecf48027d654253b

choice_made = False

while True:

    next = [raw_input(">")]

    first_choice = ("1", "south", "Navy", "Yard")
    second_choice = ("2", "east", "Olde", "City")
    third_choice = ("3", "local", "1735", "Market", "St.", "St")
    
<<<<<<< HEAD
    for i in next:
        if any(s in i for s in first_choice) and not choice_made:
            print "You're heading south!"
            choice_made = True
            #job_south(health, jobs +1, cash)
            exit(0)
    
    for j in next:
        if any(s in j for s in second_choice) and not choice_made:
            print "You're heading east!"
            choice_made = True
            #job_east(health, jobs +1, cash)
            exit(0)
            
    for k in next:
        if any(s in k for s in third_choice) and not choice_made:
            print "You're staying local!"
            choice_made = True
            #job_local(health, jobs +1, cash)
            exit(0)
            
    else:
        print "I didn't get that! Enter your choice again."
=======
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
            
            
        
    
>>>>>>> 84e80ec29d29da6fdd2846a2ecf48027d654253b
