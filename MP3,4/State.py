"""This file is the model for a state in a Turing machine.

Author: Ryan Austin Fernandez
Date Last Edited: 09/21/2016
"""
class State:
	"""This class models a state in a Turing machine."""
	
	def __init__(self,name,isFinal=False):
		"""constructs a basic state

		Parameters:
		name - name of state
		isFinal - whether this state is accepting or not
		"""
		self.name = name
		self.trans= {}
		self.outputs = {}
		self.direction = {}
		self.isFinal = isFinal

	def setTransition(self,input,target,output,direction):
		"""sets a transition of this state

		Parameters:
		input - input symbol
		target - target state
		output - output symbol
		direction - -1 if left, 0 if stay, 1 if right
		"""
		self.trans[input] = target
		self.outputs[input] = output
		self.direction[input] = direction if direction >= -1 and direction <= 1 else 1

	def getNextState(self,input):
		"""gets the transition information on the given input

		Parameter:
		input - input symbol

		Returns:
		tuple containing (q,t,d) where q is the new state, t is the tape symbol
		to write, and d is the direction of the tape head
		"""
		if input in self.trans:
			return (self.trans[input],self.outputs[input],self.direction[input])
		else:
			return None

	def __str__(self):
		"""returns a string representing this state's transition"""
		ret = self.name + "\n"
		for k in self.trans.keys():
			ret += "d(%s,%s) = (%s,%s,%s)\n" \
					% (self.name,k,self.trans[k].name,self.outputs[k],
						"L" if self.direction[k] == -1 else 
						("R" if self.direction[k] == 1 else "S"))
		return ret