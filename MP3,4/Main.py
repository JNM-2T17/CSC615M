from TuringMachine import *

add1 = TuringMachine("Add 1")

add1sA = State("A")
add1sB = State("B")
add1sC = State("C")
add1sD = State("D")

add1sA.setTransition("0",add1sA,"0",1)
add1sA.setTransition("1",add1sA,"1",1)
add1sA.setTransition("B",add1sB,"B",-1)
add1sB.setTransition("0",add1sC,"1",-1)
add1sB.setTransition("1",add1sB,"0",-1)
add1sB.setTransition("B",add1sC,"1",-1)
add1sC.setTransition("0",add1sC,"0",-1)
add1sC.setTransition("1",add1sC,"1",-1)

add1.addState(add1sA)
add1.addState(add1sB)
add1.addState(add1sC)
add1.addState(add1sD)
add1.setStart(add1sA)

print(add1)
print(add1.process("111111"))
print(add1.process("110111"))


ww = TuringMachine("WW")

wwsA = State("A")
wwsB = State("B")
wwsB1 = State("B1")
wwsC = State("C")
wwsD = State("D")
wwsE = State("E")
wwsF = State("F")
wwsG = State("G")
wwsH = State("H")
wwsI = State("I")
wwsJ = State("J",True)

wwsA.setTransition("0",wwsB,"X",1)
wwsA.setTransition("1",wwsB,"Y",1)
wwsA.setTransition("S",wwsE,"S",-1)
wwsA.setTransition("T",wwsE,"T",-1)
wwsB.setTransition("0",wwsB1,"0",1)
wwsB.setTransition("1",wwsB1,"1",1)
wwsB1.setTransition("0",wwsB1,"0",1)
wwsB1.setTransition("1",wwsB1,"1",1)
wwsB1.setTransition("B",wwsC,"B",-1)
wwsB1.setTransition("S",wwsC,"S",-1)
wwsB1.setTransition("T",wwsC,"T",-1)
wwsC.setTransition("0",wwsD,"S",-1)
wwsC.setTransition("1",wwsD,"T",-1)
wwsD.setTransition("0",wwsD,"0",-1)
wwsD.setTransition("1",wwsD,"1",-1)
wwsD.setTransition("X",wwsA,"X",1)
wwsD.setTransition("Y",wwsA,"Y",1)
wwsE.setTransition("X",wwsE,"X",-1)
wwsE.setTransition("Y",wwsE,"Y",-1)
wwsE.setTransition("B",wwsF,"B",1)
wwsF.setTransition("C",wwsJ,"C",1)
wwsF.setTransition("X",wwsG,"D",1)
wwsF.setTransition("Y",wwsI,"D",1)
wwsG.setTransition("X",wwsG,"X",1)
wwsG.setTransition("Y",wwsG,"Y",1)
wwsG.setTransition("C",wwsG,"C",1)
wwsG.setTransition("S",wwsH,"C",-1)
wwsH.setTransition("C",wwsH,"C",-1)
wwsH.setTransition("X",wwsH,"X",-1)
wwsH.setTransition("Y",wwsH,"Y",-1)
wwsH.setTransition("D",wwsF,"D",1)
wwsI.setTransition("X",wwsI,"X",1)
wwsI.setTransition("Y",wwsI,"Y",1)
wwsI.setTransition("C",wwsI,"C",1)
wwsI.setTransition("T",wwsH,"C",-1)

ww.addState(wwsA)
ww.addState(wwsB)
ww.addState(wwsB1)
ww.addState(wwsC)
ww.addState(wwsD)
ww.addState(wwsE)
ww.addState(wwsF)
ww.addState(wwsG)
ww.addState(wwsH)
ww.addState(wwsI)
ww.addState(wwsJ)

ww.setStart(wwsA)

print(ww)

print(ww.process("00100010"))
print(ww.process("001010010"))
print(ww.process("001010010001010010"))
print(ww.process("001011010001010010"))


ww2 = TuringMachine("WW2")

ww2sA = State("A")
ww2sB = State("B")
ww2sB1 = State("B1")
ww2sC = State("C")
ww2sD = State("D")

ww2sA.setTransition("0",ww2sB,"X",1)
ww2sA.setTransition("1",ww2sB,"Y",1)
ww2sB.setTransition("0",ww2sB1,"0",1)
ww2sB.setTransition("1",ww2sB1,"1",1)
ww2sB1.setTransition("0",ww2sB1,"0",1)
ww2sB1.setTransition("1",ww2sB1,"1",1)
ww2sB1.setTransition("B",ww2sC,"B",-1)
ww2sB1.setTransition("S",ww2sC,"S",-1)
ww2sB1.setTransition("T",ww2sC,"T",-1)
ww2sC.setTransition("0",ww2sD,"S",-1)
ww2sC.setTransition("1",ww2sD,"T",-1)
ww2sD.setTransition("0",ww2sD,"0",-1)
ww2sD.setTransition("1",ww2sD,"1",-1)
ww2sD.setTransition("X",ww2sA,"X",1)
ww2sD.setTransition("Y",ww2sA,"Y",1)

ww2.addState(ww2sA)
ww2.addState(ww2sB)
ww2.addState(ww2sB1)
ww2.addState(ww2sC)
ww2.addState(ww2sD)

ww2.setStart(ww2sA)

ww3 = TuringMachine("WW3")

ww3sStart = State("Start")
ww3sE = State("E")
ww3sF = State("F")
ww3sG = State("G")
ww3sH = State("H")
ww3sI = State("I")
ww3sJ = State("J",True)

ww3sStart.setTransition("S",ww3sE,"S",-1)
ww3sStart.setTransition("T",ww3sE,"T",-1)
ww3sE.setTransition("X",ww3sE,"X",-1)
ww3sE.setTransition("Y",ww3sE,"Y",-1)
ww3sE.setTransition("B",ww3sF,"B",1)
ww3sF.setTransition("C",ww3sJ,"C",1)
ww3sF.setTransition("X",ww3sG,"D",1)
ww3sF.setTransition("Y",ww3sI,"D",1)
ww3sG.setTransition("X",ww3sG,"X",1)
ww3sG.setTransition("Y",ww3sG,"Y",1)
ww3sG.setTransition("C",ww3sG,"C",1)
ww3sG.setTransition("S",ww3sH,"C",-1)
ww3sH.setTransition("C",ww3sH,"C",-1)
ww3sH.setTransition("X",ww3sH,"X",-1)
ww3sH.setTransition("Y",ww3sH,"Y",-1)
ww3sH.setTransition("D",ww3sF,"D",1)
ww3sI.setTransition("X",ww3sI,"X",1)
ww3sI.setTransition("Y",ww3sI,"Y",1)
ww3sI.setTransition("C",ww3sI,"C",1)
ww3sI.setTransition("T",ww3sH,"C",-1)

ww3.addState(ww3sE)
ww3.addState(ww3sF)
ww3.addState(ww3sG)
ww3.addState(ww3sH)
ww3.addState(ww3sI)
ww3.addState(ww3sJ)

ww3.setStart(ww3sStart)

ww2.combine(ww3)

print(ww3)
print(ww2.process("00100010"))
print(ww2.process("001010010"))
print(ww2.process("001010010001010010"))
print(ww2.process("001011010001010010"))

