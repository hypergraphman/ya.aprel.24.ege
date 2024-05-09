print('y w x u f')
for y in 0, 1:
    for w in 0, 1:
        for x in 0, 1:
            for u in 0, 1:
                f = int(not ((y <= w) == x) and u)
                print(y, w, x, u, f)