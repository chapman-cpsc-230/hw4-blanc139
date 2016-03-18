"""
File: count_pairs.py

Copyright (c) 2016 Grayden Blanchard

License: MIT

Write a program to count the pairs in a strand of DNA.
"""

def count_pairs(dna, pair):
    i = 0 #counter
    j = 0 #string index
    while i < len(dna):
        if dna(j) == pair:
            i += 1
        pair += 1
    return i


dna = 'ACTGCTATCCATT'
pair = 'AT'
n = count_pairs(dna, pair)

print "The base %s appears %d times in %s" % (pair, n, dna)
