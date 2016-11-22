class Command:
	def __init__(self,num,id,params=[]):
		self.num = num
		self.id = id
		self.params = params

	def do(self,list,index):
		raise NotImplementedError()

class SHL(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		for i in range(self.params[0]):
			if index == 0:
				list = [0] + list
			index -= 1
		return (list,index,self.num + 1)

	def __str__(self):
		return "shL %d" % (self.params[0])

class SHR(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		for i in range(self.params[0]):
			if index == len(list) - 1:
				list.append(0)
			index += 1
		return (list,index,self.num + 1)

	def __str__(self):
		return "shR %d" % (self.params[0])

class Add(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		list[index] = list[index] + list[index + 1]
		list[index + 1] = 0
		return (list,index,self.num + 1)

	def __str__(self):
		return "add"

class Const(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		list.append(self.params[0])
		return (list,index,self.num + 1)

	def __str__(self):
		return "const %d" % (self.params[0])

class Copy(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		if index - self.params[0] >= 0:
			if len(list) < index + 1:
				list.append(0)
			list[index] = list[index - self.params[0]]
			index += 1
			return (list,index,self.num + 1)
		else:
			return None

	def __str__(self):
		return "copy %d" % (self.params[0])

class Dec(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		list.append(list[index] - 1)
		index += 1
		return (list,index,self.num + 1)

	def __str__(self):
		return "dec"

class Inc(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		list.append(list[index] + 1)
		index += 1
		return (list,index,self.num + 1)

	def __str__(self):
		return "inc"

class Monus(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		list[index] = list[index] - list[index + 1]
		if list[index] < 0:
			list[index] = 0
		list[index + 1] = 0
		return (list,index,self.num + 1)

	def __str__(self):
		return "monus"

class Halt(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		return None

	def __str__(self):
		return "HALT"

class Move(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		list = list[0:index - self.params[0]] + list[index:]
		return (list,index,self.num + 1)

	def __str__(self):
		return "move %d, %d" % (self.params[0],self.params[1])

class Mult(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		list[index] = list[index] * list[index + 1]
		list[index + 1] = 0
		return (list,index,self.num + 1)

	def __str__(self):
		return "mult"

class PushL(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		list = list[0:index - 1] + list[index:]
		return (list,index,self.num + 1)

	def __str__(self):
		return "pushL"

class Swap(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		list[index],list[index + 1] = list[index + 1],list[index]
		return (list,index,self.num + 1)

	def __str__(self):
		return "swap"
