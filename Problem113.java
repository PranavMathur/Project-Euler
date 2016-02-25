public class Problem113 {

	static int length = 3;
	
	public static void main(String[] args) throws InterruptedException{
		int answer = 0;
		for (int i = 0; i < 10; i++) {
			answer += count(0, i, true);
			answer += count(0, i, false);
		}
		System.out.println(answer);
	}
	
	public static int count(int index, int prev, boolean up) {
		if (index == length - 1)
			return 1;
		int c = 0;
		if (up) {
			for (int i = prev; i < 10; i++)
				c += count(index + 1, i, up);
		} else {
			for (int i = prev; i >= 0; i--)
				c += count(index + 1, i, up);
		}
		return c;
	}
	
}
