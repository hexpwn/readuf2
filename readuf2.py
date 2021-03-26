#!/usr/bin/env python3

'''
    https://github.com/hexpwn/readuf2
    Version: 0.01

    `readuf2` is supposed to be a `readelf` for UF2 files. 
    A simple tool to get a quick understanding of what a UF2 files is packing.

    License: IDGAF 1.0
'''

from uf2 import UF2
from jinja2 import nativetypes
import argparse
import sys
import struct

# Console shenanigans
e = '\033[31m[:(]\033[0m'
s = '\033[32m[:)]\033[0m'

# Important variables
magic_number        = b'\x55\x46\x32\x0a'
second_magic_number = b'\x57\x51\x5d\x9e'
final_magic_number  = b'\x30\x6f\xb1\x0a'

# Parse the arguments
parser = argparse.ArgumentParser(description='Get an overview of UF2 files.\
 Like `readelf`, but for UF2 files.')
parser.add_argument('filename', metavar='FILENAME', type=str, nargs=1, \
					help='the path to a UF2 file to be analyzed')
parser.add_argument('-o, --output', metavar='output_filename', type=str, \
					nargs=1, help='an optional path for an output binary file',\
					dest='output')
args = parser.parse_args()

# Load the file into memory
filename = args.filename[0]

try:
	f_ = open(filename, 'rb')
	f = f_.read()
	f_.close()
except FileNotFoundError:
	print(f'{e} {filename} was not found')
	sys.exit(-1)

# Helper functions (too lazy to split into a utils.py file right now...)
def printableByte(b):
    if (b < 127) & (b > 32):
        return chr(b)
    else:
        return '.'

def printableArray(arr):
    r = ''
    for c in arr:
        r += printableByte(c)
    return r

def printableData(raw):
	''' not how it workssss.... #FIXME '''
	r = ''
	for i in range(len(raw)//16):
		data = raw[i*16:(i*16)+16]
		while(len(data) < 16):
			data += b'\x00'
		r += f"{i*16:#010x}   {data.hex(' ', 1)}  {printableArray(data)}\n"
	return r


### Parsing start here
if len(f) < 512: # Check file size
	print(f'{e} File is not large enough to be a UF2 file. Min. size is 512 \
bytes. This file is {len(f)} bytes long...')
	sys.exit(-1)

bi 		= 0 	# Block index
block 	= UF2() # Block object
rawdata	= b'' 	# Used to print the final data output of the file

while True:
	# Carve block from file
	try:
		b = f[bi*512:bi*512+512]
	except IndexError:
		print(f'{e} Block is not large enough to be a UF2 file. Min. size is \
512	bytes. This block is {len(f[bi*512:])} bytes long...')
		sys.exit(-1)

	block.magic1			= b[0:4]
	block.magic2			= b[4:8]
	block.flags 			= struct.unpack("I", b[8:12])
	block.target_addr 		= struct.unpack("I", b[12:16])
	block.num_bytes			= struct.unpack("I", b[16:20])[0]
	block.seq_num			= struct.unpack("I", b[20:24])[0]
	block.num_blocks 		= struct.unpack("I", b[24:28])[0]
	block.family_or_size	= struct.unpack("I", b[28:32])[0]
	block.data				= b[32:508]
	block.magic3			= b[508:512]

	if block.magic1 != magic_number:
		print(f'{e} Block does not have the correct UF2 magic number')
		print(f'     Bytes 0:4 are: {(block.magic1).hex()}')
		sys.exit(-1)

	if block.magic2 != second_magic_number:
		print(f'{e} Block does not have the correct UF2 magic number')
		print(f'     Bytes 4:8 are: {(block.magic2).hex()}')
		sys.exit(-1)

	if block.magic3 != final_magic_number:
		print(f'{e} Block does not have the correct UF2 magic number')
		print(f'     Bytes 508:512 are: {(block.magic3).hex()}')
		sys.exit(-1)

	env = nativetypes.NativeEnvironment()
	template = env.from_string("""
{{ '-' * 77 }}
Target address:	{{ block.getAddress() }}
Block size:	{{ block.num_bytes }} bytes
Seq number: 	{{ block.seq_num }}/{{ block.num_blocks - 1 }}
Flags:		[{{ '*' if block.getFlag1() else ' ' }}] not main flash	\
		[{{ '*' if block.getFlag2() else ' ' }}] file container
		[{{ '*' if block.getFlag3() else ' ' }}] familyID present	\
		[{{ '*' if block.getFlag4() else ' ' }}] MD5 checksum present
		[{{ '*' if block.getFlag5() else ' ' }}] extension tags present\
{% if block.getFlag3() %}
FamilyID:	{{ block.getFamilyId() }} - {{ block.getFamilyName() }}
{% else %}
File size: {{ block.getFamilyId() }} bytes
{% endif %}
Data:
{{ block.printableData() }}
""")
	print(template.render(block=block))
	
	rawdata += block.data[:block.num_bytes]
	
	if args.output != None:
		with open(args.output[0], 'wb') as of:
			of.write(rawdata)
					
	# Parse next block?
	if block.seq_num < block.num_blocks - 1:
		bi += 1
	else:
		print(f'{"-" * 77}')
		print(f'Output data:')
		print(printableData(rawdata))
		break

