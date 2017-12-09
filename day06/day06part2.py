# Advent of Code 2017
# Day 6, Part 2
# @geekygirlsarah

# Files to run through
# input.txt being the input the puzzle provides
inputFile = "input.txt"
# inputFile = "testinput.txt"

# Variables
numbers = []
old_combos = dict()
length = 0
num_steps = 0

# To make checking lists a lot simpler
def listToString(the_list):
    return " ".join(str(elem) for elem in the_list)

# Process file
with open(inputFile) as f:
    while True:
        contents = f.readline(-1)
        if not contents:
            # print "End of file"
            break
        # print ("Contents: ", contents)

        numbers = contents.split()
        numbers = map(int, numbers)

length = len(numbers)

print("length: " + str(length))
print("list: ")
print(numbers)

while True:
    num_steps += 1
    print("Step: " + str(num_steps))

    # add combo to tracking list
    old_combos[listToString(numbers)] = num_steps

    # Find largest position
    max_num = max(numbers)
    position = numbers.index(max_num)
    print("   Found max number: " + str(max_num))
    print("   Found at index: " + str(position))

    # Redistribute blocks
    numbers[position] = 0
    print("   Before redistribution: ")
    print(numbers)
    for i in range (0, max_num):
        # increment position
        position = (position + 1) % length
        # Add one to the position's number
        numbers[position] += 1
    print("   After redistribution: ")
    print(numbers)

    # See if this combo exists
    string = listToString(numbers)
    if string in old_combos:
        print("\n\nNumber of steps: " + str(num_steps))
        step_found = num_steps - old_combos[string] + 1
        print("\nStep found at: " + str(step_found))
        break
