import re
invalid_add_p1 = invalid_add_p2 = 0
pattern = r"(.+)\1"
with open("Input/2.txt") as f:
    for lower, upper in [i.split("-") for i in f.readline().split(",")]:
        for test_id in range(int(lower), int(upper) + 1):
            if bool(re.fullmatch(pattern, str(test_id))):
                invalid_add_p1 += test_id
            if bool(re.fullmatch(pattern+"+", str(test_id))):
                invalid_add_p2 += test_id
print(f"Solution part 1: {invalid_add_p1}, Solution part 2: {invalid_add_p2}")