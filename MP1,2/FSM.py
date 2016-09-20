from State import *
import operator

class FSM:
	def __init__(self,name):
		self.name = name
		self.states = {}

	def addState(self,state):
		newName = self.name + "~" + state.name
		self.states[newName] = state
		state.name = newName

	def setStart(self,start):
		self.start = start

	def printEquivalence(self):
		for k,s1 in sorted(self.states.items(),key=operator.itemgetter(0)):
			for k,s2 in sorted(self.states.items(),key=operator.itemgetter(0),
								reverse=True):
				if s1 is not s2 and s1.isEquivalent(s2):
					print(s1.name[len(self.name) + 1:] + " ~ " + 
							s2.name[len(self.name) + 1:])
				elif s1 is s2:
					break

	def process(self,string,output=False,isMealy=False):
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
						return None
				state = nextState
			elif output:
				return None
			else:
				return False
		if output:
			return ret
		else:
			return state.isFinal

	def isEquivalent(self,fsm2):
		return self.start.isEquivalent(fsm2.start)

	def __str__(self):
		ret = self.name + "\n"
		for k,v in self.states.items():
			ret += v.__str__() + "\n"
		return ret