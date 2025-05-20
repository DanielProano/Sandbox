import hmac
import hashlib
import os

directory = "."
sign = "ciCloud-API-20240315-4f7b9c"

count = 0
total = 0
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        base = filename[:-4]
        file = base + ".hmac"

        if os.path.exists(os.path.join(directory, file)):
            with open(filename, "rb") as f:
                message = f.read()
            print(f"Message #: {filename}")

            with open(file, "r") as f:
                expected = f.read().strip()

            calc = hmac.new(sign.encode(), message, hashlib.sha256).hexdigest()

            print(f"stored: {expected}")
            total += 1
            if calc == expected:
                count += 1
            else:
                print(f"HEREEEE   HMAC: {calc}")

print(f"Valid HMAC: {count} total {total}")