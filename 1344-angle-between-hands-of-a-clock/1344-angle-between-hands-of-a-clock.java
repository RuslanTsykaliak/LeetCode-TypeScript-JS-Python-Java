class Solution {
    public double angleClock(int hour, int minutes) {
        if (hour == 12)
            hour = 0;
        double ans = Math.abs((double) 30 * hour - 5.5 * (double) minutes);
        if (ans > 180) {
            return (double) 360 - ans;
        }
        return ans;
    }
}