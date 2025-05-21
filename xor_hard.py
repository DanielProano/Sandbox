hex_str_beg = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

possible_bytes = list(range(256))

for byte in possible_bytes:
    result = bytearray(len(hex_str_beg))
    for i in range(len(hex_str_beg)):
        result[i] = hex_str_beg[i] ^ byte

    try:
        out = result.decode('utf-8')
    except UnicodeDecodeError:
        continue
    print(out)
    print(byte)