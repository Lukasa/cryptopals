# -*- coding: utf-8 -*-
"""
cryptopals.challenge_one.five
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Implement repeating-key XOR

Here is the opening stanza of an important work of the English language:

    Burning 'em, if you ain't quick and nimble
    I go crazy when I hear a cymbal

Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the first
byte of plaintext will be XOR'd against I, the next C, the next E, then I again
for the 4th byte, and so on.

It should come out to:

0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
"""
from __future__ import print_function

import operator

from array import array
from binascii import hexlify
from itertools import cycle

# imap and izip don't exist in Python 3, the defaults do it.
try:
    from itertools import imap
except ImportError:
    imap = map


def to_py3_byte(byte):
    """
    Takes a single element of a bytestring and converts it to a byte in a
    platform-independent manner. In this case, a 'byte' is a Python 3 byte,
    namely an integer between 0 and 255.
    """
    if isinstance(byte, bytes):
        return ord(byte)
    else:
        return byte


def repeating_key_xor(stream, key):
    """
    Encrypts a stream of bytes ``stream`` using repeating-key XOR, with key
    ``key``.
    """
    # Make sure we're getting the right byte type.
    stream = imap(to_py3_byte, stream)
    key = imap(to_py3_byte, key)

    # Most of the magic actually happens here. If it wasn't for the fact that
    # we need to transform the bytes
    return array('B', imap(operator.xor, stream, cycle(key))).tostring()


if __name__ == '__main__':
    KEY = b"ICE"
    INPUT = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    EXPECTED_OUTPUT= "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

    encrypted = repeating_key_xor(INPUT, KEY)
    hex_encrypted = hexlify(encrypted).lower()

    if hex_encrypted == EXPECTED_OUTPUT:
        print("Encrypted correctly.")
    else:
        print("Incorrectly encrypted to {}".format(hex_encrypted))
