with open('inputs/day3.txt') as f:
    lines = f.read().splitlines()

wire1 = lines[0].split(',')
wire2 = lines[1].split(',')

def move(direction):
    if direction[0] == 'U':
        return (0, int(direction[1:]))
    if direction[0] == 'D':
        return (0, -int(direction[1:]))
    if direction[0] == 'L':
        return (-int(direction[1:]), 0)
    if direction[0] == 'R':
        return (int(direction[1:]), 0)

wire1moves = [move(d) for d in wire1]
wire2moves = [move(d) for d in wire2]

def positions(moves):
    coordinates = [(0, 0)]
    for m in moves:
        new = (coordinates[-1][0] + m[0], coordinates[-1][1] + m[1])
        coordinates.append(new)
    return coordinates

w1coords = positions(wire1moves)
w2coords = positions(wire2moves)

def coordpairs(coords):
    return [(coords[i], coords[i+1]) for i in range(len(coords) - 1)]

w1routes = coordpairs(w1coords)
w2routes = coordpairs(w2coords)

def intersect(routepairs):
    first = sorted(routepairs[0])
    if first[0][1] == first[1][1]:
        hor = first
        ver = sorted(routepairs[1])
    else:
        hor = sorted(routepairs[1])
        ver = first
    if hor[0][0] <= ver[0][0] <= hor[1][0] and ver[0][1] <= hor[0][1] <= ver[1][1]:
        return (ver[0][0], hor[0][1])

intersects = []
for w1r in w1routes:
    for w2r in w2routes:
        point = intersect((w1r, w2r))
        if point != None:
            intersects.append(point)

# Manhattan distance
distances = [abs(i[0]) + abs(i[1]) for i in intersects]
print(min(distances)) # 248!!!

# part 2
# print(w1routes)
def steps(route):
    path = []
    current = (0, 0)
    for r in route:
        if r[0] > 0:
            path.extend([(current[0] + i, current[1]) for i in range(1, r[0]+1)])
        elif r[0] < 0:
            path.extend([(current[0] - i, current[1]) for i in range(1, abs(r[0])+1)])
        elif r[1] > 0:
            path.extend([(current[0], current[1] + i) for i in range(1, r[1]+1)])
        elif r[1] < 0:
            path.extend([(current[0], current[1] - i) for i in range(1, abs(r[1])+1)])

        current = (current[0] + r[0], current[1] + r[1])

    return path


w1path = steps(wire1moves)
w2path = steps(wire2moves)


def distancetointersect(wirepath, intersect):
    for i in range(len(wirepath)):
        if wirepath[i] == intersect:
            return i+1

traveldist = [distancetointersect(w1path, i) + distancetointersect(w2path, i) for i in intersects]
print(sorted(traveldist)) # min is 28580!
