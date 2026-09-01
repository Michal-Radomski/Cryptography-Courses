from Crypto.Hash import SHA256  # type: ignore[import-not-found]
from Crypto.PublicKey import RSA  # type: ignore[import-not-found]
from Crypto.Signature import pss  # type: ignore[import-not-found]

message = b"An important message"
signature = open("signature.bin", "rb").read()  # noqa: SIM115
key = RSA.import_key(open("public.pem").read())  # noqa: SIM115
h = SHA256.new(message)
verifier = pss.new(key)
try:
    verifier.verify(h, signature)
    print("The signature is valid.")
except (ValueError, TypeError):
    print("The signature is NOT valid.")
