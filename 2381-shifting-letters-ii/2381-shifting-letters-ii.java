class Solution {
    public String shiftingLetters(String s, int[][] shifts) {
        char[] characters = s.toCharArray();
        int[] shiftMap = new int[characters.length + 1];
        for (int[] shift : shifts) {
            if (shift[2] == 0) {
                shiftMap[shift[0]] -= 1;
                shiftMap[shift[1] + 1] += 1;
            } else {
                shiftMap[shift[0]] += 1;
                shiftMap[shift[1] + 1] -= 1;
            }
        }
        int cumulativeShift = 0;
        for (int i = 0; i < characters.length; i++) {
            cumulativeShift += shiftMap[i];
            int newCharIndex = ((characters[i] - 'a') + cumulativeShift) % 26;
            if (newCharIndex < 0)
                newCharIndex += 26;
            characters[i] = (char) (newCharIndex + 'a');
        }
        return new String(characters);
    }
}