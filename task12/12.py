f = open('12.txt', 'w')
for n in range(4, 10000):
    line = '8' + n * '5'
    while '8858' in line or '555' in line:
        if '8858' in line:
            line = line.replace('8858', '4', 1)
        else:
            line = line.replace('555', '58', 1)
        if '5858' in line:
            line = line.replace('5858', '85', 1)
    if sum(map(int, line)) == 66:
        print(n)
        f.write(str(n) + '\n')