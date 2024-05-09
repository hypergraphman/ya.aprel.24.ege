*a, = map(int, open('17.txt'))
x = sorted(a)[-3]
# for i in range(len(a) - 2):
#     p1, p2, p3 = a[i], a[i + 1], a[i + 2]
b = []
for p1, p2, p3 in zip(a, a[1:], a[2:]):
    if (p1 % 2 != 0 or p2 % 2 != 0 or p3 % 2 != 0) and p1 + p2 + p3 <= x:
        b.append(p1 + p2 + p3)
print(len(b), max(b))

b = []
for t in zip(a, a[1:], a[2:]):
    if sum(el % 2 == 0 for el in t) <= 2 and sum(t) <= x:
        b.append(sum(t))
print(len(b), max(b))