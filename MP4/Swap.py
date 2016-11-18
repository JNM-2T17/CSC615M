class Swap(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		list[index],list[index + 1] = list[index + 1],list[index]
		return (list,index)
