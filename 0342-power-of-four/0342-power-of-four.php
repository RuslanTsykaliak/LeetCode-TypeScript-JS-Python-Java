class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isPowerOfFour($n) {
        while ($n > 1) {
            $n = $n / 4;
        }

        return $n == 1;
    }
}