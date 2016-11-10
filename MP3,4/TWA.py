"""This file is the model for a Turing Machine.

Author: Ryan Austin Fernandez
Date Last Edited: 09/21/2016
"""
from State import State
from operator import attrgetter

class TWA:
	"""This class models a Turing machine."""

	def __init__(self,name,blank="#"):
		"""constructs a basic FSM

		Parameters:
		name - name of fsm
		blank - blank symbol to use; default is B
		"""
		self.name = name
		self.states = {}
		self.blank = "#"
		self.defaultNext = []
		self.nextTWA = {}

	def addState(self,state):
		"""adds a state to this FSM

		Parameter:
		state - state to be added to this FSM
		"""
		newName = self.name + "~" + state.name
		self.states[newName] = state
		state.name = newName

	def setStart(self,start):
		"""sets a start state for this FSM

		Parameter:
		start - state to set as start state
		"""
		self.start = start

	def getState(self,name):
		"""returns the state with the specified name

		Parameter:
		name - name of state to return
		"""
		return (self.states[self.name + "~" + name] 
			if (self.name + "~" + name) in self.states else None)

	# def cleanString(self,string):
	# 	"""cleans the tape string passed

	# 	Parameter:
	# 	string - tape string to clean

	# 	Return:
	# 	new string with blank symbols stripped from both ends
	# 	"""
	# 	i = 0
	# 	while i < len(string) and string[i] == self.blank:
	# 		i += 1
	# 	string = string[i:]
	# 	i = len(string) - 1
	# 	while i >= 0 and string[i] == self.blank:
	# 		i -= 1
	# 	string = string[:i + 1]	
	# 	return string

	def process(self,string):
		"""processes a string using this TWA's definition
		
		Parameter:
		string - string to process

		Return:
		Tuple containing(A,S) where A is True/False depending on whether the 
		string is accepted or not and S is the contents of the tape
		"""
		state = self.start
		i = 0
		fallback = 0
		string = "#%s#" % string
		halting = False
		# print(state.name)
		# print(state.direction)
		while not halting:
			# print(string)
			# for j in range(len(string)):
				# if j == i:
					# print("^",end="")
				# else:
					# print(" ",end="")
			if state.direction == State.LEFT:
				if i == 0:
					string = "#" + string
					i = 1
				nextState = state.getNextState(string[i - 1])
				if nextState is not None:
					state = nextState
					i -= 1
				else:
					halting = True
			else:
				if i == len(string) - 1:
					string = string + "#"
				nextState = state.getNextState(string[i + 1])
				if nextState is not None:
					state = nextState
					i += 1
				else:
					halting = True
			# print("")
			# print(state.name)
			# print(state.direction)
			
		return state.isFinal

	# def combine(self,TWA2,symbol=None):
	# 	"""combines this TWA with another

	# 	Parameter:
	# 	TWA2 - TWA to combine with
	# 	symbol - symbol to transition from this machine to new machine; if None,
	# 	all halts are transferred to TWA2
	# 	"""
	# 	if symbol == None:
	# 		self.defaultNext.append(TWA2.start)
	# 	else:
	# 		for k,v in self.states.items():
	# 			if v.getTransition(symbol) == None:
	# 				v.setTransition(symbol,TWA2.start,symbol,0)

	# 	for k,v in TWA2.states.items():
	# 		self.addState(v)

	def __str__(self):
		"""returns string representation of this state"""
		ret = self.name + "\n\n"
		for v in sorted(self.states.values(),key=attrgetter("name")):
			ret += v.__str__() + "\n"
		return ret