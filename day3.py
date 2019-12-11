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

print(intersects)

# Manhattan distance
distances = [abs(i[0]) + abs(i[1]) for i in intersects]
print(min(distances)) # 248!!!
