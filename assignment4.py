##################
#  Assignment 4  #
##################
#    Abe Fehr    #
#   100908743    #
##################

#
# This is the simulation of an ant colony
#

import random

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

class Colony(object):    
    def __init__(self):
        self.ants = []
        self.food = 10

    def breedWorker(self):
        if(self.food >= 5):
            self.food -= 5
            baby = Ant()
            print "A bouncing baby %s was born, %s name was %s!" % (("boy" if (baby.gender=="m") else "girl"), baby.possessivepronoun(False), baby.name)
            self.ants.append(baby)
        else:
            print "There is not enough food for an ant"

    def step(self):
        for ant in self.ants:
            self.food += ant.forage()
            if(self.food > 0):
                self.food -= 1
            else:
                ant.health -= 1
                if(ant.health == 0):
                    print ant.name + " has died of starvation!"
        
    def purge(self):
        temp = []
        for ant in self.ants:
            if(ant.health > 0):
                temp.append(ant)
            else:
                self.food += 1
        self.ants = temp
    
class Ant(object):
    global names
    
    def __init__(self):
        self.health = 10
        i = random.randint(0, len(names)-1)
        self.name = names[i][0]
        self.gender = names[i][1]

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
        
    def possessivepronoun(self, capitalized):
        if(self.gender == "m"):
            return "His" if capitalized else "his"
        else:
            return "Her" if capitalized else "her"

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

def plural(num):
    if(num==1):
        return ""
    else:
        return "s"
