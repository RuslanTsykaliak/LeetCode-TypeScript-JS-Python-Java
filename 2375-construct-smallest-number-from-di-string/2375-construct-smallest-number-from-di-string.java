class Solution {
    public String smallestNumber(String pattern) {
        int patternLength = pattern.length();
        int maxSoFar = 0, currMax = 0, temp;

        // Array to store lengths of decreasing subsequences in the pattern
        int[] arrD = new int[patternLength + 2];

        // Compute the lengths of decreasing subsequences in the pattern
        for (
            int patternIndex = patternLength;
            patternIndex >= 0;
            patternIndex--
        ) {
            // If 'D', increment the length of the decreasing sequence
            if (
                patternIndex < patternLength &&
                pattern.charAt(patternIndex) == 'D'
            ) arrD[patternIndex] = arrD[patternIndex + 1] + 1;
        }

        StringBuilder result = new StringBuilder();

        // Build the result string based on the pattern
        for (int position = 0; position <= patternLength; position++) {
            if (position < patternLength && pattern.charAt(position) == 'I') {
                // If 'I', assign the next maximum digit and append it to the result
                maxSoFar++;
                result.append(maxSoFar);

                // Update the max digit encountered so far
                maxSoFar = Math.max(maxSoFar, currMax);

                // Rest current max for the next interation
                currMax = 0;
            } else {
                // If 'D', calculate the appropriate digit and append it to the result
                temp = 1 + maxSoFar + arrD[position];
                result.append(temp);

                // Update the current max value
                currMax = Math.max(currMax, temp);
            }
        }

        return result.toString();
    }
}