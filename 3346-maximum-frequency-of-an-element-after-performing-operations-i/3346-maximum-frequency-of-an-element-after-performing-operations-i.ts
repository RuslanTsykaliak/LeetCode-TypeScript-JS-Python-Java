function maxFrequency(nums: number[], k: number, numOperations: number): number {
    // Find the maximum number in nums to define the size of cnt and prefixSum arrays
    let maxNum = -Infinity;
    let minNum = Infinity;

    for (const num of nums) {
        maxNum = Math.max(maxNum, num);
        minNum = Math.min(minNum, num);
    }

    // Initialize count array
    let count = new Array(maxNum + 1).fill(0);
    for (let num of nums) {
        count[num]++;
    }

    // Compute prefix sums
    let prefixSum = new Array(maxNum + 1).fill(0);
    prefixSum[0] = count[0];
    for (let i = 1; i <= maxNum; i++) {
        prefixSum[i] = prefixSum[i - 1] + count[i];
    }

    let maxFreq = 0;

    // Iterate through all possible targets
    for (let target = minNum; target <= maxNum; target++) {
        let leftBound = Math.max(target - k, minNum);
        let rightBound = Math.min(target + k, maxNum);

        // Total elements within [leftBound, rightBound]
        let totalInRange = prefixSum[rightBound] - (prefixSum[leftBound - 1] ?? 0);

        // Elements that can be modified to t
        let elementsToModify = totalInRange - count[target];

        // Number of operations we can use to modify elements to t
        let possibleToModify = Math.min(numOperations, elementsToModify);

        // Current frequency if we choose t as the target
        let currentFreq = count[target] + possibleToModify;

        // Update maximum frequency
        maxFreq = Math.max(maxFreq, currentFreq);
    }

    return maxFreq;
}