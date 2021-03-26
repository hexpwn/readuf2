# readuf2
`readuf2` is supposed to be a `readelf` for [UF2](https://github.com/Microsoft/uf2) files.

A simple tool to get a quick understanding of what a UF2 file is packing.

## Requirements
* Python 3
* Jinja2

## Installation

`pip -R requirements.txt` should install all necessary files.

## Usage

```
usage: readuf2.py [-h] [-o, --output output_filename] FILENAME

Get an overview of UF2 files. Like `readelf`, but for UF2 files.

positional arguments:
  FILENAME              		 the path to a UF2 file to be analyzed

optional arguments:
  -h, --help                     show this help message and exit
  -o, --output output_filename   an optional path for an output binary file
```
