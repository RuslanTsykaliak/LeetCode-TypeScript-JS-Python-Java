class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function smallestNumber($n) {
        // If n is already a number with all set bits, return n
        if (($n & ($n + 1)) === 0) {
            return $n;
        }

        // Find the smallest power of 2 greater than n
        $power = 1;
        while ($power <= $n) {
            $power <<= 1;
        }

        // Return the number with all set bits up to the power
        return $power - 1;
    }
}