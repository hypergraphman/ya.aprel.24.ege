def f(s, e):
    if s > e or s == 11:
        return 0
    if s == e:
        return 1
    moves = [f(s + 1, e),
             f(s + 4, e),
             f(s * 3, e)]
    return sum(moves)


print(f(7, 27) * f(27, 42))