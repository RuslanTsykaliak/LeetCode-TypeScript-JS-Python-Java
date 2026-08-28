class Solution {

    public String lexPalindromicPermutation(String s, String target) {
        int n = s.length();
        // Special case: length of 1
        if (n == 1) {
            return s.compareTo(target) > 0 ? s : "";
        }

        // Count the frequency of each character
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) {
            cnt[c - 'a']++;
        }

        // Check if it can form a palindrome and record the characters with odd occurrences
        String oddChar = "";
        for (int i = 0; i < 26; i++) {
            if (cnt[i] % 2 == 1) {
                // More than one character appears an odd number of times, cannot form a palindrome
                if (oddChar != "") {
                    return "";
                }
                oddChar = String.valueOf((char) ('a' + i));
            }
            cnt[i] /= 2; // It takes only half the characters to construct the left half
        }

        StringBuilder prefix = new StringBuilder();

        // Construct the left part of each digit greedily
        for (int i = 0; i < n / 2; i++) {
            boolean found = false;
            // Try to place the smallest character in lexicographical order
            for (int j = 0; j < 26; j++) {
                if (cnt[j] == 0) {
                    continue;
                }

                cnt[j]--;
                if (check(
                        prefix.toString(),
                        (char) ('a' + j),
                        cnt,
                        oddChar,
                        target)) {
                    // If the constructed palindrome is greater than target, choose the character
                    prefix.append((char) ('a' + j));
                    found = true;
                    break;
                } else {
                    cnt[j]++; // Not meeting the conditions, reset the counter
                }
            }
            if (!found) {
                return ""; // Cannot construct a palindrome larger than target
            }

            if (prefix.charAt(i) > target.charAt(i)) {
                // prefix is already greater than target
                StringBuilder left = new StringBuilder(prefix);
                for (int j = 0; j < 26; j++) {
                    for (int k = 0; k < cnt[j]; k++) {
                        left.append((char) ('a' + j));
                    }
                }
                String palindrome = left.toString() +
                        oddChar +
                        new StringBuilder(left).reverse().toString();
                return palindrome;
            }
        }

        // Construct the final palindrome string
        String ans = prefix.toString() +
                oddChar +
                new StringBuilder(prefix).reverse().toString();
        return ans;
    }

    private boolean check(
            String prefix,
            char c,
            int[] cnt,
            String oddChar,
            String target) {
        StringBuilder left = new StringBuilder(prefix);
        left.append(c);
        for (int i = 25; i >= 0; i--) {
            for (int k = 0; k < cnt[i]; k++) {
                left.append((char) ('a' + i));
            }
        }

        String palindrome = left.toString() +
                oddChar +
                new StringBuilder(left).reverse().toString();

        return palindrome.compareTo(target) > 0;
    }
}