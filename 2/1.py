def run(lines):
    mem = [int(line) for line in lines[0].split(',')]
    mem[1] = 12
    mem[2] = 2

    go(mem)
    return mem[0]

def go(mem):
    p = 0
    while(mem[p] != 99):
        f = add if mem[p] == 1 else mult
        a, b, c = mem[p+1:p+4]
        mem[c] = f(mem[a],mem[b])
        p += 4

def add(a, b):
    return a + b

def mult(a, b):
    return a * b
