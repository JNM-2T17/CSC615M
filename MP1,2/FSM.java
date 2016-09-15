import java.util.ArrayList;
import java.util.HashMap;

public class FSM {
	private String name;
	private HashMap<String,State> q;
	private State q0;

	public FSM(String name) {
		this.name = name;
		q = new HashMap<String,State>();
	}

	public void addState(State s) {
		q.put(this.name + "~" + s.getName(),s);
		s.setName(this.name + "~" + s.getName());
	}

	public State getState(String name) {
		return q.get(this.name + "~" + name);
	}

	public void setStartState(State s) {
		q0 = s;
	}

	public boolean run(String input) {
		if( q0 == null ) {
			return false;
		} else {
			State curr = q0;
			for(int i = 0; i < input.length(); i++) {
				curr = curr.getTransition(input.charAt(i) + "");
				if( curr == null ) {
					return false;
				}
			}
			return curr.isFinal();
		}
	}

	public String run(String input,boolean isMealy) {
		if( q0 == null ) {
			return "";
		} else {
			State curr = q0;
			StringBuilder output = new StringBuilder();
			for(int i = 0; i < input.length(); i++) {
				State newcurr = curr.getTransition(input.charAt(i) + "");
				if( newcurr == null ) {
					return output.toString();
				} else if(isMealy) {
					output.append(curr.getOutput(input.charAt(i) + ""));
				} else {
					output.append(newcurr.getOutput());
				}
				curr = newcurr;
			}
			return output.toString();
		}	
	}

	public boolean isEquivalent(FSM m2) {
		if( q0 == null && m2.q0 == null || q0 != null && m2.q0 != null && 
			!q0.isEquivalent(m2.q0) ) {
			return false;
		}
		return true;
	}
}