#! /usr/bin/env python

# exercise 40 LPTHW
# introducing dictionaries!
# lets you create pairs of associations in a container in the form of (key, value).
# not indexable like lists but are way cool.

cities = { 'CA': 'San Francisco', 'MI': 'Detroit', 
                   'FL': 'Miami'} # apparently you can have new lines and hella spaces between pairs

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

cities['_find'] = find_city # is this passing the function find_city() as the second item of the pair in the cities dictionary?

while True:
     print "State? (ENTER to quit)",
     state = raw_input("> ")
     
     if not state: break
     
     city_found = cities['_find'](cities, state) # assigns the variable city found to the
     # '_find' instance of cities and calls a function with parameters state and cities.
     print city_found

# extra-credit:     
# re-write while loop using cities.get(raw_input("> "), state)?
# print cities.items() # prints each item pair 
# print cities.keys() # prints only the keys
# print cities.values() # prints only the values