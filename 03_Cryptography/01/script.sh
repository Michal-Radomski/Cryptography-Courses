#!/bin/bash

# Create the plaintext files
echo -n "This is a known message!" >P1
echo -n "This is a top secret!" >P2

# Encrypt P1 using AES-128-OFB with a static key and IV
openssl enc -aes-128-ofb -e -in P1 -out C1 \
  -K 00112233445566778899AABBCCDDEEFF \
  -iv 00000000000000000000000000000000

# Encrypt P2 using the exact same key and IV (IV Reuse vulnerability demonstration)
openssl enc -aes-128-ofb -e -in P2 -out C2 \
  -K 00112233445566778899AABBCCDDEEFF \
  -iv 00000000000000000000000000000000

# Output results
echo "P1 (Plaintext): $(cat P1)"
echo "C1 (Ciphertext Hex): $(xxd -p C1)"
echo ""
echo "P2 (Plaintext): $(cat P2)"
echo "C2 (Ciphertext Hex): $(xxd -p C2)"

# P1 (Plaintext): This is a known message!
# C1 (Ciphertext Hex): a98c92dd6a6093008ed749f8f0f4ed0b82bdb005acddddfb

# P2 (Plaintext): This is a top secret!
# C2 (Ciphertext Hex): a98c92dd6a6093008ed756f9efa3f04e8caaa602ec
