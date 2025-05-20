from Crypto.Cipher import DES
import binascii

# Hexadecimal ciphertext
ciphertext = binascii.unhexlify('03BAA1CA02056F071AA818381E4E281B')

# Key (kercy113) should be 8 bytes for DES
key = b'kercy113'

# Decrypting using DES ECB mode
cipher = DES.new(key, DES.MODE_ECB)
decrypted = cipher.decrypt(ciphertext)

# Print the decrypted message (raw bytes)
print(binascii.hexlify(decrypted))
