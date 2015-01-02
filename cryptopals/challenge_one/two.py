# -*- coding: utf-8 -*-
"""
cryptopals.challenge_one.two
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fixed XOR.

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965

... should produce:

746865206b696420646f6e277420706c6179
"""
from __future__ import print_function

import array
import binascii
import operator

try:
    from itertools import imap
except ImportError:
    imap = map


def bytes_xor(a, b):
    """
    XORs two equal length byte buffers.

    This avoids the Python 2/Python 3 bytestring mess by putting both
    strings into arrays, then iterating over them. It's frustrating that we
    have to do this, but there we are. It's even more frustrating that we need
    a temporary array at the end.
    """
    aa = array.array('B', a)
    bb = array.array('B', b)

    return array.array('B', imap(operator.xor, aa, bb)).tostring()


if __name__ == '__main__':
    TEST_STRING_A = u'1c0111001f010100061a024b53535009181c'
    TEST_STRING_B = u'686974207468652062756c6c277320657965'
    EXPECTED_RESULT = u'746865206b696420646f6e277420706c6179'

    a = binascii.unhexlify(TEST_STRING_A)
    b = binascii.unhexlify(TEST_STRING_B)

    result = bytes_xor(a, b)
    result = binascii.hexlify(result).decode('ascii')
    print("Result: {}".format(result))
    print("Success: {}".format(result == EXPECTED_RESULT))
