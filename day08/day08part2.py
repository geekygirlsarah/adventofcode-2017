# Advent of Code 2017
# Day 8, Part 2
# @geekygirlsarah

from pprint import pprint

# Files to run through
# input.txt being the input the puzzle provides
inputFile = "input.txt"
# inputFile = "testinput.txt"

# Variables
all_registers = dict()
highest_value_ever = 0

# Process file
with open(inputFile) as f:
    while True:
        contents = f.readline(-1)
        if not contents:
            # print "End of file"
            break
        # print ("Contents: ", contents)

        # Parse it out
        command = contents.split()
        register = command[0]
        operand = command[1]
        operand_amount = int(command[2])
        conditional_register = command[4]
        conditional_operand = command[5]
        conditional_value = int(command[6])

        # Figure out conditional
        value = 0
        if conditional_register in all_registers:
            value = all_registers[conditional_register]

        perform_action = False
        if conditional_operand == "<":
            if value < conditional_value:
                perform_action = True
        elif conditional_operand == "<=":
            if value <= conditional_value:
                perform_action = True
        elif conditional_operand == ">":
            if value > conditional_value:
                perform_action = True
        elif conditional_operand == ">=":
            if value >= conditional_value:
                perform_action = True
        elif conditional_operand == "==":
            if value == conditional_value:
                perform_action = True
        elif conditional_operand == "!=":
            if value != conditional_value:
                perform_action = True

        # Do calculations
        if perform_action:
            if operand == "inc":
                if register in all_registers:
                    all_registers[register] += operand_amount
                else:
                    all_registers[register] = operand_amount
            else:
                if register in all_registers:
                    all_registers[register] -= operand_amount
                else:
                    all_registers[register] = -operand_amount

        max_value = max(all_registers.values())
        highest_value_ever = max([highest_value_ever, max_value])

pprint(all_registers)

print("The maximum value is: " + str(max(all_registers.values())))
print("The highest value ever is: " + str(highest_value_ever))
