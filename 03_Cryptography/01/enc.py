from Crypto.Cipher import AES  # type: ignore[import-not-found]
from Crypto.Util import Padding  # type: ignore[import-not-found]

key_hex_string = "00112233445566778899AABBCCDDEEFF"
iv_hex_string = "000102030405060708090A0B0C0D0E0F"
key = bytes.fromhex(key_hex_string)
iv = bytes.fromhex(iv_hex_string)
data = b"The quick brown fox jumps over the lazy dog"
print(f"Length of data: {len(data):d}")


# Encrypt the data piece by piece
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(data[0:32])
ciphertext += cipher.encrypt(Padding.pad(data[32:], 16))
print(f"Ciphertext: {ciphertext.hex()}")


# Encrypt the entire data
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(Padding.pad(data, 16))
print(f"Ciphertext: {ciphertext.hex()}")

# Decrypt the ciphertext
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)
print(
    f"Plaintext: {Padding.unpad(plaintext, 16)}"
)  # * Plaintext: b'The quick brown fox jumps over the lazy dog'
