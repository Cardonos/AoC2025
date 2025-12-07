splitcount = 0
beam_index = set()
beam_paths_dict = {}

with open("Input/7.txt") as f:
    for line in f:
        new_line = [i for i in line[:-1]]
        # First line: add the beam origin as the current beam location to the set and as the path origin to the dict
        if len(beam_index) == 0:
            beam_index.add(new_line.index("S"))
            beam_paths_dict[new_line.index("S")] = 1
        # iterate over every character in the line to check whether it is a splitter
        for i in range(len(new_line)):
            # Part 1:
            # if the character is a splitter and there is a beam above it (index is in beam index) then
            # remove it from the beam index and add the left and right indices to the beam index, increment splitcount
            # this generates the proper beam state for the next row
            #
            # Part 2:
            # The beam index in the path dict at a location represents how many paths can make the beam end up
            # in that location. When beams "merge" (aka the same index gets changed by multiple splitters) the indices
            # add up.Summing up the values of the dictionary represents the total unique paths through the grid
            if new_line[i] == "^" and i in beam_index:
                # Part 1
                beam_index.remove(i)
                beam_index.add(i-1)
                beam_index.add(i+1)
                splitcount += 1

                # Part 2
                if i+1 in beam_paths_dict.keys():
                    beam_paths_dict[i + 1] += beam_paths_dict[i]
                else:
                    beam_paths_dict[i + 1] = beam_paths_dict[i]
                if i-1 in beam_paths_dict.keys():
                    beam_paths_dict[i - 1] += beam_paths_dict[i]
                else:
                    beam_paths_dict[i - 1] = beam_paths_dict[i]
                beam_paths_dict[i] = 0

print(f"The beam was split {splitcount} times")
print(f"The total number of unique paths is {sum(beam_paths_dict.values())}")
