"""This file is the model for a state in a finite state machine.

Author: Ryan Austin Fernandez
Date Last Edited: 09/21/2016
"""
class State:
	"""This class models a state in a finite state machine."""
	
	def __init__(self,name,isFinal=False,output=""):
		"""constructs a basic state

		Parameters:
		name - name of state
		isFinal - whether this state is accepting or not
		output - output of this state in a Moore machine
		"""
		self.name = name
		self.trans= {}
		self.output = output
		self.outputs = {}
		self.isFinal = isFinal

	def setOutput(self,output,input=None):
		"""sets an output of this state

		Parameters:
		output - output symbol
		input - input symbol, if None, sets output as Moore machine output
		"""
		if input is None:
			self.output = output
		else:
			self.outputs[input] = output

	def setTransition(self,input,target):
		"""sets a transition of this state

		Parameters:
		input - input symbol
		target - target state
		"""
		self.trans[input] = target

	def getOutput(self,input=None):
		"""gets the output of this state
		
		Parameter:
		input - input on which to base the output, if None, return Moore machine
		output
		"""
		if input is None:
			return self.output
		elif input in self.outputs:
			return self.outputs[input]
		else:
			return None

	def getNextState(self,input):
		"""gets the transition information on the given input

		Parameter:
		input - input symbol

		Returns:
		next state
		"""
		if input in self.trans:
			return self.trans[input]
		else:
			return None

	def _checkEquiv(self,s2,v1,v2):
		"""checks equivalence of two states recursively

		Parameters:
		s2 - state to compare to
		v1,v2 - list of visited states
		"""
		# print(self.name,"vs",s2.name)
		if self.name < s2.name:
			# print(self.name," vs ",s2.name)
			v1.append(self)
			v2.append(s2)
		elif self.name > s2.name:
			# print(s2.name," vs ",self.name)
			v1.append(s2)
			v2.append(self)
		else:
			# print(self.name," vs ",s2.name)
			return True

		if self.isFinal != s2.isFinal:
			return False

		# print(self.output,"vs",s2.output)
		if self.output != s2.output:
			# print("g(%s) = %s != g(%s) = %s" % \
			# 		(self.name,moore1,s2.name,moore2))
			# print("%s is not equivalent to %s" % (self.name,s2.name))
			return False

		for k,v in self.trans.items():
			t1 = v
			t2 = s2.getNextState(k)

			if t1.name > t2.name:
				temp = t1
				t1 = t2
				t2 = temp

			found = False
			for i in range(len(v1)):
				if t1 == v1[i] and t2 == v2[i]:
					found = True
			mealy1 = self.getOutput(k)
			mealy2 = s2.getOutput(k)
			if mealy1 != mealy2:
				# print("g(%s,%s) = %s != g(%s,%s) = %s" % \
				# 		(self.name,k,mealy1,s2.name,k,mealy2))
				# print("%s is not equivalent to %s" % (self.name,s2.name))
				return False
			if not found and not t1._checkEquiv(t2,v1,v2):
					# print("%s is not equivalent to %s" % (self.name,s2.name))
					return False

		return True

	def isEquivalent(self,s2):
		"""returns whether this state is equivalent to another state

		Parameter:
		s2 - state to compare to
		"""
		return self._checkEquiv(s2,[],[])

	def __str__(self):
		"""returns string representation of this state"""
		ret = self.name + "\n";
		if self.output != "":
			ret += "h(" + self.name + ") = " + self.output + "\n"
		for k,v in self.trans.items():
			ret += "f(%s,%s) = %s\n" % (self.name,k,v.name)
		for k,v in self.outputs.items():
			ret += "g(%s,%s) = %s\n" % (self.name,k,v)

		return ret