class Solution {
    public int scoreOfParentheses(String s) {
        int score = 0;
        int openBrackets = 0;
        Boolean seenFirstClosingBracket = false;

        for (char c : s.toCharArray()) {
            if (c == ')') {
                if (!seenFirstClosingBracket) {
                    seenFirstClosingBracket = true;
                    score = score + (int) Math.pow(2, openBrackets - 1);
                }
                openBrackets--;
            } else {
                openBrackets++;
                seenFirstClosingBracket = false;
            }
        }
        return score;
    }
}