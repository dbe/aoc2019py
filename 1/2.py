memo = {}

def run(lines):
    return sum([fuel(line) for line in map(int, lines)])

def fuel(amt):
    if(amt in memo):
        return memo[amt]

    if(amt <= 0):
        return 0

    needed = (amt // 3) - 2
    total = max(needed, 0) + fuel(needed)
    memo[amt] = total
    return total

def test_fuel():
    assert(fuel(1969) == 966)
    assert(fuel(100756) == 50346)
