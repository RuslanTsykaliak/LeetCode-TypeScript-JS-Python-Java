class Solution {
    public boolean hasAlternatingBits(int n) {
        int prev = 2;

        while (n != 0) {
            if (prev == n % 2) {
                return false;
            }
            prev = n % 2;
            n /= 2;
        }
        return true;
    }
}