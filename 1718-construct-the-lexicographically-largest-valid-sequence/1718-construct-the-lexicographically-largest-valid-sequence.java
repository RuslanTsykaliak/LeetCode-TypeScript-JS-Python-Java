class Solution {
    public int[] constructDistancedSequence(int n) {
        // Initialize the result sequence with size 2*n - 1 filled with 0s
        int[] result = new int[n * 2 - 1];

        // Keep track of which numbers are already placed in the sequence
        boolean[] isNumberUsed = new boolean[n + 1];

        // Start recursive backtracking to construct the sequence
        findLexicographicallyLargestSequence(
            0,
            result,
            isNumberUsed,
            n
        );

        return result;
    }

    // Recursive function to generate the desired sequence
    private boolean findLexicographicallyLargestSequence(
        int currentIndex,
        int[] result,
        boolean[] isNumberUsed,
        int n
    ) {
        // If we have filled all positions, return true indicating success
        if (currentIndex == result.length) {
            return true;
        }

        // If the current position is alredy filled, move to the next index
        if (result[currentIndex] != 0) {
            return findLexicographicallyLargestSequence(
                currentIndex + 1,
                result,
                isNumberUsed,
                n
            );
        }

        // Attempt to place numbers from n to 1 for 
        // a lexicographically largest result
        for (
            int numberToPlace = n;
            numberToPlace >= 1;
            numberToPlace--
        ) {
            if (isNumberUsed[numberToPlace]) continue;

            isNumberUsed[numberToPlace] = true;
            result[currentIndex] = numberToPlace;

            // If placing number 1, move to the next index directly
            if (numberToPlace == 1) {
                if (
                    findLexicographicallyLargestSequence(
                        currentIndex + 1,
                        result,
                        isNumberUsed,
                        n
                    )
                ) {
                    return true;
                }
            }
            // Place larger numbers at two positions if valid
            else if (
                currentIndex + numberToPlace < result.length && result[currentIndex + numberToPlace] == 0
            ) {
                result[currentIndex + numberToPlace] = numberToPlace;
                
                if (
                    findLexicographicallyLargestSequence(
                        currentIndex + 1,
                        result,
                        isNumberUsed,
                        n
                    )
                ) {
                    return true;
                }

                // Undo the placement for bactracking
                result[currentIndex + numberToPlace] = 0;
            }

            // Undo current placement and makr the number as unused
            result[currentIndex] = 0;
            isNumberUsed[numberToPlace] = false;
        }
        
        return false;
    }
}