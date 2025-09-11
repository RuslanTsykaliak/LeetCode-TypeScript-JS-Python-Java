class Solution {

    /**
     * @param String $s
     * @return String
     */
    function sortVowels($s) {
        $vowelList = [];
        $vowelPosition = [];

        for($i=0; $i<strlen($s); $i++) {
        	$c = $s[$i];

        	if($c=='a' || $c=='e' || $c=='i' || $c=='o' || $c=='u' || $c=='A' || $c=='E' || $c=='I' || $c=='O' || $c=='U') {
        		$vowelList[] = $c;
        		$vowelPosition[] = $i;
        	}
        }
        sort($vowelList);
        $answer = str_split($s);

        for($i=0; $i<count($vowelList); $i++) {
        	$answer[$vowelPosition[$i]] = $vowelList[$i];
        }
        return implode("", $answer);
    }
}