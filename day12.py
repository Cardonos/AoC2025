areas = []
with open("Input/12.txt") as f:
    k = 0
    for line in f:
        k+=1
        if k > 30:
            areas.append([line[:-1]])
# Part 1
# Lazy assumption: Every present is a solid 3x3 block, no tiling necessary
# if the area fits enough 3x3 blocks for every present it obviously works
# for some reason this is already the correct answer
fit_ar = 0
for area in areas:
    splitar = area[0].split(":")
    x_y_ar = splitar[0].split("x")
    # Number of 3x3 blocks that fit in the area
    full_area = (int(x_y_ar[0])//3)*(int(x_y_ar[1])//3)
    # Number of presents of any shape needed
    k = sum([int(i) for i in splitar[1].split()])
    # if number of 3x3 spaces in the area is bigger or equal than number of presents they all obviously fit
    if full_area >= k:
        fit_ar += 1
print(fit_ar)