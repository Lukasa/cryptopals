# -*- coding: utf-8 -*-
"""
cryptopals.challenge_one.four
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Detect single-character XOR
One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.
"""
from __future__ import print_function

from binascii import unhexlify

from three import guess_single_byte_xor

def search_fitness(items, fitness_function):
    """
    This function takes a set of items and a fitness function that can be
    applied to them. It applies the fitness function to each one, and returns
    the one that has the highest fitness value, along with anything returned
    by the fitness function.

    The fitness function is any function that takes only one argument (the
    item) and returns either the fitness or a tuple of elements where the first
    element is the fitness. If the second case, this function will include all
    subsequent elements in the tuple in the return value from this function.

    This function will always return a tuple, where the first element will be
    the most-fit item.
    """
    current_leader = None
    current_leader_fitness = 0

    for item in items:
        rval = fitness_function(item)

        if isinstance(rval, tuple):
            fitness, others = rval[0], rval[1:]
            others = (item,) + others
        else:
            fitness = rval
            others = (item,)

        if fitness > current_leader_fitness:
            current_leader = others
            current_leader_fitness = fitness

    return current_leader


def unhexlify_file(fobj):
    """
    Takes a file object and iterates over it line by line, decoding the hex
    string.
    """
    return (line.strip() for line in fobj if line)


if __name__ == '__main__':
    with open('four.txt', 'rb') as f:
        most_fit = search_fitness(unhexlify_file(f), guess_single_byte_xor)

        # The decoded string is in the second element of the tuple, with the
        # byte in the third.
        input_string, outcome, byte = most_fit

        print("String {} decoded into {}, using byte {}".format(
            input_string.decode('ascii'), outcome.decode('ascii'), byte
        ))
