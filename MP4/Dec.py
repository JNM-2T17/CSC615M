class Dec(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		list.append(list[index] - 1)
		index += 1
		return (list,index)
