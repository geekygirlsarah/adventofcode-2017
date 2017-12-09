# Advent of Code 2017
# Day 6, Part 1
# @geekygirlsarah

# Files to run through
# input.txt being the input the puzzle provides
inputFile = "input.txt"
# inputFile = "testinput.txt"

# Variables
numbers = []
old_combos = []
length = 0
num_steps = 0

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
    old_combos.append(listToString(numbers))

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
    if listToString(numbers) in old_combos:
        break

print("\n\nNumber of steps: " + str(num_steps))

