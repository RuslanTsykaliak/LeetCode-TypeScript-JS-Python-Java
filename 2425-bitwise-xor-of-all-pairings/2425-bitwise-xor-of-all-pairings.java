class Solution {
    public int xorAllNums(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int n2 = nums2.length;
        int result = 0;

        if (n1 % 2 != 0) {
            for (int i = 0; i < n2; i++) {
                result ^= nums2[i];
            }
        }

        if (n2 % 2 != 0) {
            for (int i = 0; i < n1; i++) {
                result ^= nums1[i];
            }
        }

        return result;
    }
}