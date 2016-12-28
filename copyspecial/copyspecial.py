#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def list(dir):
  filenames = os.listdir(dir)
  result = []
  for filename in filenames:
    match = re.search('__\w*__', filename)
    if match:
      path = os.path.join(dir, filename)
      result.append( os.path.abspath(path) )
  return result

# +++your code here+++
# Write functions and modify main() to call them



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  if todir:
    for full_filename in list(args[0]):
      shutil.copy(full_filename, todir)
    return

  if tozip:
    full_filenames = ' '.join( list(args[0]) )
    cmd = 'zip -j ' + tozip + ' ' + full_filenames
    (status, output) =  commands.getstatusoutput(cmd)
    if status:
      print 'Error: ', status, output
    return
  
  # default option 
  print '\n'.join( list(args[0]) )
  # Call your functions
  
if __name__ == "__main__":
  main()
