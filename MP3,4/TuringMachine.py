from State import *

class TuringMachine:
	def __init__(self,name,blank="B"):
		self.name = name
		self.states = {}
		self.blank = "B"

	def addState(self,state):
		newName = self.name + "~" + state.name
		self.states[newName] = state
		state.name = newName

	def setStart(self,start):
		self.start = start

	def setBlank(self,blank):
		self.blank = blank[0]

	def cleanString(self,string):
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
		state = self.start
		i = 0
		if len(string) == 0:
			string = self.blank
		while True:
			transition = state.getNextState(string[i])
			if transition != None:
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
			else:				
				return (state.isFinal,self.cleanString(string))

		return (state.isFinal,self.cleanString(string))