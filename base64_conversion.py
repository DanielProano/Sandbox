import base64

from_str = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

raw_bytes = bytes.fromhex(from_str)
encoded_base = base64.encodebytes(raw_bytes)

print(encoded_base)