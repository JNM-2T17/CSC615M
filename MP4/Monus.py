class Monus(Command):
	def __init__(self,num,id,params=[]):
		super().__init__(num,id,params)

	def do(self,list,index):
		list[index] = list[index] - list[index + 1]
		if list[index] < 0:
			list[index] = 0
		list[index + 1] = 0
		return (list,index)
