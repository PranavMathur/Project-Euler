import java.util.Scanner;
import java.util.Arrays;
import java.io.File;

public class Problem96{
	
	public static void main(String[] args) {
		try (Scanner s = new Scanner(new File("sudoku.txt"))) {
			Sudoku[] sudokus = new Sudoku[50];
			for (int i = 0; i < 50; i++) {
				s.nextLine();
				String[] lines = new String[9];
				for (int j = 0; j < 9; j++) {
					lines[j] = s.nextLine();
				}
				int[][] field = new int[9][9];
				for (int row = 0; row < 9; row++) {
					String line = lines[row];
					int[] nums = field[row];
					for (int col = 0; col < 9; col++) {
						nums[col] = Integer.parseInt(line.substring(col, col+1));
					}
				}
			}
		} catch(Exception e) {
			System.out.println(e.getMessage());
		}
	}

}

class Sudoku {
	
	private int[][] field;
	
	public Sudoku(int[][] field) {
		this.field = field;
	}
	
	public void solve() {
		
	}
	
	public int digits() {
		return 100 * field[0][0] + 10 * field[0][1] + field[0][2];
	}

}
