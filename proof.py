import testOccupation

occL = open('occupations.csv').read()
occS = occL.split('\n')[1:-1]
occDict = {}

for line in occS:
  comma = line.rfind(',')
  occKey = line[:comma].strip('"')
  occDict[occKey] = 0

del occDict['Total']

for num in range(10000):
    occDict[testOccupation.pickOccupation()] += 1

for key in occDict:
    print key,occDict[key]/100
