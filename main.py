# coding: utf8

from bs4 import BeautifulSoup
import urllib.request
import os
import time
import sys

def main():
	def clear():
		os.system('cls' if os.name=='nt' else 'clear')

	def start():		
		a = 0
		b = 0
		c = 0
		i = '-'
		while True:
			while b <= 99:	
				while c <= 99:	
					url = 'https://vk.com/catalog.php?selection='+str(a)+i+str(b)+i+str(c)
					response = urllib.request.urlopen(url)
					soup = BeautifulSoup(response, 'lxml')
					users = soup.find_all("div", class_='column2')
					file = open("users.html", "a", encoding="utf-8")
					file.write(str(users))
					file.close()
					print(">parse "+url)
					c += 1
				c = 0
				b += 1
			b = 0
			a += 1

	def title():
		clear()
		print("\nVK.COM USERS PARSER BY DANILNEONOV v1.\n")
		print("\nDANIL NEONOV")
		print("VK - https://vk.com/neonovd")
		print("github - https://github.com/danilneonov/\n")
		print("1 - start parse")
		print("2 - clear date file")
		print("0 - exit the program\n")
		inp = input(">: ")
		if(inp == "1"):
			clear()
			start()
		elif(inp == "2"):
			f = open("users.html", "w", encoding='utf-8')
			f.write("")
			f.close()
			clear()
			print(">>File cleared successfully")
			time.sleep(1.5)
			return main()
		elif(inp == "0"):
			clear()
			sys.exit("Bay bay!")
		else:
			return main()
	title()

if __name__ == "__main__":
	main()