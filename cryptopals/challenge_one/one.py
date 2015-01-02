# -*- coding: utf-8 -*-
"""
cryptopals.challenge_one.one
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Convert hex to base 64.

The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

So go ahead and make that happen. You'll need to use this code for the rest of the exercises.
"""
from __future__ import print_function

import base64
import binascii

BASE_STRING = u'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
TARGET_RESULT = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

def hex_to_b64(hex_string):
    """
    This function turns a hexadecimal string into a base64 string.
    """
    bytestring = binascii.unhexlify(hex_string)
    return base64.b64encode(bytestring).decode('ascii')

if __name__ == '__main__':
    out = hex_to_b64(BASE_STRING)
    print("Input string: {}".format(BASE_STRING))
    print("Output string: {}".format(out))
    print("Correct output: {}".format(out == TARGET_RESULT))
