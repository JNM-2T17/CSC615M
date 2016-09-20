class State:
	def __init__(self,name,isFinal=False,output=""):
		self.name = name
		self.trans= {}
		self.output = output
		self.outputs = {}
		self.isFinal = isFinal

	def setOutput(self,output,input=None):
		if input is None:
			self.output = output
		else:
			self.outputs[input] = output

	def setTransition(self,input,target):
		self.trans[input] = target

	def getOutput(self,input=None):
		if input is None:
			return self.output
		elif input in self.outputs:
			return self.outputs[input]
		else:
			return None

	def getNextState(self,input):
		if input in self.trans:
			return self.trans[input]
		else:
			return None

	def checkEquiv(self,s2,v1,v2):
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

			if not found:
				mealy1 = self.getOutput(k)
				mealy2 = s2.getOutput(k)
				if mealy1 != mealy2:
					# print("g(%s,%s) = %s != g(%s,%s) = %s" % \
					# 		(self.name,k,mealy1,s2.name,k,mealy2))
					# print("%s is not equivalent to %s" % (self.name,s2.name))
					return False
				elif not t1.checkEquiv(t2,v1,v2):
					# print("%s is not equivalent to %s" % (self.name,s2.name))
					return False

		return True

	def isEquivalent(self,s2):
		return self.checkEquiv(s2,[],[])

	def __str__(self):
		ret = self.name + "\n";
		if self.output != "":
			ret += "h(" + self.name + ") = " + self.output + "\n"
		for k,v in self.trans.items():
			ret += "f(%s,%s) = %s\n" % (self.name,k,v.name)
		for k,v in self.outputs.items():
			ret += "g(%s,%s) = %s\n" % (self.name,k,v)

		return ret