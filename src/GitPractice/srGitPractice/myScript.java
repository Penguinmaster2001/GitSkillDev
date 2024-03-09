class Fibonacci {
	public static void main(String args[]){
		int n = 10;
		int result = fib(n);
		// The final result
		System.out.println("Final result of " + n + ": ");
		System.out.println(result);

		// All steps
		System.out.println("All step to " + n + ": ");
		for (int i = 0; i < n; i++) {
			System.out.println(fib(i));
		}
	}

	private static void fib(int n) {
		if (n <= 1) {
			return;
		}

		return fib(n-2) + fib(n-1);
	}
}
