#! usr/bin/env python

"""
testing new stuff and debugging for ex36.py from LPTHW
To do: incorporate regular expressions;
    try IGNORECASE <done>
        and searching "1" vs. "1735" <use the \d escape code?>
"""

import re

# fixed error for "1" and "1735" but feel I am not understanding the use of \d in re ...
# also added a print statement to debug and also to double check user entered desired choice.
def dispatcher():
    
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
           print "you're heading south."
        else:
           dispatcher()
        
    elif re.search(second_pattern, choice, re.I):
        print("You said %r, so you're calling on the east job?" 
              "\nY/N?" % choice)
              
        yes_no = raw_input("> ")
        
        if "Y" in yes_no or "y" in yes_no:
           print "you're heading east."
        else:
           dispatcher()
           
    elif re.search(third_pattern, choice, re.I):
        print("You said %r, so you're calling on the local job?"
              "\nY/N?" % choice)
              
        yes_no = raw_input("> ")
        
        if "Y" in yes_no or "y" in yes_no:
           print "you're staying local."
        else:
           dispatcher()
    else:
        print("I didn't get that, tell me again.")
        dispatcher()



# second try; using regular expressions but didn't quite get the syntax right:
"""
def dispatcher():

    first_choice = ("1", "south", "Navy", "Yard")
    second_choice = ("2", "east", "Olde", "City")
    third_choice = ("3", "local", "1735", "Market", "St.", "St")

    print("\nYour dispatcher calls out three jobs, which one do you call on?"
          "\n\t 1. a job heading south to the Navy Yard"
          "\n\t 2. a job heading east to Olde City"
          "\n\t 3. a job staying local to 1735 Market St.")
	
	
	
    for choice in [raw_input(">")]:        
		if re.search(choice, first_choice, re.I):
		    print("You said; %r") % choice
			#print("You're heading south!")
		elif [re.search(choice, choice, re.I) for choice in second_choice]:
			print("You're heading east!")
		elif [re.search(choice, choice, re.I) for choice in third_choice]:
			print("You're staying local!")
		else:
			print("I didn't get that, tell me again.")
			dispatcher()
"""



# first try, resulted in 1 and 1735 not being read differently:
"""
def dispatcher():

    first_choice = ("1", "south", "Navy", "Yard")
    second_choice = ("2", "east", "Olde", "City")
    third_choice = ("3", "local", "1735", "Market", "St.", "St")

    print("\nYour dispatcher calls out three jobs, which one do you call on?"
          "\n\t 1. a job heading south to the Navy Yard"
          "\n\t 2. a job heading east to Olde City"
          "\n\t 3. a job staying local to 1735 Market St.")

    for choice in [raw_input("> ")]:
        if any(c in choice for c in first_choice):
            print("You're heading south!")  #job_south(health, jobs +1, cash)
        elif any(c in choice for c in second_choice):
            print("You're heading east!")  #job_east(health, jobs +1, cash)
        elif any(c in choice for c in third_choice):
            print("You're staying local!")  #  job_local(health, jobs +1, cash)
        else:
            print "I didn't get that! Enter your choice again."
            dispatcher()

"""

if __name__ == "__main__":
    dispatcher()


 