class Solution {
    public int prefixCount(String[] words, String pref) {
        // Store the result
        int num = 0;

        for (int i = 0; i < words.length; i++) {
            if (words[i].startsWith(pref)) {
                num += 1;
            }
        }
        return num;
    }
}