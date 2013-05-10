#! /usr/bin/env python

cities = {'CA': 'Oakland', 'NV': 'Reno', 'OR': 'Corvalis', 'NJ': 'Trenton', 'NY': 'New York'}

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

cities['state']=find_city

for city in cities['state']:
   print "The city name is: %s" % city

