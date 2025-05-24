x1 = "dqxqcius"
x2 = "YeaTtgUnzezBqiwa2025"

k = "nahamcon"

cae = ""

def reverse(t):
    r = ''
    for i in range(len(t)):
        c = t[i]
        if c.isalpha():
            o = 0
            if ord(c) >= 97:
                o = 97
            else:
                o = 65
            r += chr((ord(c) - o - 16 + 26) % 26 + o)
    print(r)

reverse(x1)

def vin_reverse(t, a):
    r = ''
    j = 0
    for i in range(len(t)):
        c = t[i]
        if c.isalpha():
            l = c.lower()
            d = ord(l[0]) - 97
            m = a[j % len(a)].lower()
            n = ord(m[0]) - 97
            e = ((d - n) + 26) % 26
            f = chr(e + 97)
            if c.isupper():
                f = f.upper()

            r += f
            j += 1
        else:
            r += c

    print(r)

vin_reverse(x2, k)
