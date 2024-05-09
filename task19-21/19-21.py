def f(s1, s2, c, m):
    if c > m:
        return False
    if s1 + s2 >= 150:
        return c % 2 == m % 2
    moves = [f(s1 + 2, s2, c + 1, m),
             f(s1 * 3, s2, c + 1, m),
             f(s1, s2 + 2, c + 1, m),
             f(s1, s2 * 3, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, 133 + 1):
    for m in range(1, 4 + 1):
        if f(16, s, 0, m):
            if m == 4:
                print(s)
            break