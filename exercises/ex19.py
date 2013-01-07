#! usr/bin/env python
#exercise 19: Functions and Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers+1000)

#extra credit: make your own function! okay here we go...

def bikes_and_beer(number_bikes, number_beers, alley_cat_name):
    print "There are %r bikes." % number_bikes
    print "There are %r beers." % number_beers
    print "So %r bikes and %r beers will be enough for the %s alleycat?" % (number_bikes, number_beers, alley_cat_name)
    print "I dunno..."
    
print "So looks like we may be in trouble..."
bikes = raw_input("number of bikes? ")
beers = raw_input("number of beers? ")
alleycat = raw_input("what's the name of this alley cat? ")

bikes_and_beer(bikes, beers, alleycat) 