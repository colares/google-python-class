#!/usr/bin/python -tt
# coding=UTF-8

import sys

def Cat(filename):
	f = open(filename, 'rU')
	lines = f.readlines()
	print lines
	f.close() # se vc omite, ele fecha quando o processo termina

# r The mode can be 'r', 'w' or 'a' for reading (default),\nwriting or appending. 
# U Add a 'U' to mode to open the file for input with universal newline\nsupport.  Any line ending in the input file will be seen as a '\\n'\nin Python.  Also, a file so opened gains the attribute 'newlines';\nthe value for this attribute is one of None (no newline read yet),\n'\\r', '\\n', '\\r\\n' or a tuple containing all the newline types seen.\n\n'U' cannot be combined with 'w' or '+' mode."

def main():
	Cat(sys.argv[1])

if __name__ == '__main__':
	main()
