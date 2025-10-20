class Solution {

    /**
     * @param String[] $operations
     * @return Integer
     */
    function finalValueAfterOperations($a) {
        $r = 0;
        foreach($a as $i)
            $r += (($i[1] === '+') ? 1 : -1);

        return $r;
    }
}