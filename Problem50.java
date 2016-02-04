import java.util.Arrays;
import java.util.Scanner;
import java.io.File;

public class Problem50 {

	public static void main(String[] args) {
		long[] primes = new long[78498];
		long[] sumUpTo = new long[78498];
		
		try (Scanner s = new Scanner(new File("primes.list"));) {
			int current = 0;
			while (s.hasNextLong() && current < primes.length) {
				primes[current++] = s.nextLong();
			}
		} catch (Exception ignore) { System.out.println("Exception"); }
		
		sumUpTo[0] = 0;
		for (int i = 1; i < sumUpTo.length; i++)
			sumUpTo[i] = sumUpTo[i-1] + primes[i-1];
		
		long limit = 1000000L;
		int maxLength = 0;
		long result = 0;

		for (int end = sumUpTo.length - 1; end >= 0; end--) {
			for (int start = end - maxLength - 1; start >= 0; start--) {
				if (sumUpTo[end] - sumUpTo[start] > limit) break;
				long diff = sumUpTo[end] - sumUpTo[start];
				if (Arrays.binarySearch(primes, diff) >= 0) {
					maxLength = end - start;
					result = diff;
				}
			}
		}
		
		System.out.println(maxLength);
		System.out.println(result);
	}

}
