class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function zeroFilledSubarray($nums) {
        $count = 0;
        $length = 0;
        for ($i = 0; $i < sizeof($nums); $i++) {
            if ($nums[$i] === 0) {
                $length++;
                $count += $length;
            } else $length = 0;
        }
        return $count;
    }
}