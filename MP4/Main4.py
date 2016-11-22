from TuringMachine import *
from FileReader import readFile

filename = " "
while len(filename) > 0:
	try:
		filename = input("Enter filename of Turing Machine (Leave blank to exit): ")
		tm = readFile(filename)
		inputStr = " "
		while len(inputStr) > 0:
			try:
				inputStr = input("Enter space separated input (integers only; leave blank to exit): ")
				inputs = [int(x) for x in inputStr.split(" ")]
				if len(inputStr) > 0:
					tm.run(inputs)
			except ValueError:
				if len(inputStr) > 0:
					print("Input format error. Try again.")
	except FileNotFoundError:
		if len(filename) > 0:
			print("File not found. Input another filename.")