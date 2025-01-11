class Solution {
    public boolean canConstruct(String s, int k) {
        // If k is greater than the length of s, it's impossible to form k palindromes
        if (k > s.length()) {
            return false;
        }

        // Create a frequency map to count occurrences of each character
        Map<Character, Integer> charCount = new HashMap<>();
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }

        // Count how many characters have an odd frequency
        int oddCount = 0;
        for (int count : charCount.values()) {
            if (count % 2 != 0) {
                oddCount++;
            }
        }

        // We can form at most K palindromes if the number of odd counts is <= K
        return oddCount <= k;
    }
}