public class Problem112 {
	
	public static void main(String[] args) {
// 		int numBouncy = 1;
// 		int i;
// 		for (i = 0; true; i++) {
// 			if (100*numBouncy==99*i) break;
// 			if (isBouncy(i)) numBouncy++;
// 			
// 		}
// 		System.out.println(i);
		int a = 0;
		for (int i = 1; i < 1000000; i++)
			if (!isBouncy(i)) a++;
		System.out.println(a);	
	}
	
	private static boolean isBouncy(int num) {
		if (num < 100) return false;
		int[] digits =  Integer.toString(num).chars().map(c -> c-='0').toArray();
		Direction dir = Direction.IDK;
		for (int i = 0; i < digits.length - 1; i++) {
			if (digits[i] == digits[i + 1])
				continue;
			else if (digits[i] < digits[i + 1]) {
				if (dir == Direction.IDK)
					dir = Direction.NEG;
				else if (dir == Direction.POS)
					return true;	
			} else {
				if (dir == Direction.IDK)
					dir = Direction.POS;
				else if (dir == Direction.NEG)
					return true;	
			}
		}
		return false;
	}
	
	private enum Direction {
		POS, NEG, IDK
	}
	
}
