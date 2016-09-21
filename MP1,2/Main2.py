"""This file is responsible for being the main control for MP2

Author: Ryan Austin Fernandez
Date Last Edited: 09/21/2016
"""
from State import State
from FSM import FSM
from FSMReader import readFSM

quit = False

print("Machine Equivalence Checker\nLeave input empty to quit")

while not quit:
	fsm = [None] * 2
	# comparing 2 machines
	for ctr in range(2):
		ok = False
		# while filename not valid
		while not ok:
			filename = input(
				"Enter filename for machine %d: " 
				% (ctr + 1)
			)
			if filename == "":
				quit = True
				break
			try:
				# process FSM
				fsm[ctr] = readFSM(filename)
				ok = True
			except FileNotFoundError:
				print("File not found.")
		if quit:
			break

	if not quit:
		# if equal, print equivalence
		if fsm[0] == fsm[1]:
			print(fsm[0].name,"and",fsm[1].name,"are equivalent.")
			fsm[0].printEquivalence(fsm[1])
		else:
			print(fsm[0].name,"and",fsm[1].name,"are not equivalent.")