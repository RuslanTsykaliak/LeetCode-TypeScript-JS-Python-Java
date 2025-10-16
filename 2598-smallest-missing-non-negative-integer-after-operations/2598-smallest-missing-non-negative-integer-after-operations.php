class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $value
     * @return Integer
     */
    function findSmallestInteger($nums, $value) {
        $valCount = [];
        foreach ($nums as $index => $num) {
            // find out the min value > 0
            if ($num < 0) {
                $nums[$index] += $value * ceil(abs($num) / $value);
            } elseif ($num >= $value) {
                $nums[$index] -= $value * floor($num / $value);
            }

            $newNum = $nums[$index];
            // count
            $valCount[$newNum] = isset($valCount[$newNum]) ? $valCount[$newNum] + 1 : 1;
        }

        // checking int loop from 0,1,2,3,4......
        $min = 0;
        while (true) {
            // turn int check also to be the min check
            $baseMin = $min % $value;
            // no available min int
            if (empty($valCount[$baseMin])) {
                return $min;
            }

            // available int minus 1
            $valCount[$baseMin]--;
            if ($valCount[$baseMin] == 0) {
                unset($valCount[$baseMin]);
            }

            $min++;
        }
    }
}