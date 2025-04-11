class Solution {
    public int countSymmetricIntegers(int low, int high) {
        int res = 0;
        for (int i = low; i <= high; ++i) {
            if (i < 100 && i % 11 == 0) {
                res++;
            } else if (1000 <= i && i < 10000) {
                int left = i / 1000 + (i % 1000) / 100;
                int right = (i % 100) / 10 + (i % 10);
                if (left == right) {
                    res++;
                }
            }
        }
        return res;
    }
}