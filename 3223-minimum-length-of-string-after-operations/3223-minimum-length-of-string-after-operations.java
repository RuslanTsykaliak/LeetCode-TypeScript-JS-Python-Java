class Solution {
    public int minimumLength(String s) {
        HashMap<Character, Integer> freq = new HashMap<>();

        // Count frequency of each character
        for (char ch: s.toCharArray()) {
            freq.put(ch, freq.getOrDefault(ch, 0) + 1);
        }

        int ans = 0;

        // Process each character frequency
        for (int count : freq.values()) {
            ans += (count % 2 == 0) ? 2 : 1;
        }

        return ans;
    }
}