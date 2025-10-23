class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function hasSameDigits($s) {
        $arr = str_split($s);
        $len = count($arr);
        while ($len--) {
            $newArr = [];
            for ($i = 0; $i < count($arr) - 1; $i++) {
                $newArr []= ($arr[$i] + $arr[$i + 1]) % 10;
            }

            $arr = $newArr;

            if (count($newArr) == 2) {
              if($newArr[0] == $newArr[1]) return true;

              return false;
            }
        }
    }
}