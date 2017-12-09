# Advent of Code 2017
# Day 5, Part 1
# @geekygirlsarah

# Files to run through
# input.txt being the input the puzzle provides
inputFile = "input.txt"
# inputFile = "testinput.txt"

# Variables
numbers = []
max_length = 0
pointer = 0
steps = 0

# Process file
with open(inputFile) as f:
    while True:
        contents = f.readline(-1)
        if not contents:
            # print "End of file"
            break
        # print ("Contents: ", contents)

        numbers.append(int(contents))

# Main processing loops
max_length = len(numbers)
while True:
    steps += 1
    print("Step #" + str(steps))
    current_number = numbers[pointer]
    print("   Current number: " + str(current_number))
    # check if it goes outside the loop
    if pointer + current_number >= max_length:
        print("   Outside list!")
        break

    # increment current step
    numbers[pointer] += 1
    print("   New number: " + str(numbers[pointer]))
    # Move pointer
    pointer += current_number
    print("   Pointer now at: " + str(pointer))


print("Number of steps: " + str(steps))
