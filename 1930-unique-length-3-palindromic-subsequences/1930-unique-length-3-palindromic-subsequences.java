class Solution {
    public int countPalindromicSubsequence(String s) {
        Integer[] first = new Integer[26];
        Integer[] last = new Integer[26];

        int result = 0;

        int index = 0;
        for (char c : s.toCharArray()) {
            if (first[c - 'a'] == null) {
                first[c - 'a'] = index;
            } else {
                last[c - 'a'] = index;
            }
            index++;
        }

        for (int i = 0; i < 26; i++) {
            if (first[i] == null || last[i] == null)
                continue;

            HashSet<Character> set = new HashSet<>();

            for (int j = first[i] + 1; j < last[i]; j++) {
                set.add(s.charAt(j));
            }

            result += set.size();
        }

        return result;
    }
}