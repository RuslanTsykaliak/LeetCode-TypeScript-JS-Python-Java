class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $numOperations
     * @return Integer
     */
    function maxFrequency($nums, $k, $numOperations) {
        // Count frequency of each number in original array
        $freq = [];
        // Track sweep line events: +1 at range start, -1 at range end
        $events = [];
        
        // Count frequency of each number
        foreach ($nums as $num) {
            $freq[$num] = isset($freq[$num]) ? $freq[$num] + 1 : 1;
        }
        
        // For each number, mark the range of targets it can be converted to
        foreach ($nums as $num) {
            // Number can be converted to any target in [num-k, num+k]
            $start = max(0, $num - $k);
            $end = $num + $k + 1; // End of convertible range (exclusive)
            
            $events[$start] = isset($events[$start]) ? $events[$start] + 1 : 1;
            $events[$end] = isset($events[$end]) ? $events[$end] - 1 : -1;
        }
        
        $maxFreq = 0;
        $sweep = 0;
        
        // Get all unique positions (event boundaries and original numbers)
        $positions = array_unique(array_merge(
            array_keys($events),
            array_keys($freq)
        ));
        sort($positions);
        
        // Process all relevant positions
        foreach ($positions as $pos) {
            $sweep += isset($events[$pos]) ? $events[$pos] : 0; // Update running count
            
            // Convertible numbers that are NOT already equal to current position
            $currentFreq = isset($freq[$pos]) ? $freq[$pos] : 0;
            $convertibleCount = $sweep - $currentFreq;
            
            // Max frequency = existing count + min(convertible, available operations)
            $maxFreq = max($maxFreq, $currentFreq + min($convertibleCount, $numOperations));
        }
        
        return $maxFreq;
    }
}