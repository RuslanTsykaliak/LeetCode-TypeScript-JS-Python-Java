class Solution {
    public String getHappyString(int n, int k) {
        Stack<String> stringsStack = new Stack<>();
        int indexInSortedList = 0;
        stringsStack.push(""); // Start with an empty string

        while (stringsStack.size() > 0) {
            String currentString = stringsStack.pop();

            // If we have built a string of length n, count it
            if (currentString.length() == n) {
                indexInSortedList++;
                // If we reach the k-th happy strig, return it
                if (indexInSortedList == k) {
                    return currentString;
                }
                continue;
            }

            // Expand the current string by adding 'a', 'b', or 'c'
            // Ensuring lexicographic order by pushing in reverse
            for (char currentChar = 'c'; currentChar >= 'a'; currentChar--) {
                // Avoid consecutive identical characters
                if (currentString.length() == 0 ||
                        currentString.charAt(currentString.length() - 1) != currentChar) {
                    stringsStack.push(currentString + currentChar);
                }
            }
        }
        return "";
    }
}