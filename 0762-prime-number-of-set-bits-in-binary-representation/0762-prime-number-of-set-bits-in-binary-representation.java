class Solution {
    public int countPrimeSetBits(int left, int right) {
        int res = 0;
        for (int i = left; i <= right; ++i) {
            if (isSmallPrime(Integer.bitCount(i))) {
                res++;
            }
        }
        return res;
    }
    public boolean isSmallPrime(int i) {
        return (i == 2 || i == 3 || i == 5 || i == 7 | i == 11 || i == 13 || i == 17 || i == 19);
    }
}