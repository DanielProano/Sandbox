
def GCD_find(a, b):
    if b == 0:
        return a
    return GCD_find(b, a % b)


def extended(u, v, y, x):
    a = u * y + x * v
    if a == 1:
        print(u, v)

def find_mod(x, y, mod):
    if y % mod == x:
        print(y)

# a^2 = x mod p (x is a list of possible quadratics in this
def find_modular_arithmetic(possible, p):
    for i in range(p):
        double = i * i
        left_over = double % p
        for j in possible:
            if j == left_over:
                print(f"Success: {i}")


# (a / p) = a ^ (p - 1) / 2 mod p
def legendre_sym(x, p):
    for i in x:
        num = pow(i, ((p - 1) // 2), p)
        if num == 1:
            print(i)

# p = 3 mod 4
def special_legendre(x, z):
    a = pow(x, (z + 1) // 4, z)
    print(a)

num = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768
prime = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161

class tonelli_shanks:
    def eulers_criterion(self, pot, p):
        if pow(pot, ((p - 1) // 2), p) == 1:
            return True
        return False
    def find_S_Q(self, p):
        S = 0
        Q = p - 1
        while Q % 2 == 0:
            Q //= 2
            S += 1
        return S, Q
    def find_z(self, p):
        for i in range(2, p, 1):
            z = self.eulers_criterion(i, p)
            if not z:
                return i

    def loop(self, M, c, t, R, p):
        if t == 1:
            return R
        for z in range(1, M):
            if t ** (2 ** z) % p == 1:
                i = z
                break
        b = pow(c, 2 ** (M - i - 1), p)
        return self.loop(i, pow(b, 2, p), (t * pow(b, 2, p)) % p, pow(R * b, 1, p), p)

get_r = tonelli_shanks()

if not get_r.eulers_criterion(num, prime):
    print("No square root")
S, Q= get_r.find_S_Q(prime)
print(S, Q)
z = get_r.find_z(prime)
print(z)
result = get_r.loop(S, pow(z, Q, prime), pow(num, Q, prime), pow(num, (Q+1) // 2, prime), prime)
print(result)