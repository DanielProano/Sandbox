string = "label"

result = ""
for char in range(len(string)):
    result += chr(ord(string[char]) ^ 13)

print(result)