# Advent of Code 2017
# Day 3, Part 1
# @geekygirlsarah

from math import sqrt, ceil

# Files to run through
# input.txt being the input the puzzle provides

inputFile = "input.txt"
# inputFile = "testinput.txt"

# Variables

# Process file
with open(inputFile) as f:
    while True:
        numberInput = f.readline(-1)
        if not numberInput:
            # print "End of file"
            break
        numberInput = int(numberInput)
        print ("Input: " + str(numberInput))

        # Calculations

        # The "length" of each ring
        lengthOfSide = int(ceil(sqrt(numberInput)))
        if lengthOfSide % 2 == 0:
            lengthOfSide += 1

        # Maximum number in each ring
        highestNumberOnSide = lengthOfSide * lengthOfSide
        # Offset used for calculating midpoints of each side
        offset = int((lengthOfSide - 1) / 2)

        # Find each midpoint on each side
        midpoints = []
        for i in range(0, 4):
            midpoints.append(highestNumberOnSide - (offset + (i * lengthOfSide - i)))

        stepsFromRingToCenter = (lengthOfSide - 1) / 2

        for i in range(0, 4):
            midpoints[i] = stepsFromRingToCenter + abs(numberInput - midpoints[i])

        finalDistance = min(midpoints)

        print("   Final distance: " + str(finalDistance))
