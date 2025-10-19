class Solution {
    private $ans = "";

    private function f($s, $a, $b, &$st) {
        if (isset($st[$s])) return;
        $st[$s] = true;
        if ($this->ans === "") $this->ans = $s;
        $this->ans = min($this->ans, $s);

        $temp = substr($s, -$b);
        $s = substr($s, 0, strlen($s) - $b);
        $s = $temp . $s;
        $this->f($s, $a, $b, $st);

        $s = substr($s, $b) . substr($s, 0, $b);

        for ($i = 1; $i < strlen($s); $i += 2) {
            $s[$i] = chr((((intval($s[$i]) + $a) % 10) + ord('0')));
        }
        $this->f($s, $a, $b, $st);
    }

    public function findLexSmallestString($s, $a, $b) {
        $st = [];
        $this->f($s, $a, $b, $st);
        return $this->ans;
    }
}