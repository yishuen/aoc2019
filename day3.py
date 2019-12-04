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

print(w1coords, w2coords)

def intersects(w1, w2):
    crosses = []
    for i in range(len(w1) - 1):
        for j in range(len(w2) - 1):
            w1[i+1] - w1[i]

    return crosses
