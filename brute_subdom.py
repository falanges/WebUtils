#!/usr/bin/env python
#_*_ coding: utf8 _*_

import dns.resolver
from os import path



def main():
	if path.exists('subdominios.txt'):											            # Tenes que bajarte una buena lista de subdominios para usar y dejarla en la misma carpeta
		wordlist = open('subdominios.txt','r')                            # de este script,sabes? tal vez alguna de https://github.com/danielmiessler/SecLists?
    
		wordlist = wordlist.read().split('\n')
		lista = []
		for s in wordlist:
			try:
				a = dns.resolver.query('{}.paginardi.com'.format(s),'A')			#'A' lo ponemos ya que si puede resolver la consulta de address, significa que existe
				lista.append('{}.paginardi.com'.format(s))
			except:
				pass
		if len(lista) > 0:
			print('Numero de subdominios posibles: {}'.format(len(lista)))
			for e in lista:
				print(e)
		else:
			print("No se encontraron subdominios.txt")
	else:
		print("No existe el archivo")


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
