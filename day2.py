import numpy as np
import math

inputs = np.loadtxt('inputs/day2.txt', delimiter = ',', unpack = False)

def add(idx, lst):
    return lst[int(lst[idx + 1])] + lst[int(lst[idx + 2])]

def product(idx, lst):
    return lst[int(lst[idx + 1])] * lst[int(lst[idx + 2])]

def decode(program):
    current_i = 0
    for i in range(math.floor(len(program)/4)):
        if program[current_i] == 1:
            program[int(program[current_i+3])] = add(current_i, program)
        if program[current_i] == 2:
            program[int(program[current_i+3])] = product(current_i, program)
        if program[current_i] == 99:
            break
        current_i += 4
    return program

def inputchange(i1, i2):
    inputs = np.loadtxt('inputs/day2.txt', delimiter = ',', unpack = False)
    inputs[1] = i1
    inputs[2] = i2
    return decode(inputs)[0]

# print(decode(inputs)[0])
# print(inputchange(10, 2)) # 3101878

for i in range(99):
    for j in range(99):
        if inputchange(i, j) == 19690720:
            print(i, j)
