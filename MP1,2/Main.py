from State import *
from FSM import *

m1 = FSM("Odd1");
m2 = FSM("Odd2");

m1s1 = State("A");
m1s2 = State("B",True);
m1s1.setTransition("0",m1s2);
m1s2.setTransition("0",m1s1);

m1.addState(m1s1);
m1.addState(m1s2);
m1.setStart(m1s1);

m2s1 = State("A");
m2s2 = State("B",True);
m2s1.setTransition("0",m2s2);
m2s2.setTransition("0",m2s1);

m2.addState(m2s1);
m2.addState(m2s2);
m2.setStart(m2s1);

print(m1.isEquivalent(m2));

consec1 = FSM("Consec1");

c1A = State("c1A",output="A");
c1B = State("c1B",output="A");
c1C = State("c1C",output="A");
c1D = State("c1D",output="B");

c1A.setTransition("0",c1B);
c1A.setTransition("1",c1C);
c1B.setTransition("0",c1D);
c1B.setTransition("1",c1C);
c1C.setTransition("0",c1B);
c1C.setTransition("1",c1D);
c1D.setTransition("0",c1D);
c1D.setTransition("1",c1D);

consec1.addState(c1A);
consec1.addState(c1B);
consec1.addState(c1C);
consec1.addState(c1D);

consec1.setStart(c1A);

consec2 = FSM("Consec2");

c2A = State("c2A",output="A");
c2B = State("c2B",output="A");
c2C = State("c2C",output="A");
c2D = State("c2D",output="B");
c2E = State("c2C",output="A");
c2F = State("c2D",output="A");

c2A.setTransition("0",c2B);
c2A.setTransition("1",c2C);
c2B.setTransition("0",c2D);
c2B.setTransition("1",c2E);
c2C.setTransition("0",c2F);
c2C.setTransition("1",c2D);
c2D.setTransition("0",c2D);
c2D.setTransition("1",c2D);
c2E.setTransition("0",c2B);
c2E.setTransition("1",c2D);
c2F.setTransition("0",c2D);
c2F.setTransition("1",c2C);

consec2.addState(c2A);
consec2.addState(c2B);
consec2.addState(c2C);
consec2.addState(c2D);
consec2.addState(c2E);
consec2.addState(c2F);

consec2.setStart(c2A);

print(c2E.isEquivalent(c2C));
print(c2B.isEquivalent(c2F));
print(consec1.isEquivalent(consec2));
print("Consec1: " + consec1.process("0101",True,False));
print("Consec2: " + consec2.process("0101",True,False));