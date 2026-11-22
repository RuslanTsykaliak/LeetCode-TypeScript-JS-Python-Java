class Solution {
    public boolean checkString(String s) {
        for (int a = 1; a < s.length(); a++) {
            if (s.charAt(a - 1) == 'b' && s.charAt(a) == 'a') {
                return false;
            }
        }
        return true;
    }
}