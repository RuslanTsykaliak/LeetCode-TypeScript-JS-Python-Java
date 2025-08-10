class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function reorderedPowerOf2($n) {
        for ($i = 0; $i < 32; $i++) { // based on the fact that $n <= 10^9
            $candidate = pow(2, $i);
            if ($this->canRearrange($n, $candidate)) {
                return true;
            }
        }
        return false;
    }
    
    function canRearrange($n, $candidate) {
        $map = [];
        $n = (string)$n;
        $candidate = (string)$candidate;
        for ($i = 0; $i < strlen($n); $i++) {
            if (!isset($map[$n[$i]])) {$map[$n[$i]] = 0;}
            $map[$n[$i]]++;
        }
        
        for ($i = 0; $i < strlen($candidate); $i++) {
            if (!isset($map[$candidate[$i]])) {$map[$candidate[$i]] = 0;}
            $map[$candidate[$i]]--;
        }

        return min($map) == 0 && max($map) == 0;
    }
}