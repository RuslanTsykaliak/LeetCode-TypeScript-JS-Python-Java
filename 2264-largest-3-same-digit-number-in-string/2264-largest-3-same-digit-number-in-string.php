class Solution {

    /**
     * @param String $num
     * @return String
     */
    function largestGoodInteger($num) {
        $arr = str_split($num, 1);
        $count = count($arr);
        if ($count < 3){
            return '';
        }
        
        $result = [];
        for ($i = 0; $i < $count; $i++) {
            if ($arr[$i] == $arr[$i + 1] && $arr[$i + 1] == $arr[$i + 2]) {
                $result[] = $arr[$i] . $arr[$i] . $arr[$i];
            }
        }

        return (!empty($result)) ? max($result) : "";
    }
}