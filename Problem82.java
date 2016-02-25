public class Problem82 {
	
	public static void main(String[] args) {
		int[][] matrix;
		matrix = new int[][]{{131, 673, 234, 103, 18}, {201, 96, 342, 965, 150}, {630, 803, 746, 422, 111}, {537, 699, 497, 121, 956}, {805, 732, 524, 37, 331}};
// 		try (Scanner s = new Scanner(new File("matrix.txt"));) {
// 			matrix = new int[80][80];
// 			for (int i = 0; i < matrix.length; i++) {
// 				String line = s.nextLine();
// 				String[] nums = line.split(",");
// 				for (int j = 0; j < nums.length; j++) {
// 					matrix[i][j] = Integer.parseInt(nums[j]);
// 				}
// 			}
// 		}
		
		
		
	}
	
}

class Node {
	
	int val;
	Node child;
	
	Node(int val) {
		this.val = val;
	}
	
	int sum() {
		int s = val;
		s += (child != null) ? child.val : 0;
		return s
	}
	
}
