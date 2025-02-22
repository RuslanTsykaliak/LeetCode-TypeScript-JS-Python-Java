class Solution {
    public int numberOfSteps(int num) {
        // Initialize the variable to hold the number of steps to reduce 'num' to zero
        int steps = 0;

        // Loop until num equals 0
        while (num != 0) {
            // If num is even, divide it by 2
            if (num % 2 == 0) {
                num /= 2;
                // Increment the step count
                steps++;
                // If num is odd, subtract 1
            } else {
                num -= 1;
                // Increment the step count
                steps++;
            }
        }

        return steps;
    }
}
