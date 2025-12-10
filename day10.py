import scipy as sp

lights = []
instructions = []
joltage = []

with open("Input/test.txt") as f:
    for line in f:
        lsplit = line.split()
        lights.append(lsplit[0])
        instruc = []
        for k in range(len(lsplit)-2):
            instruc.append(lsplit[k+1])
        instructions.append(instruc)
        joltage.append(lsplit[-1])

num_lights = []
for i in lights:
    a = []
    for j in i:
        a.append(1) if j == "#" else a.append(0)
    num_lights.append(a[1:-1])
print(num_lights)

# Graph theory bs i cant be bothered to learn rn