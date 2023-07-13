#!/usr/bin/env python3

import sys

file_name = sys.argv[1]
nb_bytes = int(sys.argv[2])
file_bytes = open(file_name, "rb").read()

size = int.from_bytes(file_bytes[0x0002 : 0x0002 + 4], "little")
offset = int.from_bytes(file_bytes[0x000A : 0x000A + 4], "little")

print("Size: " + str(size))
print("Offset: " + str(offset))
while offset < size:
    pixel = int.from_bytes(file_bytes[offset : offset + 3], "little")
    red = pixel & 0xFF
    green = (pixel >> 8) & 0xFF
    blue = (pixel >> 16) & 0xFF
    print("#" + format(red, "02x") + format(green, "02x") + format(blue, "02x"))
    offset += 3
