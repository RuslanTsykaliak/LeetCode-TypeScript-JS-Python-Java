class Solution {

    /**
     * @param Integer[] $fruits
     * @param Integer[] $baskets
     * @return Integer
     */
    function numOfUnplacedFruits($fruits, $baskets) {
        $m = count($baskets);
        // To keep track of which baskets are used
        $used = array_fill(0, $m, false);
        $unplaced = 0;

        foreach ($fruits as $fruit) {
            $placed = false;
            for ($i = 0; $i < $m; $i++) {
                if (!$used[$i] && $baskets[$i] >= $fruit) {
                    $used[$i] = true;
                    $placed = true;
                    break;
                }
            }
            if (!$placed) {
                $unplaced++;
            }
        }
        
        return $unplaced;
    }
}