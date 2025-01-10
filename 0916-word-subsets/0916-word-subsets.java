class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        int[] maxCount = new int[26];

        for (String w : words2) {
            int[] curCount = new int[26];
            for (char c : w.toCharArray())
                curCount[c - 'a']++;
            for (int i = 0; i < 26; i++)
                maxCount[i] = Math.max(maxCount[i], curCount[i]);
        }

        List<String> result = new ArrayList<>();

        for (String w : words1) {
            int[] curCount = new int[26];
            for (char c : w.toCharArray())
                curCount[c - 'a']++;
            for (int i = 0; i < 26; i++) {
                if (curCount[i] < maxCount[i])
                    break;
                if (i == 25)
                    result.add(w);
            }
        }
        return result;
    }
}