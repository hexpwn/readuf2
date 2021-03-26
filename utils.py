#!/usr/bin/env python3

# Helper functions to pretty-print data
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
	r = ''
	for i in range(len(raw)//16):
		data = raw[i*16:(i*16)+16]
		while(len(data) < 16):
			data += b'\x00'
		r += f"{i*16:#010x}   {data.hex(' ', 1)}  {printableArray(data)}\n"
	return r
