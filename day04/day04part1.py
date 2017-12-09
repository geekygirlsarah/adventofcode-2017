# Advent of Code 2017
# Day 4, Part 1
# @geekygirlsarah

# Files to run through
# input.txt being the input the puzzle provides
inputFile = "input.txt"
# inputFile = "testinput.txt"

# Variables
num_valid = 0

# Process file
with open(inputFile) as f:
    while True:
        contents = f.readline(-1)
        if not contents:
            # print "End of file"
            break
        # print ("Contents: ", contents)

        words = contents.split()
        word_list = []
        is_not_valid = False
        for word in words:
            if word in word_list:
                is_not_valid = True
                break
            else:
                word_list.append(word)
        if not is_not_valid:
            num_valid += 1

print("Number of valid passwords: " + str(num_valid))