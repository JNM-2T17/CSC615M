from State import State
from TWA import TWA

def readFile(filename):
	with open(filename,"r") as file:
		# truncate file extension
		dotIndex = filename.rfind(".")
		if dotIndex != -1:
			filename = filename[:dotIndex]

		twa = TWA(filename)

		for line in file:
			if len(line) > 0:
				parts = line.split(",")
				temp = twa.getState(parts[0])
				if temp is None:
					temp = State(parts[0])
					if parts[0] == "start":
						twa.setStart(temp)
					elif parts[0] == "accept":
						temp.isFinal = True
					twa.addState(temp)
				
				if parts[1] == "scanleft":
					# print("Changing %s's direction to left." % (temp.name))
					temp.direction = State.LEFT
				elif parts[1] == "scanright":
					# print("Changing %s's direction to left." % (temp.name))
					temp.direction = State.RIGHT

				symbol = parts[2]

				if parts[3][-1] == "\n":
					parts[3] = parts[3][:-1]
				nextState = twa.getState(parts[3])
				if nextState is None:
					nextState = State(parts[3])
					if parts[3] == "start":
						twa.setStart(nextState)
					elif parts[3] == "accept":
						nextState.isFinal = True
					twa.addState(nextState)

				temp.setTransition(symbol,nextState)
		return twa




