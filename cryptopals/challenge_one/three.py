# -*- coding: utf-8 -*-
"""
cryptopals.challenge_one.three
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Single byte XOR cipher.

The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the
message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character
frequency is a good metric. Evaluate each output and choose the one with the
best score.
"""
from __future__ import print_function, division

import binascii
import math
import struct

from collections import Counter

from two import bytes_xor


# Use xrange wherever possible
try:
    range = xrange
except NameError:
    pass


# This is an approximate character frequency table of the English language.
# We'll use it to determine which plaintext is closest to being English. The
# table maps character to frequency, a number between 0 and 1. Note that this
# table implicitly assumes an ASCII representation of the english language.
FREQUENCY_TABLE = {
    b'a':  0.08167,
    b'b':  0.01492,
    b'c':  0.02782,
    b'd':  0.04253,
    b'e':  0.1270,
    b'f':  0.02228,
    b'g':  0.02015,
    b'h':  0.06094,
    b'i':  0.06966,
    b'j':  0.00153,
    b'k':  0.00772,
    b'l':  0.04025,
    b'm':  0.02406,
    b'n':  0.06749,
    b'o':  0.07507,
    b'p':  0.01929,
    b'q':  0.00095,
    b'r':  0.05987,
    b's':  0.06327,
    b't':  0.09056,
    b'u':  0.02758,
    b'v':  0.00978,
    b'w':  0.02360,
    b'x':  0.00150,
    b'y':  0.01974,
    b'z':  0.00074,
}

# The table is useless in Python 3, where each individual string will be
# analysed as a byte. This code transforms it when necessary.
if isinstance(b'a'[0], int):
    FREQUENCY_TABLE = {x[0]: y for x, y in FREQUENCY_TABLE.items()}


def englishness(a):
    """
    This function determines how 'likely' a string is to be English, based on
    character frequency. Returns a value between 0 and 1, where 0 means
    'totally unlike English', and 1 means 'exactly like English'.

    Implementation wise, this calculates what my old statistics textbook calls
    the 'Bhattacharyya Coefficient'. This is a fairly intuitive measure of
    overlap of two different distributions: for each point in the distribution,
    multiply the probability for each distribution together, then take the
    square root. Sum all the probabilities together, and you get your
    coefficient. Simple, right?
    """
    # Use the Counter dictionary to find out how often each character appears
    # as a sum total.
    c = Counter(a.lower())
    total_characters = len(a)

    # We then want to sum the square roots of the products of the probability
    # from both the counter dictionary c and the English frequency table. If an
    # element is entirely absent then the frequency is zero: this penalises
    # punctuation heavily.
    coefficient = sum(
        math.sqrt(FREQUENCY_TABLE.get(char, 0) * y/total_characters)
        for char, y in c.items()
    )

    return coefficient


def single_byte_xor(string, byte):
    """
    Given a byte, XORs all characters in a byte string with that byte and
    returns it.

    We do this the cheap way by re-using the bytes_xor string from part two,
    buiding a string that is all the same byte.
    """
    test_string = struct.pack("B", byte) * len(string)
    return bytes_xor(string, test_string)


def guess_single_byte_xor(string):
    """
    Given a string that has been 'encrypted' by a single byte XOR cipher,
    attempts to work out which byte was used by brute force testing every
    possible byte and testing the 'englishness' of the result. Returns the
    decrypted string and the byte that decrypted it.
    """
    results = ((single_byte_xor(string, byte), byte) for byte in range(0, 256))
    emap = [(englishness(r[0]), r[0], r[1]) for r in results]

    emap.sort(key=lambda x: x[0], reverse=True)
    winner = emap[0]

    return winner[1], winner[2]


if __name__ == '__main__':
    TEST_STRING = u'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    bytestring = binascii.unhexlify(TEST_STRING)

    outcome, byte = guess_single_byte_xor(bytestring)
    print("Decoded string is {}, using byte {}".format(outcome.decode('ascii'), byte))
