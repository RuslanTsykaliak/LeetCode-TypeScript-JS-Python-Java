class Solution {

    /**
     * @param String[] $bank
     * @return Integer
     */
    function numberOfBeams($bank) {
        $res = 0;  
        $prev  = 0; 
        for($i = count($bank)-1; $i>=0; $i--){
            $count = 0;
            for($j = 0; $j<strlen($bank[$i]); $j++){
                if($bank[$i][$j] == '1') $count++;
            }
            if($count > 0){
                $res+=$prev*$count;
                $prev = $count;
            }
        }
        return $res;
    }

}