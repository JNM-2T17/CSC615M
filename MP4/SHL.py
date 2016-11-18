class SHL(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		if index == 0:
			list = [0] + list
		else:
			index -= 1
			
		return (list,index)
