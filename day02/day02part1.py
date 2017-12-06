# Advent of Code 2017
# Day 2, Part 1
# @geekygirlsarah

# Files to run through
# input.txt being the input the puzzle provides
inputFile = "input.txt"
# inputFile = "testinput.txt"

# Variables
checksum = 0

# Process file
with open(inputFile) as f:
    while True:
        contents = f.readline(-1)
        if not contents:
            # print "End of file"
            break
        # print ("Contents: ", contents)

        # Split
        row_numbers = list(map(int, contents.split("\t")))
        print("Row: " + str(row_numbers))
        max_num = max(row_numbers)
        min_num = min(row_numbers)
        checksum += max_num - min_num

        print("Min: " + str(min_num))
        print("Max: " + str(max_num) + "\n")

print("Final checksum: " + str(checksum))
