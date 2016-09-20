class State:
	def __init__(self,name,isFinal=False):
		self.name = name
		self.trans= {}
		self.outputs = {}
		self.direction = {}
		self.isFinal = isFinal

	def setTransition(self,input,target,output,direction):
		self.trans[input] = target
		self.outputs[input] = output
		self.direction[input] = direction if direction >= -1 or direction <= 1 else 1

	def getNextState(self,input):
		if input in self.trans:
			return (self.trans[input],self.outputs[input],self.direction[input])
		else:
			return None

	def __str__(self):
		return self.name