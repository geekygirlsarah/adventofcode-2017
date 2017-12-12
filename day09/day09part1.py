# Advent of Code 2017
# Day 9, Part 1
# @geekygirlsarah

# Files to run through
# input.txt being the input the puzzle provides
inputFile = "input.txt"
# inputFile = "testinput.txt"


# Process file
with open(inputFile) as f:
    while True:
        contents = f.readline(-1)
        if not contents:
            # print "End of file"
            break
        # print ("Contents: ", contents)

        state = "start"
        group_level = 0
        group_sum = 0
        char_pos = -1

        while True:
            # increment char
            char_pos += 1
            if state == "end" or char_pos >= len(contents):
                break

            char = contents[char_pos]

            # Starting state
            if state == "start" and char == "{":
                group_level += 1
                state = "in group"
                continue
            if state == "in group" and char == "{":
                group_level += 1
                continue
            if state == "in group" and char == "}":
                group_sum += group_level
                group_level -= 1
                if group_level == 0:
                    state = "end"
                continue
            if state == "in group" and char == "<":
                state = "garbage"
                continue
            if state == "garbage" and char == ">":
                state = "in group"
                continue
            if state == "garbage" and char == "!":
                char_pos += 1
                continue
            if state == "garbage" and char == ">":
                state = "in group"
                continue
        print("Sum: " + str(group_sum))

