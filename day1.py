import numpy as np

inputs = np.loadtxt('inputs/day1.txt', delimiter = ',', unpack = False)

def sumfuel(masses):
    return sum([np.floor(mass/3)-2 for mass in masses])

# part 1
print(sumfuel(inputs))

def totalfuel(mass):
    current = mass
    total = 0
    while current >= 0:
        f = np.floor(current/3)-2
        if f > 0:
            total += f
            current = f
        else:
            break
    return total

# part 2
print(sum([totalfuel(mass) for mass in inputs]))
