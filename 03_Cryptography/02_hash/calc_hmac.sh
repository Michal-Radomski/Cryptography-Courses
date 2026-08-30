#!/bin/bash

# Check if both secret key and message/file are provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <secret_key> <message_or_file>"
  exit 1
fi

SECRET_KEY="$1"
INPUT="$2"

echo "Calculating HMAC-SHA256..."

if [ -f "$INPUT" ]; then
  # If input is a file, compute HMAC of the file contents
  openssl dgst -sha256 -hmac "$SECRET_KEY" "$INPUT"
else
  # If input is a plain text string
  echo -n "$INPUT" | openssl dgst -sha256 -hmac "$SECRET_KEY"
fi
