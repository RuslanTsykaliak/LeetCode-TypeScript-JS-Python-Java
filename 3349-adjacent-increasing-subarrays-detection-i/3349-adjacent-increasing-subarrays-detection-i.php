class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function hasIncreasingSubarrays($nums, $k) {
        $n = count($nums);
        if ($n < 2 * $k) {
            return false;
        }

        for ($i = 0; $i <= $n - 2 * $k; $i++) {
            $firstIncreasing = true;
            $secondIncreasing = true;

            // Check first subarray
            for ($j = $i; $j < $i + $k - 1; $j++) {
                if ($nums[$j] >= $nums[$j + 1]) {
                    $firstIncreasing = false;
                    break;
                }
            }

            // Check second subarray
            if ($firstIncreasing) {
                for ($j = $i + $k; $j < $i + 2 * $k - 1; $j++) {
                    if ($nums[$j] >= $nums[$j + 1]) {
                        $secondIncreasing = false;
                        break;
                    }
                }

                if ($secondIncreasing) {
                    return true;
                }
            }
        }

        return false;
    }
}
