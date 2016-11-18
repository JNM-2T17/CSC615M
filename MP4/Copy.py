class Copy(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		if index - params[0] >= 0:
			list.append(list[index - params[0]])
			index = len(list) - 1
			return (list,index)
		else:
			return None
