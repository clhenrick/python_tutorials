#! usr/bin/env python

"""
exercise 40: Modules, Classes, and Objects
"""

class Song(object):
    """this is a song class"""

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
    
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

print "\n"

bulls_on_parade.sing_me_a_song()

print "\n"

##########################################################
"""
extra credit here
"""

# pass lyrics to a variable rather than to the Song class
yes = ["close to the edge",
       "down by the river",
       "seasons will pass you by",
       "I get up, I get down"]

weird_al = ["they see me rolln'",
               "on my segway",
               "gonna catch me white n nerdy"]

yes_song = Song(yes) # create a new instance of the Song class and pass to it the variable yes

yes_song.sing_me_a_song() # call the built-in function sing_me_a_song

# create a "mix tape" dictionary to store my tunes!
mix_tape = {}

# add "close to the edge" as a song to the mix-tape
mix_tape["Close to the edge"] = Song(yes)
mix_tape["White n' Nerdy"] = Song(weird_al)

mix_tape["White n' Nerdy"].sing_me_a_song()


#create a new class based on Song that will reverse the lyrics
#not working yet...
class Reverse_Song(Song):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.index = len(lyrics)
    
    def __iter__(self):
        return self
    
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.lyrics[self.index]
    
    def reverse(self):
        iter(self.lyrics)
        for line in self.lyrics:
            print line

backwards_yes = Reverse_Song(yes)

backwards_yes.reverse()

iter(backwards_yes)
for line in backwards_yes:
    print line
