#!/bin/bash

#* Run: bash hash.sh test.txt

# Check if a filename was provided as an argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <filename>"
  exit 1
fi

FILE="$1"

# Check if the file actually exists
if [ ! -f "$FILE" ]; then
  echo "Error: File '$FILE' does not exist."
  exit 1
fi

echo "Calculating cryptographic hashes for: $FILE"
echo "----------------------------------------"
echo "SHA-256: $(sha256sum "$FILE" | awk '{print $1}')"
echo "SHA-1:   $(sha1sum "$FILE" | awk '{print $1}')"
echo "MD5:     $(md5sum "$FILE" | awk '{print $1}')"

# SHA-256: 39388cbc483a423495efa37883c713081540e5c8b2a6a40225c97a406a8af73f
# SHA-1:   6522949e8e001cfdd5a02e813bda30280bccd56f
# MD5:     db09472198c9b4dd5496d93f16ba788e
