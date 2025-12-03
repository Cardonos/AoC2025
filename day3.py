total_jolts = 0

# Part 1: exactly two batteries to form the biggest number
with open("Input/3.txt") as f:
    for line in f:
        first_digit = 0
        second_digit = 0
        # Parse line into list of numbers
        line = list(map(int, list(line)[:-1]))
        max_pos = line.index(max(line))
        # Check whether the largest number is at the end of the string
        if max_pos == len(line)-1:
            # If it is, then it is the second digit, and the second largest number is the first
            first_digit = max(line[:max_pos])
            second_digit = line[max_pos]
        else:
            # otherwise it is the first digit and the second one is the largest one behind
            first_digit = line[max_pos]
            second_digit = max(line[max_pos+1:])

        total_jolts += int(str(first_digit) + str(second_digit))
print(f"Total jolt max from two batteries: {total_jolts}")

# Part 2: exactly 12 batteries to form the biggest number
total_jolts_2 = 0

with open("Input/3.txt") as f:
    for line in f:
        joltage_bank = ""
        # Parse line into list of numbers
        line = list(map(int, list(line)[:-1]))
        # left cutoff point
        start_id = 0
        # Collect 12 numbers out of the list
        for i in range(12):
            # Drop the last 11-i numbers so there will always be enough to "fill up" at the end
            # then look for the biggest number between the left and right cutoff points
            if i < 11:
                next_num = max(line[start_id:-(11-i)])
            else:
                next_num = max(line[start_id:])
            # set the new left cutoff point to be behind the just chosen largest number
            # so bigger numbers before it will be ignored
            start_id += line[start_id:].index(next_num)+1
            # concatenate the number for the output
            joltage_bank += str(next_num)
        # sum up the bank joltages
        total_jolts_2 += int(joltage_bank)

print(total_jolts_2)