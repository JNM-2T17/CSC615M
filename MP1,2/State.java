import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map.Entry;

public class State {
	private String name;
	private HashMap<String,State> transition;
	private HashMap<String,String> output;
	private String outputSymbol;
	private boolean isFinal;
	private HashMap<State,Boolean> equivalence;

	public State(String name) {
		this.name = name;
		transition = new HashMap<String,State>();
		output = new HashMap<String,String>();
		outputSymbol = "";
		isFinal = false;
		equivalence = new HashMap<State,Boolean>();
	}

	public State(String name,String outputSymbol) {
		this.name = name;
		transition = new HashMap<String,State>();
		output = new HashMap<String,String>();
		this.outputSymbol = outputSymbol;
		isFinal = false;
		equivalence = new HashMap<State,Boolean>();
	}

	public State(String name,String outputSymbol, boolean isFinal) {
		this.name = name;
		transition = new HashMap<String,State>();
		output = new HashMap<String,String>();
		this.outputSymbol = outputSymbol;
		isFinal = true;
		equivalence = new HashMap<State,Boolean>();
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public boolean isFinal() {
		return isFinal;
	}

	public void setFinal(boolean isFinal) {
		this.isFinal = isFinal;
		equivalence.clear();
	}

	public void setTransition(String input,State target) {
		transition.put(input,target);
		equivalence.clear();
	}

	public void setTransition(String input,State target,String output) {
		transition.put(input,target);
		this.output.put(input,output);
		equivalence.clear();
	}

	public State getTransition(String input) {
		return transition.get(input);
	}

	public String getOutput() {
		return outputSymbol;
	}

	public String getOutput(String input) {
		String ret = output.get(input);
		return ret == null ? "" : ret;
	}

	public boolean isEquivalent(State s2) {
		Boolean b = equivalence.get(s2);
		if( b == null ) {
			return isEquivalent(s2,new ArrayList<State>(),new ArrayList<State>());
		} else {
			return b;
		}
	}

	private boolean isEquivalent(State s2, ArrayList<State> v1, 
									ArrayList<State> v2) {
		// System.out.println(name + " vs " + s2.name);
		// System.out.println(isFinal + " vs " + s2.isFinal);
		if( this.isFinal ^ s2.isFinal ) {
			System.out.println(this.name + " and " + s2.name + " are not both acceptors or non-acceptors.");
			this.equivalence.put(s2,false);
			s2.equivalence.put(this,false);
			return false;
		} else if( s2.name.compareTo(name) < 0 ) {
			v1.add(s2);
			v2.add(this);
		} else if( s2.name.compareTo(name) > 0 ) {
			v1.add(this);
			v2.add(s2);
		} 

		for(Entry<String,State> entry : transition.entrySet() ) {
			String alpha = entry.getKey();
			State t1 = transition.get(alpha);
			State t2 = s2.transition.get(alpha);

			boolean found = false;

			for(int i = 0; i < v1.size(); i++) {
				if( t1 == v1.get(i) && t2 == v2.get(i)) {
					found = true;
					break;
				}
			}

			if( found ) {
				continue;
			}

			String oMoore1 = t1.outputSymbol;
			String oMoore2 = t2.outputSymbol;
			String oMealy1 = getOutput(alpha);
			String oMealy2 = s2.getOutput(alpha);
			if( !oMoore1.equals(oMoore2) || 
				!oMealy1.equals(oMealy2) || !t1.isEquivalent(t2,v1,v2) ) {
				if( !oMoore1.equals(oMoore2) ) {
					System.out.println("g(" + t1.name + ") = " + oMoore1 + 
										" != g(" + t2.name + ") = " + oMoore2);
				} else if( !oMealy1.equals(oMealy2) ) {
					System.out.println("g(" + name + "," + alpha + ") = " + 
										oMealy1 + " != g(" + s2.name + "," + 
										alpha + ") = " + oMealy1);
				} else {
					System.out.println(name + " !~ " + s2.name);
				}
				this.equivalence.put(s2,false);
				s2.equivalence.put(this,false);
				return false;
			}
		}

		this.equivalence.put(s2,true);
		s2.equivalence.put(this,true);
			
		return true;
	}
}