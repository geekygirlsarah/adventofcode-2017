# Advent of Code 2017
# Day 3, Part 2
# @geekygirlsarah

from math import sqrt, ceil

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

        # Create initial lists that algorithm can use
        #    17 16 15 14 13
        #    18  5  4  3 12
        #    19  6  1  2 11\
        #    20  7  8  9 10
        #    21 22 23 24 25
        #

        list1 = [1]
        list2 = [1, 2, 4, 5, 10, 11, 23, 25]  # these are sums
        current = 10  # number to start at

        # Calculate the 4 corner values

        lengthOfSide = int(ceil(sqrt(numberInput)))
        if lengthOfSide % 2 == 0:
            lengthOfSide += 1



        # Go through each side and calculate it
        # Check also if a summed number exceeds the input number

        while (True):
            loop1counter = 0
            loop2counter = 0
            loop1 = loop2
            loop2 = range(current, current + (lengthOfSide * 4))

            # Side 1:





        # The "length" of this number's ring
        # lengthOfSide = int(ceil(sqrt(numberInput)))
        # if lengthOfSide % 2 == 0:
        #     lengthOfSide += 1
        #
        # # Maximum number in each ring
        # highestNumberOnSide = lengthOfSide * lengthOfSide
        # # Offset used for calculating midpoints of each side
        # offset = int((lengthOfSide - 1) / 2)


