#!/bin/bash

# Create a sample text file with a length that is not a multiple of 16 bytes (29 bytes)
echo -n "This is a test message here!" >input.txt

# 1. Padding REQUIRED (CBC Mode)
# Block ciphers like CBC require data length to be a multiple of the block size (16 bytes).
# OpenSSL automatically applies PKCS#7 padding by default, making the output larger (32 bytes).
openssl enc -aes-128-cbc -e -in input.txt -out cbc_encrypted.bin \
  -K 00112233445566778899AABBCCDDEEFF \
  -iv 00000000000000000000000000000000

# 2. Padding NOT REQUIRED (CTR Mode)
# Counter mode turns the block cipher into a stream cipher, encrypting byte-by-byte
# via XOR. It handles arbitrary lengths natively without adding padding bytes.
openssl enc -aes-128-ctr -e -in input.txt -out ctr_encrypted.bin \
  -K 00112233445566778899AABBCCDDEEFF \
  -iv 00000000000000000000000000000000

# Compare the file sizes to see padding in action
echo "Original file size: $(wc -c <input.txt) bytes"                         # Original file size: 28 bytes
echo "CBC ciphertext size (with padding): $(wc -c <cbc_encrypted.bin) bytes" # CBC ciphertext size (with padding): 32 bytes
echo "CTR ciphertext size (no padding): $(wc -c <ctr_encrypted.bin) bytes"   # CTR ciphertext size (no padding): 28 bytes
