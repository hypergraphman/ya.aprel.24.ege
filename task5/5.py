from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    alf = digits + ascii_uppercase
    while n > 0:
        r = alf[n % p] + r
        n //= p
    return r


def f(n):
    s1 = n_to_p(n, 7)
    if n % 7 == 0:
        s2 = s1 + s1[-2:]
    else:
        s2 = s1 + n_to_p(n % 7 * 2, 7)
    return int(s2, 7)


for n in range(2200, 0, -1):
    if f(n) < 220:
        print(n)
        break