# Advent of Code 2017
# Day 1, Part 2
# @geekygirlsarah

# Files to run through
# input.txt being the input the puzzle provides
inputFile = "input.txt"
# inputFile = "testinput.txt"

# Process file
with open(inputFile) as f:
    contents = f.readline(-1)
    if not contents:
        print("End of file")
        quit()
    # print("Contents: ", contents)

    length = len(contents)
    half_length = int(length / 2)
    # Double it. This lets me traverse it in a circular way without the math. (Could do mod but... eh, it's late)
    contents += contents

    # print("Contents: ", contents)

    total = 0
    for i in range(0, length):
        char = contents[i]
        next_pos = i + half_length
        half_char = contents[next_pos]
        print(char)
        if char == half_char:
            print("Matched: " + char)
            total += int(char)
            print("New total: " + str(total))

print("Final total: " + str(total))
