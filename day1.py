dial = 50
pw = 0

# Part 1
# Count how many times the dial ends at 0
with open("Input/test.txt") as f:
    for line in f:
        if line[0] == "L":
            dial -= int(line[1:])
            dial = dial % 100
        if line[0] == "R":
            dial += int(line[1:])
            dial = dial % 100
        if dial == 0:
            pw += 1
print(pw)

# Part 2
# Count how many times the dial passes 0
dial = 50
pw = 0

with open("Input/1.txt") as f:
    for line in f:
        if line[0] == "L":
            for i in range(int(line[1:])):
                dial -= 1
                if dial == 0:
                    pw += 1
                if dial == -1:
                    dial = 99
        if line[0] == "R":
            for i in range(int(line[1:])):
                dial += 1
                if dial == 100:
                    pw += 1
                    dial = 0
print(pw)
