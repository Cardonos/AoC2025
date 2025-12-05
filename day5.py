
# Parse Input into two lists
with open("Input/5.txt") as f:
    input = f.read().split("\n")[:-1]
    # list of ranges
    ranges_ = input[:input.index("")]
    # list of ingredients
    ingredients = list(map(int,input[input.index("")+1:]))
    ranges=[]
    # split ranges into upper and lower bound
    for i in ranges_:
        ranges.append(list(map(int,i.split("-"))))

# Part 1
count = 0
# Iterate over every ingredient
for ingredient in ingredients:
    spoiled = True
    k = 0
    # iterate over all ranges and see if it has not yet been found to be within one of the ranges
    while spoiled and k < len(ranges):
        # check if ingredient is between the upper and lower bounds
        if ranges[k][0] <= ingredient <= ranges[k][1]:
            spoiled = False
            count += 1
        k += 1

print(f"The number of fresh ingredients is {count}")

# Part 2
# Iterate through the ranges, elimitate overlapping ranges by extending or removing ranges
def remove_overlap(id_ranges_, index):
    k = index+1
    lower = id_ranges_[index][0]
    upper = id_ranges_[index][1]
    id_ranges = id_ranges_[:]
    # Changed 0: no change, Changed 1: Change, Changed 2: Change and original entry must be removed
    changed = 0
    while k < len(id_ranges):
        compare_lower = id_ranges[k][0]
        compare_upper = id_ranges[k][1]
        # Horrible comparison chain
        if lower <= compare_lower and upper >= compare_upper:
            # compared entry is fully included in current entry -> remove entry
            id_ranges.pop(k)
            changed = 1
            break
        elif lower > compare_lower and upper < compare_upper:
            # compared entry fully includes current entry -> remove current entry
            changed = 2
            break
        # Next two comparisons check whether the ranges can be merged/extended, removes both entries
        # and appends a new extended entry
        elif lower <= compare_lower <= upper <= compare_upper:
            id_ranges.pop(k)
            id_ranges.append([lower, compare_upper])
            changed = 2
            break
        elif compare_lower <= lower <= compare_upper <= upper:
            id_ranges.pop(k)
            id_ranges.append([compare_lower, upper])
            changed = 2
            break
        k+=1
    return id_ranges, changed

# As long as changes have been made: loop over the ranges and compare if it can be extended or removed
# Should not be necessary with sorted ranges, but it apparently is?
changes = True
ranges = sorted(ranges)
while changes:
    m = 0
    changes = False
    while m < len(ranges):
        ranges, chan = remove_overlap(ranges, m)
        if chan == 1:
            changes = True
        if chan == 2:
            changes = True
            ranges.pop(m)
            m -= 1
        m+=1

# Add up the difference for  each range to get the total sum of ranges
out = 0
for a,b in ranges:
    out += b-a+1
print(f"The total valid ID range is {out}")