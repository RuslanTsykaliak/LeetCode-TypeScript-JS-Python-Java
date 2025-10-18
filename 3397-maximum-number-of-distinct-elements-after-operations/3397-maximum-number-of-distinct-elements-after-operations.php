class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maxDistinctElements($nums, $k) {
        sort($nums);
        $minValue = $nums[0] - $k;
        $distinct = 0;

        foreach ($nums as $num) {
            if ($minValue <= $num + $k) {
                $minValue = max($minValue, $num - $k) + 1;
                $distinct += 1;
            }
        }
        return $distinct;
    }
}