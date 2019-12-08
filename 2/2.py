from copy import copy

def run(lines):
    mem = [int(line) for line in lines[0].split(',')]
    noun, verb = runner(mem)
    return 100 * noun + verb

def runner(mem):
    for noun in range(100):
        for verb in range(100):
            cp = copy(mem)
            cp[1] = noun
            cp[2] = verb
            go(cp)

            if(cp[0] == 19690720):
                return (noun, verb)

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
