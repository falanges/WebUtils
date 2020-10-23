#!/usr/bin/env python
#_*_ coding: utf8 _*_

# este scrapper tiene la finalidad de scrappear una page en crudo

import urllib
import urllib.request
def main():
	file_web = open('web.html','w+')
	consulta = urllib.request.urlopen('https://lorem2.com/')
	consulta = consulta.read()
	file_web.write(str(consulta))
	file_web.close()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
