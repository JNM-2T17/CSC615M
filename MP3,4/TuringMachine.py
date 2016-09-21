"""This file is the model for a Turing Machine.

Author: Ryan Austin Fernandez
Date Last Edited: 09/21/2016
"""
from State import State
from operator import attrgetter

class TuringMachine:
	"""This class models a Turing machine."""

	def __init__(self,name,blank="B"):
		"""constructs a basic FSM

		Parameters:
		name - name of fsm
		blank - blank symbol to use; default is B
		"""
		self.name = name
		self.states = {}
		self.blank = "B"
		self.defaultNext = []
		self.nextTM = {}

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

	def cleanString(self,string):
		"""cleans the tape string passed

		Parameter:
		string - tape string to clean

		Return:
		new string with blank symbols stripped from both ends
		"""
		i = 0
		while i < len(string) and string[i] == self.blank:
			i += 1
		string = string[i:]
		i = len(string) - 1
		while i >= 0 and string[i] == self.blank:
			i -= 1
		string = string[:i + 1]	
		return string

	def process(self,string):
		"""processes a string using this TM's definition
		
		Parameter:
		string - string to process

		Return:
		Tuple containing(A,S) where A is True/False depending on whether the 
		string is accepted or not and S is the contents of the tape
		"""
		state = self.start
		i = 0
		fallback = 0
		if len(string) == 0:
			string = self.blank
		while True:
			transition = state.getNextState(string[i])
			if transition is not None:
				state = transition[0]
				# print(state,transition[1:],string)
				string = string[0:i] + transition[1] + \
							(string[i + 1:] if i + 1 < len(string) else "")
				i += transition[2]
				if i < 0:
					string = self.blank + string
					i = 0
				elif i >= len(string):
					string += self.blank
			elif fallback < len(self.defaultNext):
				state = self.defaultNext[fallback]
				fallback += 1
			else:				
				return (state.isFinal,self.cleanString(string))

		return (state.isFinal,self.cleanString(string))

	def combine(self,tm2,symbol=None):
		"""combines this TM with another

		Parameter:
		tm2 - TM to combine with
		symbol - symbol to transition from this machine to new machine; if None,
		all halts are transferred to tm2
		"""
		if symbol == None:
			self.defaultNext.append(tm2.start)
		else:
			for k,v in self.states.items():
				if v.getTransition(symbol) == None:
					v.setTransition(symbol,tm2.start,symbol,0)

		for k,v in tm2.states.items():
			self.addState(v)

	def __str__(self):
		ret = self.name + "\n\n"
		for v in sorted(self.states.values(),key=attrgetter("name")):
			ret += v.__str__() + "\n"
		return ret