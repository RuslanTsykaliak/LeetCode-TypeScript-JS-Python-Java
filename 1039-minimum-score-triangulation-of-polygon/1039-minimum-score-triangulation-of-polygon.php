class Solution {

    /**
     * @param Integer[] $values
     * @return Integer
     */
    function minScoreTriangulation($values) {
        $n = count($values);
        $dp = array_fill(0, $n, array_fill(0, $n, 0));

        for ($len = 3; $len <= $n; $len++) {
            for ($i = 0; $i + $len - 1 < $n; $i++) {
                $j = $i + $len - 1;
                $dp[$i][$j] = PHP_INT_MAX;
                for ($k = $i + 1; $k < $j; $k++) {
                    $dp[$i][$j] = min($dp[$i][$j], $dp[$i][$k] + $dp[$k][$j] + $values[$i] * $values[$j] * $values[$k]);
                }
            }
        }

        return $dp[0][$n - 1];
    }
}