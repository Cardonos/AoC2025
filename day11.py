from functools import cache, reduce
from itertools import permutations

# Part 1
serverdict = {}
# Build a dictionary where every server has its connections listed
with open("Input/11.txt") as f:
    for line in f:
        servers = line.split()
        serverdict[servers[0][:-1]] = [servers[1]]
        for server in servers[2:]:
            serverdict[servers[0][:-1]].append(server)

# recursively step through all connections until an "out" is reached
@cache
def next_server(key, target):
    # This check is only needed for part 2
    if key == "out" and target != "out":
        return 0
    elif key == target:
        return 1
    return sum(next_server(keys, target) for keys in serverdict[key])

# Iterate through all connections of "you"
output = 0
for keys in serverdict["you"]:
    output += next_server(keys, "out")
print(f"There are {output} paths from you to the output server")

# Part 2
# Iterate through all connection pairs svr-fft fft-dac dac-out (and fft/dac switched)
# multiply them together for total path count
sum_ = 0
paths = [["svr", "fft", "dac", "out"], ["svr", "dac", "fft", "out"]]
for p in paths:
    ans = 1
    for k in range(len(p)-1):
        ans *= next_server(p[k], p[k+1])
    sum_ += ans
print(f"There are {sum_} paths from svr to the output server that pass fft and dac")
