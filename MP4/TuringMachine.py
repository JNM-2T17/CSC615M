class TuringMachine:
	def __init__(self,name):
		self.name = name
		self.commands = {}

	def addCommand(self,id,command):
		self.commands[id] = command

	def setStart(self,start):
		self.start = start

	def _printStats(self):
		# print(self.list)
		# print(self.index)

		str1 = ""
		str2 = ""
		
		for i in range(len(self.list)):
			str1 += "#"
			if i != self.index:
				str2 += " "
			else:
				str2 += "^"
			for j in range(self.list[i]):
				str1 += "1"
				str2 += " "
		str1 += "#"
		if self.index == len(self.list):
			str2 += "^"
		print(str1 + "\n" + str2)

	def run(self,input):
		curr = self.start
		self.index = 0

		self.list = input

		print("START")
		self._printStats()

		while curr is not None:
			ret = curr.do(self.list,self.index)
			print("After " + curr.id)
			if ret is None:
				curr = None
			else:
				self.list = ret[0]
				self.index = ret[1]
				curr = self.commands[ret[2]]
			self._printStats()
			

