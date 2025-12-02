import re
invalid_add_p1 = 0
invalid_add_p2 = 0

# regex matching pattern for one additional occurrence of a substring
pattern_part1 = r"(.+)\1"
# one or more occurrences
pattern_part2 = r"(.+)\1+"


with open("Input/2.txt") as f:
    # split into id ranges
    line = f.readline()
    line = line.split(",")
    for ids_ in line:
        ids = ids_.split("-")

        # iterate through the IDs and check if any of them contain repeating substrings
        for id in range(int(ids[0]),int(ids[1])+1):

            repeat = bool(re.fullmatch(pattern_part1, str(id)))
            if repeat:
                invalid_add_p1 += id

            repeat_p2 = bool(re.fullmatch(pattern_part2, str(id)))
            if repeat_p2:
                invalid_add_p2 += id


print(f"Solution part 1: {invalid_add_p1}")

print(f"Solution part 2: {invalid_add_p2}")
