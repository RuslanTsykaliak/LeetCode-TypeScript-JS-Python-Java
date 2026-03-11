class Solution {
    public int bitwiseComplement(int n) {
        if (n == 0) {
            return 1;
        }
        int mask = n;
        for (int i = 1; i <= 1 << 4; i <<= 1) {
            mask |= mask >> i;
        }
        return ~n & mask;
    }
}