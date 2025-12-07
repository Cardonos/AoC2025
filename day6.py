import numpy as np
import re

problem_array = []

with open("Input/6.txt") as f:
    for line in f:
        if len(problem_array) > 0:
            problem_array = np.vstack((problem_array,line.split()))
        else: problem_array = line.split()
# Part 1
out_sum = 0
array_shape = np.shape(problem_array)
for problem in range(array_shape[1]):
    operator = problem_array[-1][problem]
    equation = ""
    for number in range(array_shape[0]-1):
        equation += str(problem_array[number][problem]) + operator
    out_sum += eval(equation[:-1])
print(f"the sum is {out_sum}")

# Part 2
# Parsing needs to change, spaces/alignment is relevant now
# Build array including every whitespace character

problem_array_2 = []

with open("Input/6.txt") as f:
    for line in f:
        new_line = []
        for character in line[:-1].ljust(3771, " "):
            new_line.append(character)
        if len(problem_array_2) > 0:
            problem_array_2 = np.vstack((problem_array_2, new_line))
        else:
            problem_array_2 = new_line
""" 
Iterate over the bottom row until it is not empty (operator) which signifies the start of a problem block
from there build up a string of numbers top to bottom, move one index right and repeat until an empty string is returned
evaluate the built equation and sum up the solutions

awful but it works
"""
def build_and_eval(prob_arr, index, op):
    prob_size = np.shape(prob_arr)
    # current number and full problem strings
    num = ""
    prob = ""
    l = 0
    # while the returned string isnt whitespace move one index right
    while not num.isspace() and index+l < prob_size[1]:
        num = ""
        for k in range(prob_size[0]):
            # append the characters top to bottom until the bottom or operand is reached
            char = prob_arr[k][index+l]
            if not char == "+" and not char == "*":
                num += char
        # append the number and the operand if the string isnt whitespace
        if not num.isspace():
            prob += num + op
        l+=1
    # ignore trailing operand
    print(prob)
    solution = eval(prob[:-1])
    return solution

fullsum = 0
problem_size = np.shape(problem_array_2)
for i in range(problem_size[1]):
    # iterate over the bottom row until the next operand is found
    operator = problem_array_2[problem_size[0]-1][i]
    if not operator == " ":
        # build and solve the equation using the function
        fullsum += build_and_eval(problem_array_2, i, operator)
print(f"the properly calculated sum is {fullsum}")
