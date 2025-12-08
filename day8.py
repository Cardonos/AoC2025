import numpy as np

junction_boxes = np.array([])
with open("Input/8.txt") as f:
    for line in f:
        x,y,z = line.split(",")
        if len(junction_boxes)==0:
            # x, y, z, circuit_id
            junction_boxes = [int(x),int(y),int(z),None]
        else:
            junction_boxes = np.vstack((junction_boxes,[int(x),int(y),int(z),None]))

# Generate list of all distances
distances_list = np.array([0,0,0])
for i in range(len(junction_boxes)):
    print(i)
    for j in range(i, len(junction_boxes)):
        if i!=j:
            distance = (junction_boxes[i][0]-junction_boxes[j][0])**2 + (junction_boxes[i][1]-junction_boxes[j][1])**2 + (junction_boxes[i][2]-junction_boxes[j][2])**2
            distances_list = np.vstack((distances_list,[distance,i,j]))

# Sort the list of distances by smallest first to form connections
ind = np.argsort( distances_list[:,0])
distances_list = distances_list[ind][1:]
print(distances_list)

circ_count = 0
for connection in range(1000):
    node1 = distances_list[connection][1]
    node2 = distances_list[connection][2]
    if junction_boxes[node1][3] is None and junction_boxes[node2][3] is None:
        junction_boxes[node1][3] = junction_boxes[node2][3] = circ_count
        circ_count += 1
    elif junction_boxes[node1][3] is None and junction_boxes[node2][3] is not None:
        junction_boxes[node1][3] = junction_boxes[node2][3]
    elif junction_boxes[node1][3] is not None and junction_boxes[node2][3] is None:
        junction_boxes[node2][3] = junction_boxes[node1][3]
    else:
        np.putmask(junction_boxes[:,3],junction_boxes[:,3] == junction_boxes[node2][3],junction_boxes[node1][3])
print(junction_boxes)
np.putmask(junction_boxes[:, 3], junction_boxes[:, 3] == None, 10000)
circ, count = np.unique(junction_boxes[:,3], return_counts=True)
circuits = dict(zip(circ,count))
circuits.pop(10000)
circ_lengths = list(circuits.values())
circsum = 1
for m in range(3):
    maxx = max(circ_lengths)
    circsum *= maxx
    circ_lengths.pop(circ_lengths.index(maxx))
print(circsum)