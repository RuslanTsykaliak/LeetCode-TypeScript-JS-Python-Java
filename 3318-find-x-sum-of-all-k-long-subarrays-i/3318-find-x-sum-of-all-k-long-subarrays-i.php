class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $x
     * @return Integer[]
     */
    function findXSum($nums, $k, $x) {
        $n = count($nums);
        $answer = [];

        // Process each subarray of length k
        for ($i = 0; $i <= $n - $k; $i++) {
            $sub = array_slice($nums, $i, $k);

            // Count occurrences
            $counts = array_count_values($sub);

            // Sort by frequency descending, then by value descending
            uksort($counts, function($a, $b) use ($counts) {
                if ($counts[$a] == $counts[$b]) {
                    return $b - $a; // Higher value first if frequency is the same
                }
                return $counts[$b] - $counts[$a]; // Higher frequency first
            });

            // Take the top x frequencies
            $sum = 0;
            $count = 0;
            foreach ($counts as $num => $freq) {
                $sum += $num * $freq;
                $count++;
                if ($count == $x) break;
            }

            $answer[] = $sum;
        }
        return $answer;
    }
}