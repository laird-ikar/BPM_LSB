#!/usr/bin/env python3

import sys

file_name = sys.argv[1]
nb_bytes = int(sys.argv[2])
file_bytes = open(file_name, "rb").read()

size = int.from_bytes(file_bytes[0x0002 : 0x0002 + 4], "little")
offset = int.from_bytes(file_bytes[0x000A : 0x000A + 4], "little")

print("Size: " + str(size))
print("Offset: " + str(offset))
bit_count = 0
byte = 0
byte_arr = []
while offset < size:
	pixel = int.from_bytes(file_bytes[offset : offset + 3], "little")
	red = pixel & 0xFF
	green = (pixel >> 8) & 0xFF
	blue = (pixel >> 16) & 0xFF
	byte = (byte << nb_bytes) | (red & ((1 << nb_bytes) - 1))
	bit_count += nb_bytes
	if (bit_count == 8):
		byte_arr.append(byte)
		byte = 0
		bit_count = 0
	byte = (byte << nb_bytes) | (green & ((1 << nb_bytes) - 1))
	bit_count += nb_bytes
	if (bit_count == 8):
		byte_arr.append(byte)
		byte = 0
		bit_count = 0
	byte = (byte << nb_bytes) | (blue & ((1 << nb_bytes) - 1))
	bit_count += nb_bytes
	if (bit_count == 8):
		byte_arr.append(byte)
		byte = 0
		bit_count = 0
	print("#" + format(red, "02x") + format(green, "02x") + format(blue, "02x"))
	offset += 3

open(file_name + ".out", "wb").write(bytearray(byte_arr))
