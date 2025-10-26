class Bank
{
    private $balance = 0;

    /**
     * @param Integer[] $balance
     */
    function __construct($balance) {
        $this->balance = $balance;
    }

    /**
     * @param Integer $account1
     * @param Integer $account2
     * @param Integer $money
     * @return Boolean
     */
    function transfer($account1, $account2, $money) {
        if (!isset($this->balance[$account1 - 1]) ||
            !isset($this->balance[$account2 - 1])
        ) {
            return false;
        }

        $account1_bal = $this->balance[$account1 - 1];

        if (($money <= $account1_bal)) {
            $this->balance[$account1 - 1] -= $money;
            $this->balance[$account2 - 1] += $money;
            return true;
        }

        return false;
    }

    /**
     * @param Integer $account
     * @param Integer $money
     * @return Boolean
     */
    function deposit($account, $money) {
        if (isset($this->balance[$account-1])) {
            $this->balance[$account-1] += $money;
            return true;
        }
        return false;
    }

    /**
     * @param Integer $account
     * @param Integer $money
     * @return Boolean
     */
    function withdraw($account, $money) {
        if (!isset($this->balance[$account-1])) {
            return false;
        }

        $account_balance = $this->balance[$account-1];

        if ($money <= $account_balance) {
            $this->balance[$account-1] -= $money;
            return true;
        }
        return false;
    }
}