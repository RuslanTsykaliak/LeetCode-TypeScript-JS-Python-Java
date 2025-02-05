class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        if (s1.equals(s2)) {
            return true;
        }

        List<Integer> diffIndices = new ArrayList<>();

        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                diffIndices.add(i);
            }
        }

        if (diffIndices.size() != 2) {
            return false;
        }

        int index1 = diffIndices.get(0);
        int index2 = diffIndices.get(1);

        return (s1.charAt(index1) == s2.charAt(index2)) && (s1.charAt(index2) == s2.charAt(index1));
    }
}