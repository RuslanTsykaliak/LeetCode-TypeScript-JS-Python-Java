function maxFrequencyElements(nums: number[]): number {
    let freqMap = new Map<number, number>();
    let maxFreq = 0;
    let maxFreqCount = 0;

    // Count the frequency of each number
    for (let num of nums) {
        let freq = (freqMap.get(num) || 0) + 1;
        freqMap.set(num, freq);

        // Update max frequency and count
        if (freq > maxFreq) {
            maxFreq = freq;
            maxFreqCount = 1;
        } else if (freq === maxFreq) {
            maxFreqCount++;
        }
    }

    // Return the total count of numbers with max frequency
    return maxFreq * maxFreqCount;
}
