def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

def LCM(a, b):
    return a * b // GCD(a, b)

running_lcm = 1
for i in range(1, 21):
    running_lcm = LCM(running_lcm, i)

print(running_lcm)
