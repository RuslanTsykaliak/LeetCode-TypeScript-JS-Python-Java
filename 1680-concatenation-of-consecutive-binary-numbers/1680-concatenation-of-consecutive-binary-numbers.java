class Solution {
    public int concatenatedBinary(int n) {
        long r = 0L;
        for (int i = 1, l = 0; i <= n; i++) {
            r = ((r << (0 == (i & (i - 1)) ? ++l : l)) + i) % 1000000007L;
        }
        return (int) r;
    }
}