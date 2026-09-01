from Crypto.Cipher import PKCS1_OAEP  # type: ignore[import-not-found]
from Crypto.PublicKey import RSA  # type: ignore[import-not-found]

message = b"A secret message!\n"

key = RSA.importKey(open("public.pem").read())  # noqa: SIM115
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)
with open("ciphertext.bin", "wb") as f:
    f.write(ciphertext)
