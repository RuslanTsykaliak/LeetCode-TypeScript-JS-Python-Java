class Solution {
    public String mergeAlternately(String word1, String word2) {
        char[] arrayChar1 = word1.toCharArray();
        char[] arrayChar2 = word2.toCharArray();
        String merged = "";
        int i = 0, j = 0;

        while (i < arrayChar1.length || j < arrayChar2.length) {
            if (i < arrayChar1.length) {
                merged += arrayChar1[i++];
            }
            if (j < arrayChar2.length) {
                merged += arrayChar2[j++];
            }
        }
        return merged;
    }
}