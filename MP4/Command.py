class Command:
	def __init__(self,num,id,params=[]):
		self.num = num
		self.id = id
		self.params = params

	def do(self,list,index):
		raise NotImplementedError()