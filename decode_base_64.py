import base64

str = "U3RhcnQtU2xlZXAgLVNlY29uZHMgMjUwCkdldC1DaW1JbnN0YW5jZSAtQ2xhc3NOYW1lIFdpbjMyX1F1aWNrRml4RW5naW5lZXJpbmcgPiBDOlxpbmZvCg=="

byte_result = base64.b64decode(str)
result = byte_result.decode('utf-8')

print(result)