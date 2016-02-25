import java.util.Arrays;

public class Problem69 {

	public static void main(String[] args) {
		
	}
	
	private static int totient(int n) {
		boolean[] vals = new boolean[n-1];
		Arrays.fill(vals, true);
		return Arrays.count(vals, true);
	}

}
