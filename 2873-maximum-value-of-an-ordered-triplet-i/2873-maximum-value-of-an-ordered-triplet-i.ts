function maximumTripletValue(nums: number[]): number {
    // Algorithm: Optimized Single Pass Greedy

    // Input: An array of integers 'nums'.
    // Output: The maximum value of (maxLeft - currentNum) * maxRight, where 
    //         maxLeft is the maximum number to the left of currentNum, and 
    //         maxRight is the maximum number to the right of currentNum.

    let maxLeftValue = 0; // Tracks the maximum value encountered from the left.
    let maxDiff = 0;      // Tracks the maximum difference (maxLeftValue - currentNum).
    let maxValue = 0;    

    // Iterate through the 'nums' array.
    for (const currentNum of nums) {
        // Update the maximum triplet value.
        maxValue = Math.max(maxValue, maxDiff * currentNum);

        // Update the maximum difference.
        maxDiff = Math.max(maxLeftValue - currentNum, maxDiff);

        // Update the maximum left value.
        maxLeftValue = Math.max(maxLeftValue, currentNum);
    }

    return maxValue;
};