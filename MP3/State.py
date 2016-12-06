"""This file is the model for a state in a Turing machine.

Author: Ryan Austin Fernandez
Date Last Edited: 09/21/2016
"""
class State:
	"""This class models a state in a Turing machine."""

	LEFT = -1
	RIGHT = 1
	
	def __init__(self,name,direction=RIGHT,isFinal=False):
		"""constructs a basic state

		Parameters:
		name - name of state
		isFinal - whether this state is accepting or not
		"""
		self.name = name
		self.trans= {}
		# self.outputs = {}
		self.direction = direction
		self.isFinal = isFinal

	# def setTransition(self,input,target,output,direction):
	def setTransition(self,input,target):
		"""sets a transition of this state

		Parameters:
		input - input symbol
		target - target state
		direction - -1 if left, 1 if right
		"""
		self.trans[input] = target
		# self.outputs[input] = output
		# self.direction[input] = direction if direction >= -1 and direction <= 1 else 1

	def getNextState(self,input):
		"""gets the transition information on the given input

		Parameter:
		input - input symbol

		Returns:
		tuple containing (q,d) where q is the new state and d is the direction 
		of the tape head
		"""
		if input in self.trans:
			return self.trans[input]
		else:
			return None

	def __str__(self):
		"""returns a string representing this state's transition"""
		ret = self.name + "\n%s\n" % ("SL" if self.direction == State.LEFT else "SR")
		for k in self.trans.keys():
			ret += "d(%s,%s) = (%s)\n" % (self.name,k,self.trans[k].name)
		return ret