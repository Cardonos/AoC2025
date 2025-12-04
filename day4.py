from itertools import product
import numpy as np

# Part 1

# Parse input to numpy array
grid = np.array([])
with open("Input/4.txt") as f:
    for line in f:
        new_line = [i for i in line[:-1]]
        if not np.size(grid) > 0:
            grid = new_line
        else:
            grid = np.vstack((grid, new_line))

# Function that checks an ajacent field to see whether it contains a paper roll
def check_adj(grid_,x,y):
    if grid_[x][y] == "@" and x >= 0 and y >= 0:
        return 1
    else:
        return 0

def check_and_remove(warehouse_grid, indices):
    accessible = 0
    sidelength = np.size(warehouse_grid, axis=0)
    # Second grid with removal of the rolls, for visualization and Part 2
    testgrid = np.full(np.shape(warehouse_grid), ".")
    #iterating over every entry
    for h in range(sidelength):
        for v in range(sidelength):
            if warehouse_grid[h][v] == "@":
                counter = 0
                # iterating over all combinations of [1,-1,0]
                for x,y in indices:
                    # Evil if-else
                    try:
                        counter += check_adj(warehouse_grid, h+x, v+y)
                    except:
                        pass
                # check if the roll is accessible. Because [0][0] is also checked the comparison value is <= 4
                if counter <= 4:
                    accessible += 1
                    testgrid[h, v] = "."
                else:
                    testgrid[h, v] = "@"
    return accessible, testgrid

# indices for iterating over all 8 adjacent units
indices_check = list(product([-1,0,1],[-1,0,1]))

output, grid = check_and_remove(grid, indices_check)
print(f"Rolls removed in step 1: {output}")

# Part 2: remove the accessible rolls until no more can be removed
curr_removed = 1
while curr_removed > 0:
    curr_removed, grid = check_and_remove(grid,indices_check)
    output += curr_removed
print(f"rolls removed in total: {output}")
