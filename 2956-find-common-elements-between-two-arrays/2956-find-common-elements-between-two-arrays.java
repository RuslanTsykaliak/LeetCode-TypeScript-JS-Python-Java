class Solution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {
        // Use Set to check for existing elements
        Set<Integer> seen1 = new HashSet<>();
        Set<Integer> seen2 = new HashSet<>();

        // for each to insert value into set
        for (int x : nums1) seen1.add(x);
        for (int x : nums2) seen2.add(x);

        // compare arrays versus sets from oposite array
        int a = 0, b = 0;
        for (int x : nums1) if (seen2.contains(x)) a++;
        for (int x : nums2) if (seen1.contains(x)) b++;

        return new int[]{a, b};
    }
}