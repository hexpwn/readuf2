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

# Parse the arguments
parser = argparse.ArgumentParser(description='Get an overview of UF2 files. Like `readelf`, but for UF2 files.')
parser.add_argument('filename', metavar='FILENAME', type=str, nargs=1, help='the path to a UF2 file to be analyzed')

args = parser.parse_args()


