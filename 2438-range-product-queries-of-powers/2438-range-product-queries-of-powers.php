class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function productQueries($n, $queries) {
        $powers = [];
        for ($i = 0; $i < 32; $i++) {
            if ($n & (1 << $i)) {
                $powers[] = $i;
            }
        }

        $answers = [];
        for ($i = 0; $i < count($queries); $i++) {
            $left = $queries[$i][0];
            $right = $queries[$i][1];
            $product = 1;
            for ($j = $left; $j <= $right; $j++) {
                $product = (int)($product * pow(2, $powers[$j])) % 1000000007;
            }
            $answers[] = $product;
        }

        return $answers;
    }
}