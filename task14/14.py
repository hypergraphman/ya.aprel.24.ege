from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    alf = digits + ascii_uppercase
    while n > 0:
        r = alf[n % p] + r
        n //= p
    return r


print(n_to_p(7 * 49**120 - 6 * 343**65 - 5 * 7**40, 7).count('6'))