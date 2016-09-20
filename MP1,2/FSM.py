from State import *
import operator

class FSM:
	def __init__(self,name):
		self.name = name
		self.states = {}
		self.groups = []

	def addState(self,state):
		newName = self.name + "~" + state.name
		self.states[newName] = state
		state.name = newName

	def setStart(self,start):
		self.start = start

	def computeEquivalence(self):
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
		self.computeEquivalence()
		if fsm2 is None:
			i = 1
			for grp in self.groups:
				if len(grp) > 1:
					print("Equivalent Group %d: " % (i),end="")
					start = True
					for s in grp:
						if not start:
							print(",",end="")
						print(s.name[len(self.name) + 1:],end="")
						start = False
					i += 1
					print()
			if i == 1:
				print("No equivalent states.")
		else:
			fsm2.computeEquivalence()
			i = 1
			# print(len(self.groups),"vs",len(fsm2.groups))
			for grp1 in self.groups:
				for grp2 in fsm2.groups:
					if grp1[0].isEquivalent(grp2[0]):
						print("Equivalent Group %d:\n    From %15s: " % 
								(i,self.name),end="")
						first = True
						for s in grp1:
							if not first:
								print(",",end="")
							print(s.name[len(self.name) + 1:],end="")
							first = False
						print("\n    From %15s: " % (fsm2.name),end="")
						first = True
						for s in grp2:
							if not first:
								print(",",end="")
							print(s.name[len(fsm2.name) + 1:],end="")
							first = False
						i += 1
						print()
						

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