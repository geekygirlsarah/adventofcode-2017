# Advent of Code 2017
# Day 2, Part 2
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

        # Find evenly divisible numbers
        # I'm assuming there's always at least two numbers in here. Because... well,
        # you have to have two numbers to divide...
        for i in range(0, len(row_numbers)):
            for j in range(i, len(row_numbers)):
                if i == j:
                    continue

                num1 = row_numbers[i]
                num2 = row_numbers[j]
                mod1 = num1 % num2
                mod2 = num2 % num1
                if num1 > num2 and num1 % num2 == 0:
                    checksum += int(num1 / num2)
                    print("Num1: " + str(num1))
                    print("Num2: " + str(num2))
                    print("Checksum: " + str(checksum))
                    i = len(row_numbers)
                    j = len(row_numbers)
                    break
                if num2 > num1 and num2 % num1 == 0:
                    checksum += int(num2 / num1)
                    print("Num1: " + str(num1))
                    print("Num2: " + str(num2))
                    print("Checksum: " + str(checksum))
                    i = len(row_numbers)
                    j = len(row_numbers)
                    break

print("Final checksum: " + str(checksum))
