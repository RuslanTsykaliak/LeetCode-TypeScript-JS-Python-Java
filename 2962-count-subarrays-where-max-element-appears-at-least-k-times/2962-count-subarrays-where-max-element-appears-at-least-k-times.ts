function countSubarrays(nums: number[], k: number): number {
    // Find the maximum value in the input array nums
    const maximumValue = Math.max(...nums)
    // Get the length of the input array nums
    const len = nums.length
    // Initialize count of maximum values and index pointer
    let countOfMax = 0
    let indexPointer = 0
    // Initialize answer which will hold the count of valid subarrays
    let answer = 0

    // Iterate over each element in the nums array
    for (const current of nums) {
        // Increase indexPointer while total max-element count is less then k
        // and the indexPointer is within the array bounds]
        while (indexPointer < len && countOfMax < k) {
            if (nums[indexPointer] === maximumValue) {
                countOfMax += 1
            }
            indexPointer += 1
        }

        // If the count is less than k at this point, we can exit the loop
        if (countOfMax < k) {
            break
        }

        // Add the number of valid subarrays that can be formed this position.
        answer += len - indexPointer + 1

        // Decrease the count of maximum values if the current element was a maximum
        if (current === maximumValue) {
            countOfMax -= 1
        }
    }

    // Return the total number of subarrays that satisfy the condition
    return answer
};