x = 32321
y = 26513

def GCD_find(a, b):
    if b == 0:
        return a
    return GCD_find(b, a % b)


def extended(u, v):
    a = u * y + x * v
    if a == 1:
        print(u, v)

def find_mod(x, y, mod):
    if y % mod == x:
        print(y)

print(8146798528947 % 17)