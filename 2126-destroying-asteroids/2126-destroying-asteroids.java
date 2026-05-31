class Solution {
    public boolean asteroidsDestroyed(int mass, int[] asteroids) {
        Arrays.sort(asteroids); // Sort by mass in ascending order
        long currentMass = mass; // Prevent integer overflow
        for (int asteroid : asteroids) {
            // Traverse the asteroids in order, attempt to destroy and update mass or return the result
            if (currentMass < asteroid) {
                return false;
            }
            currentMass += asteroid;
        }
        return true; // Successfully destroyed all asteroids
    }
}