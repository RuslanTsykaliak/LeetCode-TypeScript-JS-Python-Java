class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;

        for (int n : nums) {
            if (String.valueOf(n).length() % 2 == 0) {
                count++; // += 1
            }
        }

        return count;
    }
}