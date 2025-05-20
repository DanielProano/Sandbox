import base64

hex_str = '91978b8df44c4da1761cc644c7622021'

bytes_data = bytes.fromhex(hex_str)

try:
    decoded = base64.b64decode(bytes_data)
    print(decoded.decode())
except Exception as e:
    print("Not working", e)