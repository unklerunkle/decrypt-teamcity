#!/usr/bin/env python3

from Crypto.Cipher import DES3
from codecs import decode
from sys import argv

def unpad(padded):
    padding_len = padded[-1]
    return padded[:-padding_len]

def main():
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <ciphertext>")
        return

    ciphertext = argv[1]

    # Reconstruct key
    key_signed_byte_array = [61, 22, 11, 57, 110, 89, -20, -1, 0, 99, 111, -120, 55, 4, -9, 10, 11, 45, 71, -89, 21, -99, 54, 51]
    key_byte_array = [b & 0xff for b in key_signed_byte_array]
    key = bytes(key_byte_array)

    # Remove prefix and decode from hex
    des3_ciphertext = ciphertext.lstrip('zxx')
    des3_cipherbytes = decode(des3_ciphertext, 'hex')

    # Create cipher - assume ECB mode unless otherwise specified
    cipher = DES3.new(key, DES3.MODE_ECB)

    # Decrypt and unpad
    plaintext_padded = cipher.decrypt(des3_cipherbytes)
    plaintext = unpad(plaintext_padded)

    print(plaintext.decode('utf-8'))

if __name__ == '__main__':
    main()
