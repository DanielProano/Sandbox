def xor_now(first: bytes, second: bytes) -> bytes:
    result = bytearray(len(first))
    for i in range(len(first)):
        result[i] = first[i] ^ second[i]

    print(result)
    return result

hex_str_beg = bytes.fromhex("0e0b213f26041e")

possible = "crypto{".encode()

xor_now(possible, hex_str_beg)

full_str = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

length = len(full_str) / 6
print(len(full_str))
print(length)
key = ("myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyr").encode()
print(len(key))

xor_now(key, full_str)
xor_now("myXORk".encode(), hex_str_beg)