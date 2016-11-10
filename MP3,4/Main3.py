from TWA import *
from FileReader import readFile

filename = " "
while len(filename) > 0:
	try:
		filename = input("Enter filename of Two-Way Accepter (Leave blank to exit): ")
		twa = readFile(filename)
		# print(twa.__str__())
		inputStr = " "
		while len(inputStr) > 0:
			inputStr = input("Enter string (Leave blank to exit): ")
			if len(inputStr) > 0:
				if twa.process(inputStr):
					print("String was accepted!")
				else:
					print("String was rejected!")
	except FileNotFoundError:
		if len(filename) > 0:
			print("File not found. Input another filename.")