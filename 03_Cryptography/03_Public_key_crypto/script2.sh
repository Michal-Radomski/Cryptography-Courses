#!/bin/bash

# Generating Hash
openssl sha256 -binary msg.txt >msg.sha256
xxd msg.sha256

# Signing
openssl pkeyutl -sign -inkey private.pem -in msg.sha256 -pkeyopt digest:sha256 -out msg.sig

# Verifying
openssl pkeyutl -verifyrecover -inkey public.pem -in msg.sig -pubin | xxd
openssl dgst -sha256 -verify public.pem -signature msg.sig msg.txt
