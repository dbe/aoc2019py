def run(lines):
    count = 0
    for i in range(156218, 652527 + 1):
        count += 1 if valid(i) else 0
    return count
    # print(valid(112233))
    # print(valid(123444))
    # print(valid(111122))

def valid(i):
    s = str(i)
    for a, b in zip(s, s[1:]) :
        if(int(a) > int(b)):
            return False

    s = 'z' + str(i) + 'z'
    for i in range(len(s) - 3):
        if(s[i + 1] == s[i + 2] and s[i + 1] != s[i + 0] and s[i + 2] != s[i + 3]):
            return True

    return False
