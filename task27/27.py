f = open('27_B.txt')
k, n = map(int, f.readline().split())
*a, = map(int, f)
b = [0] * len(a)
for i in range(1, len(a)):
    b[i] = a[i] + min(b[max(i - k, 0):i])
print(b[-1])