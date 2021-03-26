# readuf2
`readuf2` is supposed to be a `readelf` for [UF2](https://github.com/Microsoft/uf2) files.

A simple tool to get a quick understanding of what a UF2 file is carrying.

##### Disclaimer
The tool is a *Work In Progress*, please read [to-dos](#To-Do) for a quick idea of the currently missing functionalities.

<img src="img/demo.gif"  />

​																														*CRT not included*


## Requirements
* [Python 3](https://www.python.org/download/releases/3.0/)
* [Jinja2](https://pypi.org/project/Jinja2/)

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

## To-dos
* Handle UF2 *file container* flag 
* Handle UF2 *not-main-flash* flag
* Handle UF2 *MD5 checksum* flag
* Handle UF2 *extension tags* flag
* Handle UF2 *source embedding* in UF2 files

## Road-map
* Add `output-only` option flag
* Add `short-output` option flag
