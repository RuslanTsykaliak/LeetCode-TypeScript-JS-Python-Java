class Solution {
    public int minOperations(String s) {
        int start = 0;

        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 0) {
                if (s.charAt(i) == '1') {
                    start++;
                }
            } else {
                if (s.charAt(i) == '0') {
                    start++;
                }
            }
        }
        return Math.min(start, s.length() - start);
    }
}