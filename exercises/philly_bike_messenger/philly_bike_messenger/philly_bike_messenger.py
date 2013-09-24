#! usr/bin/env python
# Learn Python the Hardway
# Exercise 43: make your own `Zork` adventure game using classes and modules
# User chooses between jobs and must accumulate money by completing jobs while not dying.

from sys import exit
from random import randint
from first_branch, second_branch, third_branch

class Stage(object):
    """Creates each stage or level of the game"""
    def enter(self):
        print("This is a parent class for the game's stages."
               "Subclass it and implement enter().")
        exit(1)

class Engine(object):
    """Runs the Game"""
    
    def __init__(self, stage_map):
        self.stage_map = stage_map
    
    def play(self):
        current_stage = self.stage_map.opening_stage()
        
        while True:
            print "\n============================="
            next_stage_name = current_stage.enter()
            current_stage = self.stage_map.next_stage(next_stage_name)

class Dead(Stage):
    """The death stage where player dies. Ends game."""

class Dispatcher(Stage):
    """ Follows StartGame() """
    def enter(self):
        pass

class StartGame(Stage):
    """The first stage of the game."""
    
    stats = {
		'cash' : 20.00,
		'health' : 100,
		'jobs' : 0,
		'completed_jobs' : 0
		}
        
    def begin(self, stats):
        print("\n*************** PHILLY BIKE MESSENGER v0.1 ***************\n"
			  "\nYou are a bicycle messenger cycling towards downtown Philly."
			  "\nYou must make as many deliveries as possible without dying!"
			  "\nYour current stats are:"
			  "\ncash: %r"
			  "\nhealth: %r"
			  "\njobs: %r"
			  "\ncompleted jobs: %r" (stats['cash'], stats['health'], stats['jobs'], stats['completed_jobs']))

