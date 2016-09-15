# Team Lust for Life - Noah Fichter and Jason Mohabir
# SoftDev pd8
# HW01 -- Divine your Destiny
# 2016-09-15

import random

occL = open('occupations.csv').read()
occS = occL.split('\n')[1:-1] # Split csv into row
occDict = {}

for line in occS:
  comma = line.rfind(',') # Find comma in row
  occKey = line[:comma].strip('"') # Split row at comma
  occValue = float(line[comma + 1:])
  occDict[occKey] = occValue # Set key and value

del occDict['Total'] # You can probably remove this in an elegant way, but (shrug)


def pickOccupation():
    randNum = random.random()*100
    passenger = 0 # Will "travel" / iterate through the dictionary
    for occKey in occDict:
        passenger += occDict[occKey]
        if randNum < passenger:
            return occKey
        
print pickOccupation()
