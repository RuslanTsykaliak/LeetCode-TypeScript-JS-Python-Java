class Solution {
    public int reverseBits(int n) {
        int[] bit = new int[32];
        int i = 0;

        // Extract bits
        while (n >= 2) {
            bit[i++] = n % 2;
            n = n / 2;
        }

        if (i < 32) {
            bit[i] = n;
        }
        // Rebuild reversed number
        n = 0;
        int p = 0;
        for (int j = 31; j >= 0; j--) {
            n += bit[j] * Math.pow(2, p++);
        }

        return n;
    }
}