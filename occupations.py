import random

occL = open("occupations.csv").readLine();
occDict = {}
upperBoundL = []
currentUpperBound = 0

for line in occL:
    occS = line.split(",")[0]
    currentUpperBound += int(line.split(","))[1]
    occDict[currentUpperBound] = occS
    upperBoundL.add(currentUpperBound)

def pickOccupation():
    randNum = random.random()*100
    for num in upperBoundL:
        if randNum < num:
              break;
    return occDict[thisUpperBound]

