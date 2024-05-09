f = open('26.txt')
n = int(f.readline())
a = []
for i in range(n):
    p1, p2 = map(int, f.readline().split())
    a.append((i + 1, p1, p2))
a.sort(key=lambda x: min(x[1], x[2]))
print(a[-1][0])
k = 0
for i, p1, p2 in a[:-1]:
    if p1 < p2:
        k += 1
print(k)