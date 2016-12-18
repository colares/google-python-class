#!/usr/bin/python -tt
# coding=UTF-8

# importa uma série de interfaces do sistema operacional
import sys

# Define a main() function that prints a little greeting
def main():
	print sys.argv # imprimirá uma lista python com inputs da chamada

'''This is the standard boilerplate that calls the main() function.
# Caso voce execute o programa usando python ou ./, esse if e true e o main e excutado
# Se você só quiser incluir esste arquivo em outro código, como um módulo, sem eexecutá-lo automaticamente, esse if vira false a função não é executada
# Esse código é um boilerplate pq vc pode usar em todo arquivo q quiser q haja assim
'''
if __name__ == '__main__':
	main()
