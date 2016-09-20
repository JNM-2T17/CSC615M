from State import *
from FSM import *

while True:
	fsm = [None] * 2
	for ctr in range(2):
		ok = False
		while not ok:
			filename = input("Enter filename for machine %d:" % (ctr + 1))
			try:
				file = open(filename,"r")
				ok = True
				dotIndex = filename.rfind(".")
				if dotIndex != -1:
					filename = filename[:dotIndex]
				# fsm takes name of file
				fsm[ctr] = FSM(filename)
				autom = file.read().split("\n")

				# print(autom)
				states = autom[0].split()
				q = {}

				# store states
				for i in states:
					q[i] = State(i)

					# add state to fsm
					fsm[ctr].addState(q[i])
				
				#store inputs and responses
				inputs = autom[1].split()
				responses = autom[2].split()

				# for each row in transition table
				for i in range(3,len(autom)):
					currLine = autom[i].split()
					if len(currLine) == 0:
						break
					# initialize parameters
					isFinal = False
					output = ""

					# if final state
					if currLine[0][0] == "*":
						currLine[0] = currLine[0][1:]
						isFinal = True
					
					# if moore machine
					if currLine[0].find(":") != -1:
						split = currLine[0].split(":")
						currLine[0] = split[0]
						output = split[1]

					currState = q[currLine[0]]

					# set parameters
					currState.isFinal = isFinal
					currState.output = output

					# if first state
					if i == 3:
						fsm[ctr].setStart(currState)

					# for each transition
					for j in range(1,len(currLine)):
						trans = currLine[j]
						currSymbol = inputs[j - 1]

						# assume moore machine
						output = ""
						if trans.find(":") != -1:
							split = trans.split(":")
							output = split[1]
							trans = split[0]

						currState.setTransition(currSymbol,q[trans])
						if output != "":
							currState.setOutput(output,currSymbol)

				file.close()
			except FileNotFoundError:
				print("File not found.")

	if fsm[0].isEquivalent(fsm[1]):
		print(fsm[0].name,"and",fsm[1].name,"are equivalent.")
		for s1 in fsm[0].states.values():
			for s2 in fsm[1].states.values():
				if s1.isEquivalent(s2):
					print(s1.name[len(fsm[0].name) + 1:],"~",s2.name[len(fsm[1].name) + 1:])
	else:
		print(fsm[0].name,"and",fsm[1].name,"are not equivalent.")