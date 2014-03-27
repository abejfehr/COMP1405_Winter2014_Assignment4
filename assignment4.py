#=============================================#
# Assignment 4: A simulation of an ant colony #
# File:   assignment4.py                      #
# Author: Abe Fehr                            #
# Date: Unknown                               #
#=============================================#

import random

#a list of names and genders...because having nameless ants is no fun
names = [["John","m"],
         ["Pete","m"],
         ["Lisa","f"],
         ["Mary","f"],
         ["Anna","f"],
         ["Tom","m"],
         ["Ben","m"],
         ["Jan","f"],
         ["Alex","m"],
         ["Alexa","f"],
         ["Leo","m"],
         ["Leanne","f"],
         ["Derpina","f"],
         ["Derp","m"],
         ["Howard","m"],
         ["Penny","f"]]



###
# Class: Colony
# 
# Represents an ant colony
###
class Colony(object):    
    def __init__(self):
        self.ants = []
        self.food = 10



    ###
    # Function: breedWorker
    # Purpose:  Breeds a new ant and adds it to the colony
    ###
    def breedWorker(self):
        if(self.food >= 5):
            self.food -= 5
            baby = Ant()
            print "A bouncing baby %s was born, %s name was %s!" % (("boy" if (baby.gender=="m") else "girl"), baby.possessivepronoun(False), baby.name)
            self.ants.append(baby)
        else:
            print "There is not enough food for an ant"



    ###
    # Function: step
    # Purpose:  Performs one step of the simulation. Each ant should forage
    #           for food, and give each ant their daily provisions of food
    ###
    def step(self):
        for ant in self.ants:
            self.food += ant.forage()
            if(self.food > 0):
                self.food -= 1
            else:
                ant.health -= 1
                if(ant.health == 0):
                    print ant.name + " has died of starvation!"
        
        
        
    ###
    # Function: purge
    # Purpose:  Goes through the colony and removes all the dead ants
    ###
    def purge(self):
        temp = []
        for ant in self.ants:
            if(ant.health > 0):
                temp.append(ant)
            else:
                self.food += 1
        self.ants = temp
    
    
    
###
# Class: Ant
# 
# Represents a worker ant
###
class Ant(object):
    global names
    
    
    
    ###
    # Function: Constructor
    # Purpose:  Initializes an ant with 10 health, a random name and a gender
    ###
    def __init__(self):
        self.health = 10
        i = random.randint(0, len(names)-1)
        self.name = names[i][0]
        self.gender = names[i][1]



    ###
    # Function: forage
    # Purpose:  Tells the ant to go out and look for food
    # Returns:  The amount of food the ant found
    ###
    def forage(self):
        chance = random.randint(1,100)
        if(chance < 5):
            self.health = 0
            print self.name + " died in a horrible accident"
            return 0
        elif(chance < 40):
            food = random.randint(1,4)
            print self.name + " found %g food!" % food
            return food
        elif(chance < 98):
            print self.name + " found no food"
            return 0
        else:
            health = 10
            print self.name + " found sweet nectar! %s health was replenished" % self.possessivepronoun(True)
            return 5
       

 
    ###
    # Function: possessivepronoun
    # Purpose:  Gets the possessive pronoun for the ant
    # Input:    capitalized - Whether the pronoun should be capitalized or not
    # Returns:  The ant's posessive pronoun depending on gender
    ###
    def possessivepronoun(self, capitalized):
        if(self.gender == "m"):
            return "His" if capitalized else "his"
        else:
            return "Her" if capitalized else "her"

###
# Function: main
# Purpose:  The entry point for the simulation
###
def main():
    colony = Colony()
    while(len(colony.ants) > 0 or colony.food >= 5):
        print "==============================================="
        print "Your colony has %g ant%s and %g food, Your Majesty" % (len(colony.ants), ("" if (len(colony.ants)==1) else "s"), colony.food)
        print "What would you like to do?"
        print "0. Do nothing"
        print "1. Breed worker (costs 5 food)"
        isValid = False
        choice = ""
        while(not isValid):
            choice = raw_input(">")
            if(choice == "0" or choice == "1"):
                isValid = True
        if(choice == "1"):
            colony.breedWorker()
        colony.step()
        colony.purge()
    print "There is no hope for your colony, I hope you're proud of yourself"



###
# Function: plural
# Purpose:  Gets the plural ending for a word
# Input:    num - the number of things we're pluralizing
# Returns:  The word ending, directly depending on what num is
###
def plural(num):
    if(num==1):
        return ""
    else:
        return "s"
