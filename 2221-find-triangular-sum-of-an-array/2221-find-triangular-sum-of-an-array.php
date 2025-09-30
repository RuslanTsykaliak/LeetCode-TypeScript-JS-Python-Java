class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function triangularSum($nums) {
        if (count($nums) === 1) {
            return $nums[0];
        }

        $newNums = [];

        for ($i = 0; $i < count($nums) - 1; $i++) {
            $newNums[] = ($nums[$i] + $nums[$i+1]) % 10;
        }

        return $this->triangularSum($newNums);
    }
}