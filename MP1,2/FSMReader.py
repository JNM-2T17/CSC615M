"""This module is responsible for reading FSM-definition text files

Author: Ryan Austin Fernandez
Date Last Edited: 09/21/2016
"""
from State import State
from FSM import FSM

def readFSM(filename):
	"""This function reads a finite state machine from a file given the filename

	Parameter:
	filename - filename of fsm file

	File should be of the following format:
	first line contains q > 0 space separated strings representing Q (finite set 
	of states)
	second line contains s > 0 space separated characters representing S (finite
	set of stimuli)
	third line contains r > 0 space separated characters representing R (finite 
	set of stimuli)
	the next q lines contain s + 1 space separated strings:
	the first string is the name of the state (for the first such line, it is 
	the start state). This string may contain a colon (:) followed by a value,
	indicating it is the output for that state in this Moore Machine. It may 
	also be followed by an asterisk (*) indicating it is a final state for a
	finite state accepter
	the ith string represents the response to the (i - 1)th symbol in S. This 
	string may contain a colon(:) indicating the response from R assigned to 
	the particular transition

	Returns:
	fsm object represented by the file

	Raises:
	FileNotFoundError when the file is not there
	"""
	try:
		with open(filename,"r") as file:
			# truncate file extension
			dotIndex = filename.rfind(".")
			if dotIndex != -1:
				filename = filename[:dotIndex]
			
			# fsm takes name of file
			fsm = FSM(filename)
			autom = list(file)

			states = autom[0].split()
			q = {}

			# store states
			for i in states:
				q[i] = State(i)

				# add state to fsm
				fsm.addState(q[i])
			
			#store inputs and responses
			inputs = autom[1].split()
			responses = autom[2].split()

			# for each row in transition table
			for i in range(3,len(autom)):
				currLine = autom[i].split()
				if len(currLine) == 0:
					break
				# initialize parameters
				isFinal = False
				output = ""

				# if final state
				if currLine[0][0] == "*":
					currLine[0] = currLine[0][1:]
					isFinal = True
				
				# if moore machine
				if currLine[0].find(":") != -1:
					split = currLine[0].split(":")
					currLine[0] = split[0]
					output = split[1]

				currState = q[currLine[0]]

				# set parameters
				currState.isFinal = isFinal
				currState.output = output

				# if first state
				if i == 3:
					fsm.setStart(currState)

				# for each transition
				for j in range(1,len(currLine)):
					trans = currLine[j]
					currSymbol = inputs[j - 1]

					# assume moore machine
					output = ""
					if trans.find(":") != -1:
						split = trans.split(":")
						output = split[1]
						trans = split[0]

					currState.setTransition(currSymbol,q[trans])
					if output != "":
						currState.setOutput(output,currSymbol)
		return fsm
	except FileNotFoundError as e:
		raise e