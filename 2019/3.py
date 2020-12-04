import itertools
tmp = ""
with open("3.txt", "r") as f:
    tmp = f.read()


wires = [item.split(',') for item in tmp.split('\n')]

#wires = [['R8','U5','L5','D3'],['U7','R6','D4','L4']] # (3,2) (3,2)

#wires = [["R75","D30","R83","U83","L12","D49","R71","U7","L72"], 
# ["U62","R66","U55","R34","D71","R55","D58","R83"]]
wires = [["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"], 
         ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]]


wire1, wire2 = wires

#crossings = set(itertools.chain(wire1)).intersection(itertools.chain(wire2))

#print(crossings)

curr = [0,0]
cable1 = [(0,0)]
cable2 = [(0,0)]

for w in wire1:
    if w[0] == 'U':
        x = cable1[-1][0]
        y = cable1[-1][1] + int(w[1:])
        #print("U", [x, y])
        cable1.append((x, y))
        curr[1] += int(w[1:])
    if w[0] == 'D':
        x = cable1[-1][0]
        y = cable1[-1][1] - int(w[1:])
        #print("D", [x,y])
        cable1.append((x,y))
        curr[1] -= int(w[1:])
    if w[0] == 'R':
        x = cable1[-1][0] + int(w[1:])
        y = cable1[-1][1]
        #print("R",[x,y])
        cable1.append((x,y))
        curr[0] += int(w[1:])
    if w[0] == 'L':
        x = cable1[-1][0] - int(w[1:])
        y = cable1[-1][1]
        #print("L",[x,y])
        cable1.append((x,y))
        curr[0] -= int(w[1:])

#print(curr)
curr = [0,0]

for w in wire2:
    if w[0] == 'U':
        x = cable2[-1][0]
        y = cable2[-1][1] + int(w[1:])
        #print("U", [x, y])
        cable2.append((x,y))
        curr[1] += int(w[1:])
    if w[0] == 'D':
        x = cable2[-1][0]
        y = cable2[-1][1] - int(w[1:])
        #print("D", [x,y])
        cable2.append((x,y))
        curr[1] -= int(w[1:])
    if w[0] == 'R':
        x = cable2[-1][0] + int(w[1:])
        y = cable2[-1][1]
        #print("R",[x,y])
        cable2.append((x,y))
        curr[0] += int(w[1:])
    if w[0] == 'L':
        x = cable2[-1][0] - int(w[1:])
        y = cable2[-1][1]
        #print("L",[x,y])
        cable2.append((x,y))
        curr[0] -= int(w[1:])

#print(curr)

del cable1[0]
del cable2[0]


#cable2 = [(t[1], t[0]) for t in cable2]

print(cable1, cable2, sep="\n")

intersect = set(cable1).intersection(cable2)
intersect = intersect.difference([(0,0)])

print(intersect)


distance = [abs(i[0]) + abs(i[1]) for i in intersect]

print(min(distance))

"""
def distancesum(vec1, vec2):
    dist = abs(vec1[0] - vec2[0]) + abs(vec1[1] - vec2[1])
    return dist
    
#central_port = [0,0]

#print(distancesum(vecs[0], central_port))


    ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"] 
    ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]
"""