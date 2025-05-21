hex_str = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

possible_bytes = list(range(256))

for byte in possible_bytes:
    result = bytearray(len(hex_str))
    for i in range(len(hex_str)):
        result[i] = hex_str[i] ^ byte
    print(f"{byte} first hex: {result}")