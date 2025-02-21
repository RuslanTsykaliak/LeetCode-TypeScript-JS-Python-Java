class Solution {
    public int maximumWealth(int[][] accounts) {
        // Initialize the variable to store the wealth of the richest customer
        int wealth = 0;

        // Iterate over each customer (row in the accouns array)
        for (int i = 0; i < accounts.length; i++) {
            int customerWealth = 0;
            // Calculate the sum of all bank accounts for the current customer
            for (int j = 0; j < accounts[i].length; j++) {
                customerWealth += accounts[i][j];
            }
            // Update the wealth variable if the current customer's wealth is greater
            if (customerWealth > wealth) {
                wealth = customerWealth;
            }
        }
        return wealth;
    }
}