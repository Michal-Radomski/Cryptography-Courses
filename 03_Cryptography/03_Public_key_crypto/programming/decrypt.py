from Crypto.Cipher import PKCS1_OAEP  # type: ignore[import-not-found]
from Crypto.PublicKey import RSA  # type: ignore[import-not-found]

ciphertext = open("ciphertext.bin", "rb").read()  # noqa: SIM115

prikey_pem = open("private.pem").read()  # noqa: SIM115
prikey = RSA.importKey(prikey_pem, passphrase="pass")
cipher = PKCS1_OAEP.new(prikey)
message = cipher.decrypt(ciphertext)
print(message)
