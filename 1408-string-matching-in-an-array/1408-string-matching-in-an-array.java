class Solution {
    public List<String> stringMatching(String[] words) {
        // Use a HashSet to store the results to avoid duplicates.
        HashSet<String> st = new HashSet<>();

        // Sort the words array by length in ascending order. This optimization allows
        // us to
        // efficiently check for substrings. If a shorter string is a substring, we'll
        // find
        // it before encountering a longer string that contains it.
        Arrays.sort(words, (a, b) -> a.length() - b.length());

        // Iterate through each word in the sorted array.
        for (int i = 0; i < words.length; i++) {
            // Iterate through the remaining words (those with potentially greater length).
            for (int j = i + 1; j < words.length; j++) {
                // Check if the current word (words[i]) is a substring of the next word
                // (words[j]).
                if (words[j].contains(words[i])) {
                    // If it is a substring, add it to the HashSet.
                    st.add(words[i]);
                    // Once we find a match, we can break the inner loop because we know
                    // words[i] is a substring of at least one other word. No need to check
                    // against further longer strings.
                    break;
                }
            }
        }
        // Convert the HashSet to an ArrayList and return it.
        return new ArrayList<>(st);
    }
}