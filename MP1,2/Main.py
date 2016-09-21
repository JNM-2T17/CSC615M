"""This file is responsible for being the main control for MP1

Author: Ryan Austin Fernandez
Date Last Edited: 09/21/2016
"""
from State import State
from FSM import FSM
from FSMReader import readFSM

quit = False

print("State Equivalence Checker\nLeave input empty to quit")

# for all user inputs
while not quit:
	ok = False
	# while invalid file
	while not ok:
		filename = input("Enter filename (leave empty to quit): ")
		if filename == "":
			quit = True
			break
		try:
			fsm = readFSM(filename)
			ok = True
			fsm.printEquivalence()
		except FileNotFoundError:
			print("File not found.")
		