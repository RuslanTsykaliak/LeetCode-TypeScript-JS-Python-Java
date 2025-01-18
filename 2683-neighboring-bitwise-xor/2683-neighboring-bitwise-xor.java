class Solution {
    public boolean doesValidArrayExist(int[] derived) {
        int result = 0;
        for (int val : derived) {
            result ^= val;
        }
        return result == 0;
    }
}