for a in range(0, 100):
    if all(((x >= a) or (121 >= x**2)) and ((y**2 < 49) or (a < y)) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)