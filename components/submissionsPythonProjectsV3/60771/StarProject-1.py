import sys
import pandas
import math
from intro import *
from first import *
from second import *
from third import *
from search import *
#open some really cool csv files
constellations = pandas.read_csv("constellations.csv")
stars = pandas.read_csv("stars.csv")
eight = pandas.read_csv("eight.csv")

"""
####FILES####
'csv' is the star chart csv file
'constellations' is the constellation csv file
'aspect' is a .txt explaining the characteristics of stars
'eight' is a csv file of all 88 constellations
####FUNCTIONS####
'introduction' is the welcoming print statement and menu
'menu' is the menu that directs to info options
'secondmenu' is the menu without introduction
'sun' sets the values that are used to compare stars to our sun
'conta' provides a list of the constellations within the catalog, as well their meaning
'relay' provides a list of stars within a constellation in the catalog
'readAspect' open and read aspect.txt; also turns each element into a list
'getAspect' prints the description when a characteristic is chosen
'listCharacteristics' provides a list of all the star characteristics
'starSearch' provides all of the information on every star in a given constellation
'findaStar' allows user to find names of stars based on user set parameters
'staro' prints the information from findaStar() for columns that are integers or floats
'staraStr' prints the information from findaStar() for columns that are strings

### WRITE DOWN WHICH MODULES/FUNCTIONS EACH FUNCTION DEPENDS ON ###
"""

#how to call a function
#def function(Argument):
    #var = 10 * Argument
    #return var
#newVariable = function(Variable)
#newVariable will be equal to var, which is 10 times the original amount

###To do list###
#matplotlib make mainsequence graph OR graph of stars' measurable traits
    #traits color and size could be plotted for mainsequence graph (so two different types of graphs)
#make menu simpler (what did I mean by this)
#modulate functions AND MAKE THE CODE WORK #THIS IS DONE (mostly)
#function that gives extremest star for each category (hottest, farthest)
#function that allows user to ask for star name
#function that compares stars to the sun

#add these next:
#function that combines parameters
    #pandas .query()
#Different graphs for all traits if i have time
    #Hertzsprung graph can be made using y=Luminosity and x=Temperature
#modules: from [learn_stars] import *
#when plotting graphs, have the sun as a reference
#dictionary user inputs
#from learn_stars import *
#import learn_stars
#learn_stars.your_function_name
#do not use __init__.py (i am going to use this)

#CURRENT ERRORS
#size does not work in characteristics (its description is missing) FIXED
#in first option(constellations): if contaExit == "1": no longer gives list of stars FIXED
#typo message occurs after "no" in last choice for first option FIXED(kinda)
#ModuleNotFound (all of them)
#Function error (conta, relay, findaStar; probably more) fixed mostly


#index syntax: [row_selection(yTop:yBottom), column_selection(xLeft,xRight)]


def similarStar():
    print()

#sets conditions for stars to be compared to the sun    
def sunlike(radius, mass, luminosity, sClass, age, absMag):
    solRadius = 1
    solMass = 1
    solLuminosity = 1
    solClass = "G2 V"
    solAge = 4600
    solMag = 4.83

#all i need are these last few functions lol lets go
        #remember you're working in starpractice.py

    
# gotta study for CHEM man, look at the quiz keys brO
        
#########################################################
########## CODING AREA BELOW IM SUCH A CODER ############
#########################################################
    
#if __name__ == "__menu__":
#sunlike(radius, mass, luminosity, sClass, age, absMag)
menu()
