class Solution {
    public boolean canBeValid(String s, String locked) {
        int n = s.length();
        if (n % 2 != 0) return false;

        // Check balance from left to right
        int balance = 0;
        for (int i = 0; i < n; ++i) {
            if (s.charAt(i) == '(' || locked.charAt(i) == '0') {
                balance++;
            } else {
                balance--;
            }
            if (balance < 0) return false;
        }

        // Check balance from right to left
        balance = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (s.charAt(i) == ')' || locked.charAt(i) == '0') {
                balance++;
            } else {
                balance--;
            }
            if (balance < 0) return false;
        }

        return true;
    }
}