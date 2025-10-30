class Solution {

    /**
     * @param Integer[] $target
     * @return Integer
     */
    function minNumberOperations($target) {
        $currentMax = 0;
        $result = 0;
        foreach ($target as $value) {
            if ($value > $currentMax) {
                $result += $value - $currentMax;
            }
            $currentMax = $value;
        }
        return $result;
    }
}