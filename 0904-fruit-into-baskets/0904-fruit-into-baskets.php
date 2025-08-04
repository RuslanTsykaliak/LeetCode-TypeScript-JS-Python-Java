class Solution {

    /**
     * @param Integer[] $fruits
     * @return Integer
     */
    function totalFruit($fruits) {
        $i = 0;
        $tmpBasket = [];

        foreach($fruits as $j => $type) {
            $tmpBasket[$type] += 1;

            if (count($tmpBasket) > 2) {
                $tmpBasket[$fruits[$i]]--;

                if ($tmpBasket[$fruits[$i]] === 0) unset($tmpBasket[$fruits[$i]]);

                $i++;
            }
        }
        return $j - $i + 1;
    }
}