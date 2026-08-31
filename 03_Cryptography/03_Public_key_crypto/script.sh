#!/bin/bash

# Generating RSA Keys (Using 2048 bits for better security)
openssl genrsa -aes128 -out private.pem 2048

# View the Private Key
openssl rsa -in private.pem -noout -text

# Extracting the Public Key
openssl rsa -in private.pem -pubout -out public.pem

# View the Public Key
openssl rsa -in public.pem -pubin -text -noout

# Encryption
echo "This is a secret." >msg.txt
openssl pkeyutl -encrypt -inkey public.pem -pubin \
  -in msg.txt -out msg.enc

xxd msg.enc

# Decryption
openssl pkeyutl -decrypt -inkey private.pem \
  -in msg.enc -out msg.dec

# View decrypted message
cat msg.dec
