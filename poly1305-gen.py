import sys
from poly1305 import get_tag

if len(sys.argv) < 3:
    print(f"Usage : {sys.argv[0]} <key> <file>")
    exit()

key = bytes.fromhex(sys.argv[1])


with open(sys.argv[2], "rb") as f:
    m = f.read()

print(get_tag(key, m).hex())