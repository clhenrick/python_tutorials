#! usr/bin/env python

"""
testing new stuff and debugging for ex36.py from LPTHW
To do: incorporate regular expressions;
    try IGNORECASE and searching "1" vs. "1735"

"""


def dispatcher():
    """
    Ask user which job they'd like to take
    """
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

if __name__ == "__main__":
    dispatcher()
