passrange = range(130254, 678275)

def checkadj(inp):
    return True in [str(inp)[i] == str(inp)[i+1] for i in range(len(str(inp))-1)]

def checkinc(inp):
    return False not in [int(str(inp)[i]) <= int(str(inp)[i+1]) for i in range(len(str(inp))-1)]

# print(sum([checkadj(i) and checkinc(i) for i in passrange])) # 2090!!

def makegrps(inp):
    counts = []
    for i in range(10):
        current = 0
        for d in str(inp):
            if int(d) == i:
                current += 1
        if current != 0:
            counts.append(current)
    return counts


first = list(filter(lambda p: checkadj(p) and checkinc(p), passrange)) # length = 2090

print(makegrps(112344))

second = list(filter(lambda p: 2 in makegrps(p), first))

print(len(second)) # 1419
