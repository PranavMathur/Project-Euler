import java.util.*;
import java.io.*;

public class Problem81 {

	public static void main(String[] args) throws FileNotFoundException {
		int[][] matrix;
		//matrix = new int[][]{{131, 673, 234, 103, 18}, {201, 96, 342, 965, 150}, {630, 803, 746, 422, 111}, {537, 699, 497, 121, 956}, {805, 732, 524, 37, 331}};
		try (Scanner s = new Scanner(new File("matrix.txt"));) {
			matrix = new int[80][80];
			for (int i = 0; i < matrix.length; i++) {
				String line = s.nextLine();
				String[] nums = line.split(",");
				for (int j = 0; j < nums.length; j++) {
					matrix[i][j] = Integer.parseInt(nums[j]);
				}
			}
		}
		int[][] sums = new int[matrix.length][matrix.length];
		sums[sums.length - 1][sums.length - 1] = matrix[matrix.length - 1][matrix.length - 1];
		for (int startRow = sums.length - 1, startCol = sums.length - 2; startRow != 0 || startCol != 0; startRow -= (startCol == 0 ? 1 : 0), startCol -= (startRow == sums.length - 1 ? 1 : 0)) {
			for (int row = startRow, col = startCol; row >= 0 && col < sums.length; row--, col++) {
				sums[row][col] = matrix[row][col];
				int min = Integer.MAX_VALUE;
				if (row + 1 < sums.length && sums[row+1][col] < min)
					min = sums[row+1][col];
				if (col + 1 < sums.length && sums[row][col+1] < min)
					min = sums[row][col+1];
				sums[row][col] += min;
			}
		}
		System.out.println(matrix[0][0] + Math.min(sums[0][1], sums[1][0]));
	}

}
