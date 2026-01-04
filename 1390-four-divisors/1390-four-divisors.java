class Solution {
    public int sumFourDivisors(int[] nums) {
        int total = 0;

        for (int x : nums) {
            int count = 0, sum = 0;

            for (int i = 1; i * i <= x; i++) {
                if (x % i == 0) {
                    int j = x / i;
                    if (i == j) {
                        count++;
                        sum += i;
                    } else {
                        count += 2;
                        sum += i + j;
                    }
                }
                if (count > 4)
                    break;
            }

            if (count == 4)
                total += sum;
        }

        return total;
    }
}