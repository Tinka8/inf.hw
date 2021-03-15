def digit_sum1(n):
    sucet = 0

    for i in str(n):
        sucet = sucet + int(i)

    return sucet


def digit_sum2(n):
    sucet = 0

    while n > 0:
        cifra = n % 10
        sucet = sucet + cifra
        n = n // 10

    return sucet 
