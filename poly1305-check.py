import sys
from poly1305 import get_tag

if len(sys.argv) < 4:
    print(f"Usage : {sys.argv[0]} <key> <file> <signature>")
    exit()

key = bytes.fromhex(sys.argv[1])

with open(sys.argv[2], "rb") as f:
    m = f.read()

tag = bytes.fromhex(sys.argv[3])

print("ACCEPT" if get_tag(key, m) == tag else "REJECT")