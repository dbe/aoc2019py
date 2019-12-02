def run(lines):
    return sum([(line // 3) - 2 for line in map(int, lines)])
