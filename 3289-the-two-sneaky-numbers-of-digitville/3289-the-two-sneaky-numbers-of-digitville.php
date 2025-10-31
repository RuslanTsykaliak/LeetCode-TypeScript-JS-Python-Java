class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function getSneakyNumbers($nums) {
        $counts = array_count_values($nums);
        $result = [];
        foreach ($counts as $k => $v) {
            if ($v > 1) {
                $result[] = $k;
            }
        }
        return $result;
    }
}