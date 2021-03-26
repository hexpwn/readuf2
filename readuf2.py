#!/usr/bin/env python3

'''
    https://github.com/hexpwn/readuf2
    Version: 0.0a

    `readuf2` is supposed to be a `readelf` for UF2 files. 
    A simple tool to get a quick understanding of what a UF2 files is packing.

    License: IDGAF 1.0
'''

from uf2 import UF2
import argparse
import sys

# Console shenanigans
e = '\033[31m[:(]\033[0m'
s = '\033[32m[:)]\033[0m'

# Important variables
magic_number        = b'\x55\x46\x32\x0a'
second_magic_number = b'\x57\x51\x5d\x9e'
final_magic_number  = b'\x30\x6f\xb1\x0a'

families = {
    'SAMD21': 0x68ed2b88,
    'SAML21': 0x1851780a,
    'SAMD51': 0x55114460,
    'NRF52': 0x1b57745f,
    'STM32F0': 0x647824b6,
    'STM32F1': 0x5ee21072,
    'STM32F2': 0x5d1a0a2e,
    'STM32F3': 0x6b846188,
    'STM32F4': 0x57755a57,
    'STM32F7': 0x53b80f00,
    'STM32G0': 0x300f5633,
    'STM32G4': 0x4c71240a,
    'STM32H7': 0x6db66082,
    'STM32L0': 0x202e3a91,
    'STM32L1': 0x1e1f432d,
    'STM32L4': 0x00ff6919,
    'STM32L5': 0x04240bdf,
    'STM32WB': 0x70d16653,
    'STM32WL': 0x21460ff0,
    'ATMEGA32': 0x16573617,
    'MIMXRT10XX': 0x4FB2D5BD,
    'LPC55': 0x2abc77ec,
    'GD32F350': 0x31D228C6,
    'ESP32S2': 0xbfdd4eee,
    'RP2040': 0xe48bff56
}

# Parse the arguments
parser = argparse.ArgumentParser(description='Get an overview of UF2 files.\
 Like `readelf`, but for UF2 files.')
parser.add_argument('filename', metavar='FILENAME', type=str, nargs=1, \
					help='the path to a UF2 file to be analyzed')
args = parser.parse_args()

# Initialize the UF2 block
filename = args.filename[0]
print(f'{s} Parsing {filename}')

# Load UF2 file to memory
try:
	f = open(filename, 'rb').read()
except FileNotFoundError:
	print(f'{e} {filename} was not found')
	sys.exit(-1)


### Parsing start here
if len(f) < 512: # Check file size
	print(f'{e} File is not large enough to be a UF2 file. Min. size is 512 \
bytes. This file is {len(f)} bytes long...')
	sys.exit(-1)

bi = 0 # Block index
while True:
	# Check block size
	try:
		b = f[bi*512:bi*512+512]
	except IndexError:
		print(f'{e} Block is not large enough to be a UF2 file. Min. size is \
512	bytes. This block is {len(f[bi*512:])} bytes long...')
		sys.exit(-1)
	block.magic1			= b[0:4]
	block.magic2			= b[4:8]	
	block.flags 			= b[8:12]
	block.target_addr 		= b[12:16]
	block.num_bytes			= b[16:20]
	block.seq_num			= b[20:24]
	block.num_blocks 		= b[24:28]
	block.family_or_size 	= b[28:32]
	block.data				= b[32:508]
	block.magic3			= b[508:512]

	if block.magic1 != magic_number:
		print(f'{e} Block does not have the correct UF2 magic number')
		print(f'     Bytes 0:4 are: {block.magic1.hex()}')
		sys.exit(-1)

	if block.magic2 != second_magic_number:
		print(f'{e} Block does not have the correct UF2 magic number')
		print(f'     Bytes 4:8 are: {block.magic2.hex()}')
		sys.exit(-1)

