from State import *

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

	def process(self,string,output=False,isMealy=False):
		state = self.start		
		ret = ""
		for i in range(len(string)):
			nextState = state.getNextState(string[i])
			if nextState != None:
				if output:
					output = state.getOutput(string[i] if isMealy else None)
					if output != None:
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