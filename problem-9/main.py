def check_pythagorean_triplet(a, b, c):
    return a*a + b*b == c*c

LIMIT = 999
for a in range(1, LIMIT):
    for b in range(1, LIMIT):
        c = 1000 - (a + b)
        if check_pythagorean_triplet(a, b, c):
            # since there is only one solution
            # we print it and exit
            print(a * b * c)
            exit(0)
