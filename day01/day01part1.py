# Advent of Code 2017
# Day 1, Part 1
# @geekygirlsarah

# Files to run through
# input.txt being the input the puzzle provides
inputFile = "input.txt"
# inputFile = "testinput.txt"

# Process file
with open(inputFile) as f:
    # Read the line
    contents = f.readline(-1)
    if not contents:
        print("End of file")
        quit()
    # print("Contents: ", contents)
    # print("first char: ", contents[0])

    # Add first char to end to ensure last char has something to match
    contents += contents[0]

    # print("Contents: ", contents)

    last_char = ''
    total = 0

    # Could be simplified by just comparing contents[i] and contents[i-1] but... it's late...
    for char in contents:
        print(char)
        if last_char is '':
            last_char = char
            continue
        if char == last_char:
            print("Matched: " + char)
            total += int(char)
            print("New total: " + str(total))

        last_char = char

print("Final total: " + str(total))
