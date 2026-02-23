class Solution {
    public boolean hasAllCodes(String s, int k) {
        if (s.length() < k) {
            return false;
        }

        Set<String> set = new HashSet<String>();

        for (int i = 0; i <= s.length() - k; i++) {
            set.add(s.substring(i, i + k));
        }
        return (set.size() == (int) Math.pow(2, k));
    }
}