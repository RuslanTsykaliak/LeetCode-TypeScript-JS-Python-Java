class Solution {
    int MOD = 1000000007;

    public int numOfWays(int n) {

        // if n1 == 1 we can make 
        // 3 color pattern 123, 132, 213, 231, 312, 321
        // 2 color pattern 121, 131, 212, 232, 313, 323

        // for next row with every 3 color pattern from previous row we can make
        // eg 123 -> 231, 321 - make 2 color pattern of 3 different color so number of prev3Color pattern * 2
        // for next row with every 2 color pattern from previous row we can make
        // eg 121 -> 213, 312 - we can make pattern of 3 different color so number of prev2Color pattern * 2;

        // for next row with every 3 color pattern from previous row we can make
        // eg 123 -> 212, 313 - make 2 different pattern for 2 different color same color in edge so prev3Color * 2
        // for next row with every 2 color pattern from previous row we can make
        // eg 121 -> 212, 232, 313 - make 3 differnt pattern for 2 differnt color same color in edge so prev2Color * 3

        long prev3Color = 6;
        long prev2Color = 6;
        for (int i = 2; i <= n; i++) {
            long previousRow3ColorCount = prev3Color; //use for calculating 2 same color for next row
            prev3Color = (2 * prev3Color + 2 * prev2Color) % MOD;
            prev2Color = (2 * previousRow3ColorCount + 3 * prev2Color) % MOD;
        }

        return (int) (prev3Color + prev2Color) % MOD;
    }
}