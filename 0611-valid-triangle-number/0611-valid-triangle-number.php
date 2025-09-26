class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function triangleNumber($nums) {
        sort($nums);
        $count = 0;
        $n = count($nums);

        for ($i = $n - 1; $i >= 2; $i--) {
            $left = 0;
            $right = $i - 1;

            while ($left < $right) {
                if ($nums[$left] + $nums[$right] > $nums[$i]) {
                    $count += ($right - $left);
                    $right--;
                } else {
                    $left++;
                }
            }
        }
        return $count;
    }
}