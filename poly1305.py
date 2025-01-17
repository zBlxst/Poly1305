import sys

if len(sys.argv) < 3:
    print(f"Usage : {sys.argv[0]} <key> <file>")
    exit()


P = 2**130 - 5



def get_tag(key, m):
    try:
        r = key[:16]
        s = key[16:]
        r = list(r)
        r[3] &= 0x0f
        r[7] &= 0x0f
        r[11] &= 0x0f
        r[15] &= 0x0f

        r[4] &= 0xfc
        r[8] &= 0xfc
        r[12] &= 0xfc

        r = bytes(r)
        assert(len(r) == 16)
        assert(len(s) == 16)
        # print(s)
        r = int.from_bytes(r, 'little')
        s = int.from_bytes(s, 'little')
    except:
        print("Key should be 64 hexcharacters")
        exit()
        
    accumulator = 0
    for i in range((15+len(m))//16):
        block = int.from_bytes(b"\x01" + m[16*i:16*(i+1)][::-1], 'big')
        accumulator += block
        accumulator *= r
        accumulator %= P
    accumulator += s
    accumulator &= (2**128-1)
    return accumulator.to_bytes(16, 'little')


# print(r)
# print(m)