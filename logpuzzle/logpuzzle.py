#!/usr/bin/python
# coding=UTF-8
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order.
  /edu/languages/google-python-class/images/puzzle/a-babb.jpg
  into
  https://developers.google.com/edu/python/images/puzzle/a-baaa.jpg
  """
  f = open(filename, 'rU')
  text = f.read()
  f.close()
  imgs = re.findall('\/images.*\/.*\.jpg', text)

  unique_imgs = unique_list(imgs)
  return sorted(unique_imgs, key=img_key)

def unique_list(my_list):
  unique_list = {}
  for item in my_list:
    # match = re.search('\/\w-(\w*)-.*', item)
    # unique_id = match.group(1)
    # match = re.search('\/\w-\w\w\w\w-(\w\w\w\w)\.jpg', item)
    # unique_id = match.group(1)
    unique_list['https://developers.google.com/edu/python' + item] = ''
  return unique_list.keys()
  
def img_key(img):
  match = re.search('-(\w+)-(\w+)\.\w+', img)
  if match:
    return match.group(2)
  else:
    return img

def create_index_content(filenames):
  return '<html><body><img src="' + '"/><img src="'.join(filenames) + '"/></body></html>'

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  
  index = 0
  filenames = []
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

  for img_url in img_urls:
    filename = 'img' + str(index) + '.jpg'
    print 'Retrieving... ', img_url
    urllib.urlretrieve(img_url, dest_dir + '/' + filename)
    index += 1
    filenames.append(filename)
  index_file_content = create_index_content(filenames)
  
  f = open(dest_dir + '/index.html', 'w')
  f.write(index_file_content)
  


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])
  
  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
