from Crypto.PublicKey import RSA  # type: ignore[import-not-found]

key = RSA.generate(2048)
pem = key.export_key(format="PEM", passphrase="pass")
with open("private.pem", "wb") as f:
    f.write(pem)


pub = key.publickey()
pub_pem = pub.export_key(format="PEM")
with open("public.pem", "wb") as f:
    f.write(pub_pem)
