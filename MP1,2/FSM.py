"""This file is the model for a finite state machine.

Author: Ryan Austin Fernandez
Date Last Edited: 09/21/2016
"""
from State import *
import operator

class FSM:
	"""This class models a finite state machine"""
	
	def __init__(self,name):
		"""constructs a basic FSM

		Parameter:
		name - name of fsm
		"""
		self.name = name
		self.states = {}
		self.groups = []

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

	def computeEquivalence(self):
		"""computes the equivalences between the states of this FSM and stores 
		the groups in self.groups as multiple lists with multiple equivalent 
		states each"""
		done = {}
		self.groups = []
		for s1 in self.states.values():
			if s1.name not in done:
				newGroup = [s1]
				done[s1.name] = True
				for s2 in self.states.values():
					if s2.name not in done and s1.isEquivalent(s2):
						newGroup.append(s2)
						done[s2.name] = True
				self.groups.append(newGroup)

	def printEquivalence(self,fsm2=None):
		"""prints the equivalent states of this FSM within itself or with 
		another FSM

		Parameter:
		fsm2 - FSM to compare this FSM's states to. Default to None if user 
		only wishes to print this FSM's internal equivalent states
		"""
		# compute groups
		self.computeEquivalence()

		# if no FSM to compare to
		if fsm2 is None:
			i = 1
			for grp in self.groups:
				if len(grp) > 1:
					print("Equivalent Group %d: " % (i),end="")
					start = True
					for s in sorted(grp,key=operator.attrgetter("name")):
						if not start:
							print(",",end="")
						print(s.name[len(self.name) + 1:],end="")
						start = False
					i += 1
					print()
			if i == 1:
				print("No equivalent states.")
		
		# if comparing with an FSM
		else:
			fsm2.computeEquivalence()
			i = 1
			# print(len(self.groups),"vs",len(fsm2.groups))
			maxLen = max([len(self.name),len(fsm2.name)])
			for grp1 in self.groups:
				for grp2 in fsm2.groups:
					if grp1[0].isEquivalent(grp2[0]):
						print("Equivalent Group %d:\n    From %s: " % 
								(i,self.name.rjust(maxLen)),end="")
						first = True
						for s in sorted(grp1,key=operator.attrgetter("name")):
							if not first:
								print(",",end="")
							print(s.name[len(self.name) + 1:],end="")
							first = False
						print(
							"\n    From %s: " 
							% (fsm2.name.rjust(maxLen)),end=""
						)
						first = True
						for s in sorted(grp2,key=operator.attrgetter("name")):
							if not first:
								print(",",end="")
							print(s.name[len(fsm2.name) + 1:],end="")
							first = False
						i += 1
						print()
						

	def process(self,string,output=False,isMealy=False):
		"""processes a string using this FSM's definition
		
		Parameters:
		string - string to process
		output - whether to produce an output or not; default to False
		isMealy - whether the output is to be extracted from the transitions or 
		not; default to False

		Return:
		Output string if output is True, True/False if output is False
		"""
		state = self.start		
		ret = ""
		for i in range(len(string)):
			nextState = state.getNextState(string[i])
			if nextState is not None:
				if output:
					output = state.getOutput(string[i] if isMealy else None)
					if output is not None:
						ret += output
					else:
						return ret
				state = nextState
			elif output:
				return ret
			else:
				return False
		if output:
			return ret
		else:
			return state.isFinal

	def __eq__(self,fsm2):
		"""checks if two FSM's are equivalent

		Parameter:
		fsm2 - FSM to compare with

		Returns:
		True if the two are equivalent and False otherwise
		"""
		return self.start.isEquivalent(fsm2.start)

	def __str__(self):
		"""returns the string representation of this FSM"""
		ret = self.name + "\n"
		for k,v in self.states.items():
			ret += v.__str__() + "\n"
		return ret