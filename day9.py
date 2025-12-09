import itertools as it
import shapely as sp

x_point = []
y_point = []
with open("Input/9.txt") as f:
    for line in f:
        coords = line.split(",")
        x_point.append(int(coords[0]))
        y_point.append(int(coords[1][:-1]))
cornerpoints = list(zip(y_point, x_point))

# Part 1: get combinations of cornerpoints, calculate their area and output the maximum value
max_ar = 0
for (a,b),(x,y) in it.combinations(cornerpoints, 2):
    area = (abs(x - a)+1) * (abs(y - b)+1)
    if area > max_ar:
        max_ar = area
print(max_ar)

# Part 2: use a polygon library that for some reason cannot properly calculate the area
# so the area it outputs is wrong in absolute terms but right in relative terms, can be used for comparison
poly = sp.Polygon(cornerpoints)
max_ar = 0
for (a,b),(x,y) in it.combinations(cornerpoints, 2):
    coors = ((a,b),(a,y),(x,y),(x,b))
    check_poly = sp.Polygon(coors)
    area = check_poly.area
    if area > max_ar and sp.contains(poly, check_poly):
        max_ar = area
        out_area = (abs(x - a)+1) * (abs(y - b)+1)
print(out_area)