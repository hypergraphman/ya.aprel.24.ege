def divs(n):
    res = {2, n // 2}
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                res.add(i)
            if n // i % 2 == 0:
                res.add(n // i)
    return len(res)


for x in range(397438, 443520 + 1, 2):
    temp = divs(x)
    if temp >= 142:
        print(temp, x // 2, sep='\t')