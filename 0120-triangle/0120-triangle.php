class Solution {

    /**
     * @param Integer[][] $triangle
     * @return Integer
     */
    function minimumTotal($triangle) {
        $rows = count($triangle);

        if ($rows == 0) return 0;

        for ($ri = $rows - 2; $ri >= 0; --$ri) {
            foreach ($triangle[$ri] as $i => &$value) {
                $left = $triangle[$ri + 1][$i];
                $right = $triangle[$ri + 1][$i + 1];

                $value = $value + min($left, $right);
            }
        }
        return $triangle[0][0];
    }
}