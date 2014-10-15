#!/usr/bin/python
import re
import sys
import os

width = 128
height = 32
sizeofbyte = 8

src = open(sys.argv[1], 'r')
lines = src.readlines()
src.close()
dst = open(sys.argv[2], 'wb')
for x in range(0, height/sizeofbyte): #0,4
    for z in range(0, width):
        bits = ''
        for y in range(0, sizeofbyte): #0,8
            char = lines[sizeofbyte*x+y].rstrip()[width-1-z]
            if (char == '-' or char == ' '):
                bits += '0'
            else:
                bits += '1'
        bits = bits[::-1]
        bitsa = [int(bits,2)]
        ba = bytearray(bitsa)
        dst.write(ba)
dst.close()
