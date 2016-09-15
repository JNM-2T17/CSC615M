public class Driver {
	public static void main(String[] args) {
		// FSM m1 = new FSM("Odd1");
		// FSM m2 = new FSM("Odd2");

		// State m1s1 = new State("A");
		// State m1s2 = new State("B");
		// m1s2.setFinal(true);
		// m1s1.setTransition("0",m1s2);
		// m1s2.setTransition("0",m1s1);

		// m1.addState(m1s1);
		// m1.addState(m1s2);
		// m1.setStartState(m1s1);

		// State m2s1 = new State("A");
		// State m2s2 = new State("B");
		// m2s2.setFinal(true);
		// m2s1.setTransition("0",m2s2);
		// m2s2.setTransition("0",m2s1);

		// m2.addState(m2s1);
		// m2.addState(m2s2);
		// m2.setStartState(m2s1);

		// System.out.println(m1.isEquivalent(m2));

		FSM consec1 = new FSM("Consec1");

		State c1A = new State("c1A","A");
		State c1B = new State("c1B","A");
		State c1C = new State("c1C","A");
		State c1D = new State("c1D","B");

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

		consec1.setStartState(c1A);

		FSM consec2 = new FSM("Consec2");

		State c2A = new State("c2A","A");
		State c2B = new State("c2B","A");
		State c2C = new State("c2C","A");
		State c2D = new State("c2D","B");
		State c2E = new State("c2C","A");
		State c2F = new State("c2D","A");

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

		consec2.setStartState(c2A);

		System.out.println(consec1.isEquivalent(consec2));
		System.out.println("Consec1: " + consec1.run("0101",false));
		System.out.println("Consec2: " + consec2.run("0101",false));
	}
}