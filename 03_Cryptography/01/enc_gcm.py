from Crypto.Cipher import AES  # type: ignore[import-not-found]

key_hex_string = "00112233445566778899AABBCCDDEEFF"
iv_hex_string = "000102030405060708090A0B0C0D0E0F"
key = bytes.fromhex(key_hex_string)
iv = bytes.fromhex(iv_hex_string)
data = b"The quick brown fox jumps over the lazy dog"

# Encrypt the data
cipher = AES.new(key, AES.MODE_GCM, iv)
cipher.update(b"header")
ciphertext = bytearray(cipher.encrypt(data))
print(f"Ciphertext: {ciphertext.hex()}")

# Get the MAC tag
tag = cipher.digest()
print(f"Tag: {tag.hex()}")

# Corrupt the ciphertext
ciphertext[10] = 0x00

# Decrypt the ciphertext
cipher = AES.new(key, AES.MODE_GCM, iv)
cipher.update(b"header")
plaintext = cipher.decrypt(ciphertext)
print(f"Plaintext: {plaintext}")

# Verify the MAC tag
try:
    cipher.verify(tag)
except ValueError:
    print("*** Authentication failed ***")
else:
    print("*** Authentication is successful ***")

# Ciphertext: ed1759cf244fa97f87de552c1254b1894d1dad83d8f0e3fbacae523032e55d2ea0cfb1a30e806c2743a11d
# Tag: 701f3c84e2da10aae4b76c89e9ea8427
# Plaintext: b'The quick 7rown fox jumps over the lazy dog'
# *** Authentication failed ***
