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

			if name.lower() == "shl":
				count = int(split[2])
				command = SHL(id,name,[count])
			elif name.lower() == "shr":
				count = int(split[2])
				command = SHR(id,name,[count])
			elif name.lower() == "copy":
				count = int(split[2])
				command = Copy(id,name,[count])
			elif name.lower() == "const":
				count = int(split[2])
				command = Const(id,name,[count])
			elif name.lower() == "move":
				count1 = int(split[2])
				count2 = int(split[3])
				command = Move(id,name,[count1,count2])
			elif name.lower() == "pushl":
				command = PushL(id,name,[])
			elif name.lower() == "inc":
				command = Inc(id,name,[])
			elif name.lower() == "dec":
				command = Dec(id,name,[])
			elif name.lower() == "add":
				command = Add(id,name,[])
			elif name.lower() == "mult":
				command = Mult(id,name,[])
			elif name.lower() == "monus":
				command = Monus(id,name,[])
			elif name.lower() == "swap":
				command = Swap(id,name,[])
			elif name.lower() == "halt":
				command = Halt(id,name,[])
			elif name.lower() == "goto":
				count = int(split[2])
				command = Goto(id,name,[count])
			elif name.lower() == "gotoeq":
				count = int(split[2])
				command = GotoEQ(id,name,[count])
			elif name.lower() == "gotone":
				count = int(split[2])
				command = GotoNE(id,name,[count])
			elif name.lower() == "gotoge":
				count = int(split[2])
				command = GotoGE(id,name,[count])
			elif name.lower() == "gotogt":
				count = int(split[2])
				command = GotoGT(id,name,[count])
			elif name.lower() == "gotole":
				count = int(split[2])
				command = GotoLE(id,name,[count])
			elif name.lower() == "gotolt":
				count = int(split[2])
				command = GotoLT(id,name,[count])

			# print("%d - %s" % (id,command.__str__()))

			if command is not None:
				tm.addCommand(id,command)
				if first:
					tm.setStart(command)
					first = False

		return tm
