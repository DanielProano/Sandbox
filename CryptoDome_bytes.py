from Crypto.Util.number import *

byte_string = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

readable = long_to_bytes(byte_string)
print(readable)