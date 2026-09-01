from Crypto.Hash import SHA256  # type: ignore[import-not-found]
from Crypto.PublicKey import RSA  # type: ignore[import-not-found]
from Crypto.Signature import pss  # type: ignore[import-not-found]

message = b"An important message"
key_pem = open("private.pem").read()  # noqa: SIM115
key = RSA.import_key(key_pem, passphrase="pass")
h = SHA256.new(message)
signer = pss.new(key)
signature = signer.sign(h)
open("signature.bin", "wb").write(signature)  # noqa: SIM115
