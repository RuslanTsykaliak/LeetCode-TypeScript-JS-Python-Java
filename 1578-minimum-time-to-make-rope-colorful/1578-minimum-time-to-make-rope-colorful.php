class Solution {

    /**
     * @param String $colors
     * @param Integer[] $neededTime
     * @return Integer
     */
    function minCost($colors, $neededTime) {
        $n = strlen($colors);
        $totalCost = 0;
        $maxCostInGroup = 0;

        for ($i = 0; $i < $n; $i++) {
            if ($i > 0 && $colors[$i] === $colors[$i - 1]) {
                $totalCost += min($neededTime[$i], $maxCostInGroup);
                $maxCostInGroup = max($neededTime[$i], $maxCostInGroup);
            } else {
                $maxCostInGroup = $neededTime[$i];
            }
        }
        return $totalCost;
    }
}