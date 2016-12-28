#!/usr/bin/python -tt
# coding=UTF-8

#-t
# Issue a warning when a source file mixes tabs and spaces for indentation in a way that makes it depend on the worth of
# a tab expressed in spaces. Issue an error when the option is given twice (-tt).

# importa uma série de interfaces do sistema operacional
import sys
import os
import commands

def Cat(filename):
  try:
    f = open(filename)
    text = f.read()
    print '---', filename
    print text
  except IOError:
    print 'IO Error', filename

def List(dir):
  cmd = 'ls -l ' + dir
  print 'about to  do this:', cmd
  return
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write('there was an error:' + output)
    sys.exit(1)
  print output

  '''
  filenames = os.listdir(dir)
  for filename in filenames:
    path = os.path.join(dir, filename)
    print path
    print os.path.abspath(path)
  '''

def Hello(name):
	if name == 'Joston' or name == 'Muriel':
                print 'Alert: Joston Mode'
		name = name + '????'
	else:
		DoesNotExist(name)	
	name = name + '!!!!'
	print 'Hello', name # o print interpreta essa vírgula para colocar um espaço

# Define a main() function that prints a little greeting
def main():
  args = sys.argv[1:]
  print args
  for arg in args:
    Cat(arg)

'''This is the standard boilerplate that calls the main() function.
# Caso voce execute o programa usando python ou ./, esse if e true e o main e excutado
# Se você só quiser incluir esste arquivo em outro código, como um módulo, sem eexecutá-lo automaticamente, esse if vira false a função não é executada
# Esse código é um boilerplate pq vc pode usar em todo arquivo q quiser q haja assim
'''
if __name__ == '__main__':
	main()
