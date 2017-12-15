# Advent of Code 2017
# Day 2, Part 1
# @geekygirlsarah

from math import sqrt

# Files to run through
# input.txt being the input the puzzle provides

# inputFile = "input.txt"
inputFile = "testinput.txt"

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

        # Get the closest maximum square without going over
        # This is the "row" of the spiral the number is after
        square = int(sqrt(numberInput))
        print ("Square (row): " + str(square))

        # This is how many steps around the spiral this number is
        squareDifference = int((square + 2) ** 2) - (square ** 2)  # + 1
        squareDistance = int(numberInput - square ** 2)
        print ("Num numbers in spiral: " + str(squareDifference))
        print ("Position in spiral: " + str(squareDistance))

        # Number of steps per side
        stepsPerSide = squareDifference / 4 - 1
        stepsPerHalfSide = stepsPerSide / 2
        startSteps = square ** 2

        print ("Steps per side: " + str(stepsPerSide))
        print ("Steps per half side: " + str(stepsPerHalfSide))
        print ("Start of steps: " + str(startSteps))

        # Find which side it's on
        corner = 0
        if input < startSteps + stepsPerSide:
            corner = 1
        elif input < startSteps + stepsPerSide * 2:
            corner = 2
        elif input < startSteps + stepsPerSide * 3:
            corner = 3

        sidePosition = (numberInput - (startSteps + (stepsPerSide * corner))) / 2
        # if corner = 0 and ...
        if sidePosition > stepsPerHalfSide:
            sideDistance = sidePosition - stepsPerHalfSide
        else:
            sideDistance = stepsPerHalfSide - sidePosition

        distance = sideDistance + ((square / 2) + 1)

        print("   Final distance: " + str(distance))
        print("\n\n")
