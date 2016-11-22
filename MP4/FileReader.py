from TuringMachine import *
from Command import *

def readFile(filename):
	with open(filename,"r") as file:
		# truncate file extension
		dotIndex = filename.rfind(".")
		if dotIndex != -1:
			filename = filename[:dotIndex]

		tm = TuringMachine(filename)
		first = True

		for line in file:
			split = line.split(",")
			id = int(split[0])
			name = split[1]
			command = None

			if name[-1] == "\n":
				name = name[:-1]

			# print("%d - %s" % (id,name))

			if name == "shL":
				count = int(split[2])
				command = SHL(id,name,[count])
			elif name == "shR":
				count = int(split[2])
				command = SHR(id,name,[count])
			elif name == "copy":
				count = int(split[2])
				command = Copy(id,name,[count])
			elif name == "const":
				count = int(split[2])
				command = Const(id,name,[count])
			elif name == "move":
				count1 = int(split[2])
				count2 = int(split[3])
				command = Move(id,name,[count])
			elif name == "pushL":
				command = PushL(id,name,[])
			elif name == "inc":
				command = Inc(id,name,[])
			elif name == "dec":
				command = Dec(id,name,[])
			elif name == "add":
				command = Add(id,name,[])
			elif name == "mult":
				command = Mult(id,name,[])
			elif name == "monus":
				command = Monus(id,name,[])
			elif name == "swap":
				command = Swap(id,name,[])
			elif name == "HALT":
				command = Halt(id,name,[])

			if command is not None:
				tm.addCommand(id,command)
				if first:
					tm.setStart(command)
					first = False

		return tm
