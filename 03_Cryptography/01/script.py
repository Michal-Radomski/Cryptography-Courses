# XOR two bytearrays
def xor(first, second):
    return bytearray(x ^ y for x, y in zip(first, second))


P1_s = "This is a known message!"
C1_s = "a98c92dd6a6093008ed749f8f0f4ed0b82bdb005acddddfb"
C2_s = "a98c92dd6a6093008ed756f9efa3f04e8caaa602ec"

P1 = bytes(P1_s, "utf-8")
C1 = bytearray.fromhex(C1_s)
C2 = bytearray.fromhex(C2_s)

tt = xor(P1, C1)
P2 = xor(tt, C2)
print("P2: " + str(P2, "utf-8"))  # * P2: This is a top secret!
