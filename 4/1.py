def run(lines):
    count = 0
    for i in range(156218, 652527 + 1):
        count += 1 if valid(i) else 0
    return count

def valid(i):
    s = str(i)
    repeated = False
    for a, b in zip(s, s[1:]) :
        if(a == b):
            repeated = True
        if(int(a) > int(b)):
            return False

    return repeated
