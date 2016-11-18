class SHR(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		if index == len(list) - 1:
			list.append(0)
		else:
			index += 1
			
		return (list,index)
