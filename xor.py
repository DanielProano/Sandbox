def xor_now(first: bytes, second: bytes) -> bytes:
    result = bytearray(len(first))
    for i in range(len(first)):
        result[i] = first[i] ^ second[i]

    print(result)
    return result

original_first = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"

original_second = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"

original_third = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"

original_final = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key_one = bytes.fromhex(original_first)

key_two = xor_now(bytes.fromhex(original_second), key_one)

key_three = xor_now(bytes.fromhex(original_third), key_two)

key_final = xor_now(xor_now(xor_now(key_one, key_two), key_three), bytes.fromhex(original_final))