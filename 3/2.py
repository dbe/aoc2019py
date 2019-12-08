def run(lines):
    v1 = parse(lines[0].split(','))
    v2 = parse(lines[1].split(','))
    # v1 = parse('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','))
    # v2 = parse('U62,R66,U55,R34,D71,R55,D58,R83'.split(','))
    # v1 = parse('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','))
    # v2 = parse('U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(','))

    p1 = points(v1)
    p2 = points(v2)

    crossings = set(p1) & set(p2)
    return min([p1.index(c) + p2.index(c) for c in crossings]) + 2

def points(vectors):
    out = []

    point = (0, 0)
    for v in vectors:
        for i in range(v[0]):
            #Y direction
            if(v[1]):
                point = (point[0], point[1] + v[2])
            #X direction
            else:
                point = (point[0] + v[2], point[1])

            out.append(point)

    return out

def parse(dirs):
    #(distance, x/y, step)
    #Eg. (120, 0, 1) means go 120 in the positive x direction
    out = []

    for dir in dirs:
        if dir[0] == 'R':
            out.append( (int(dir[1:]),0, 1) )
        elif dir[0] == 'D':
            out.append( (int(dir[1:]),1, -1) )
        elif dir[0] == 'L':
            out.append( (int(dir[1:]),0, -1) )
        else:
            out.append( (int(dir[1:]),1, 1) )

    return out
