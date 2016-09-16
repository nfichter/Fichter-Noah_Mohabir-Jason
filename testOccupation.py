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
    randNum = random.random()*99.8
    passenger = 0 # Will "travel" / iterate through the dictionary
    for occKey in occDict:
        passenger += occDict[occKey]
        if randNum < passenger:
            return occKey

buckets = {} #new dictionary that stores the number of times each occupation is picked
          
def test():
  for line in occS: #creates each bucket, initializes each value to 0
    comma = line.rfind(',')
    occKey = line[:comma].strip('"')
    buckets[occKey] = 0
    
  for num in range(10000): #runs 10000 times, picks one occupation and adds one to that bucket
    chosenOne = pickOccupation()
    print chosenOne
    buckets[chosenOne] += 1

  for key in occDict: #prints the key and its corresponding percentage (10000/100 = 100, so that will give percentage)
    print key,buckets[key]/100.0

test()
